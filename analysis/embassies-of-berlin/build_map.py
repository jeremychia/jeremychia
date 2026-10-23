"""Embassies of Berlin: poster map. Run with:
uv run --with geopandas,matplotlib,requests,pandas,shapely,pyproj,pillow python build_map.py
All downloads are cached in ./data, so reruns are offline.
"""
import json
import re
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from matplotlib.patches import Rectangle
from PIL import Image
from shapely.geometry import LineString, Polygon
from shapely.ops import linemerge, polygonize, unary_union

HERE = Path(__file__).parent
DATA = HERE / "data"
FLAGS = DATA / "flags"
FLAGS.mkdir(parents=True, exist_ok=True)
CRS = "EPSG:25833"
UA = {"User-Agent": "embassy-map/1.0 (jeremyjchia@gmail.com)"}

BG, LAND, WATER, GREEN, EDGE, INK, MUTED, BAR = (
    "#f3efe4", "#e5ddcc", "#4f7f9a", "#b3c4a0", "#7a7266", "#1f3a3d", "#6b7a78", "#566f66")

# ---------- embassies ----------
NAME_FIX = {  # OSM entries lacking a usable country tag
    "Haiti": "HT", "Luxembourg": "LU", "Malaysia": "MY", "AW;CW;NL;SX": "NL",
    "Botschaft der Dominikanischen Republik": "DO", "Embassy of the Republic of Mauritius": "MU",
    "Residenz des Botschafters von Marokko": "MA", "Botschaft von Sri Lanka": "LK",
    "Botschaft von Indonesien": "ID",
}
NOT_EMBASSY = re.compile(r"residen[zc]|kultur|cultural|konsulat|consulate|wirtschaft|handels|iran haus", re.I)


def load_embassies():
    els = json.load(open(DATA / "osm_emb.json"))["elements"]
    rows = []
    for e in els:
        t = e["tags"]
        name = t.get("name", "")
        cc = t.get("country") or t.get("target")
        cc = NAME_FIX.get(cc) or NAME_FIX.get(name) or cc
        if not cc or len(cc) != 2 or cc == "EU" or cc == "DE":
            continue
        lat = e.get("lat") or e["center"]["lat"]
        lon = e.get("lon") or e["center"]["lon"]
        non = bool(NOT_EMBASSY.search(name + " " + t.get("name:en", "")))
        rows.append(dict(cc=cc, name=name, lat=lat, lon=lon, non=non, wd="wikidata" in t))
    df = pd.DataFrame(rows)
    # one point per country; prefer a real chancery over residences / cultural sections
    df = df.sort_values(["cc", "non", "wd"], ascending=[True, True, False]).drop_duplicates("cc")
    return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs="EPSG:4326").to_crs(CRS)


# ---------- OSM geometry ----------
def osm_polys(path):
    polys = []
    for el in json.load(open(path))["elements"]:
        if el["type"] == "way" and "geometry" in el:
            pts = [(g["lon"], g["lat"]) for g in el["geometry"]]
            if len(pts) > 3 and pts[0] == pts[-1]:
                polys.append(Polygon(pts))
        elif el["type"] == "relation":
            outer = [LineString([(g["lon"], g["lat"]) for g in m["geometry"]])
                     for m in el.get("members", []) if m.get("role") == "outer" and m.get("geometry")]
            inner = [LineString([(g["lon"], g["lat"]) for g in m["geometry"]])
                     for m in el.get("members", []) if m.get("role") == "inner" and m.get("geometry")]
            if not outer:
                continue
            o = unary_union(list(polygonize(linemerge(outer))))
            if inner:
                o = o.difference(unary_union(list(polygonize(linemerge(inner)))))
            polys.append(o)
    polys = [p.buffer(0) for p in polys if not p.is_empty]
    return gpd.GeoSeries(polys, crs="EPSG:4326").to_crs(CRS)


# ---------- flags ----------
def flag(cc):
    f = FLAGS / f"{cc.lower()}.png"
    if not f.exists():
        r = requests.get(f"https://flagcdn.com/w80/{cc.lower()}.png", headers=UA, timeout=30)
        if r.status_code != 200:
            return None
        f.write_bytes(r.content)
    return Image.open(f).convert("RGBA")


def spread(xy, w, h, iters=3000):
    """Push flag boxes apart (while a spring keeps them near their true spot)."""
    p = xy.copy()
    for _ in range(iters):
        d = np.zeros_like(p)
        for i in range(len(p)):
            dx = p[i, 0] - p[:, 0]
            dy = p[i, 1] - p[:, 1]
            ox = w * 1.12 - np.abs(dx)
            oy = h * 1.2 - np.abs(dy)
            m = (ox > 0) & (oy > 0)
            m[i] = False
            for j in np.where(m)[0]:
                if ox[j] < oy[j]:
                    d[i, 0] += np.sign(dx[j] or np.random.uniform(-1, 1)) * ox[j] * 0.5
                else:
                    d[i, 1] += np.sign(dy[j] or np.random.uniform(-1, 1)) * oy[j] * 0.5
        d += (xy - p) * 0.002
        p += d
    return p


def main():
    np.random.seed(7)
    emb = load_embassies()
    bez = gpd.read_file(DATA / "bezirke.geojson").to_crs(CRS)[["Gemeinde_name", "geometry"]]
    city = bez.geometry.union_all()
    water = osm_polys(DATA / "osm_water.json")
    green = osm_polys(DATA / "osm_green.json")
    water = gpd.GeoSeries([water.union_all().intersection(city)], crs=CRS)
    green = gpd.GeoSeries([green.union_all().intersection(city).difference(water.union_all())], crs=CRS)

    emb = emb[emb.within(city.buffer(500))].copy()
    emb["bezirk"] = gpd.sjoin(emb, bez, how="left", predicate="within")["Gemeinde_name"].values
    counts = emb.bezirk.value_counts()
    print(len(emb), "embassies\n", counts.to_string())
    print("unassigned:", emb.bezirk.isna().sum())
    emb.drop(columns="geometry").to_csv(DATA / "embassies_clean.csv", index=False)

    # view: zoom on where the embassies are
    xs, ys = emb.geometry.x, emb.geometry.y
    x0, x1 = np.percentile(xs, [8, 92])
    y0, y1 = np.percentile(ys, [8, 92])
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    W = max(x1 - x0, 1.0) * 1.2
    ax_w, ax_h = 0.95 * 18, 0.66 * 11.8  # px-ish proportions of the map panel (matches the Paris poster)
    H = W * ax_h / ax_w
    if (y1 - y0) * 1.2 > H:
        H = (y1 - y0) * 1.2
        W = H * ax_w / ax_h
    xlim, ylim = (cx - W / 2, cx + W / 2), (cy - H / 2, cy + H / 2)

    fig = plt.figure(figsize=(18, 11.8), facecolor=BG)
    fig.text(0.065, 0.925, "EMBASSIES OF BERLIN", fontsize=40, fontweight="bold", color=INK, va="center")
    fig.text(0.067, 0.88, f"Locations of Berlin’s {len(emb)} resident foreign embassies.",
             fontsize=15, color="#4a5c5a", va="center")

    # bar chart per district
    bx = fig.add_axes([0.50, 0.80, 0.47, 0.10], facecolor=BG)
    order = list(counts.index) + [b for b in bez.Gemeinde_name if b not in counts.index]
    vals = [int(counts.get(b, 0)) for b in order]
    bx.bar(range(len(order)), vals, color=BAR, width=0.55)
    for i, v in enumerate(vals):
        bx.text(i, v + max(vals) * 0.03, str(v) if v else "", ha="center", va="bottom", fontsize=8, color=INK)
    bx.set_xticks(range(len(order)), [o.replace('Charlottenburg-Wilmersdorf','Charlottenb.-Wilmersdorf') for o in order], fontsize=8, color=INK)
    bx.set_yticks([])
    for s in bx.spines.values():
        s.set_visible(False)
    bx.spines["bottom"].set_visible(True)
    bx.spines["bottom"].set_color("#bbb")
    bx.tick_params(length=0)
    bx.set_ylim(0, max(vals) * 1.25)
    bx.set_title("Embassies by district (Bezirk)", fontsize=11, color=INK, loc="left", pad=14)
    plt.setp(bx.get_xticklabels(), rotation=30, ha="right", fontsize=7.5)

    ax = fig.add_axes([0.025, 0.065, 0.95, 0.66], facecolor="#c6c9bb")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    bez.plot(ax=ax, color=LAND, edgecolor=EDGE, linewidth=1.0, zorder=1)
    green.plot(ax=ax, color=GREEN, zorder=2)
    water.plot(ax=ax, color=WATER, zorder=3)
    bez.boundary.plot(ax=ax, color=EDGE, linewidth=0.9, zorder=4)
    for _, r in bez.iterrows():
        p = r.geometry.representative_point()
        if xlim[0] < p.x < xlim[1] and ylim[0] < p.y < ylim[1]:
            ax.text(p.x, p.y, r.Gemeinde_name, fontsize=12, color="#5b564c", ha="center", va="center", zorder=5, alpha=0.55)

    fw = W * 0.0145  # flag width in map units
    fh = fw * 0.68
    xy = np.c_[xs, ys]
    pos = spread(xy, fw, fh)
    for (px, py), (ox, oy), cc in zip(pos, xy, emb.cc):
        im = flag(cc)
        if im is None:
            print("no flag", cc)
            continue
        if np.hypot(px - ox, py - oy) > fw * 0.6:
            ax.plot([ox, px], [oy, py], color="#333", lw=0.4, zorder=6)
        ax.plot(ox, oy, "o", ms=1.8, color="#222", zorder=7)
        # draw the flag with exact map-unit extents so image and border always coincide
        w = fh * im.width / im.height  # keep each flag's true proportions
        ax.imshow(np.asarray(im), extent=(px - w / 2, px + w / 2, py - fh / 2, py + fh / 2),
                  zorder=8, interpolation="lanczos", aspect="auto")
        ax.add_patch(Rectangle((px - w / 2, py - fh / 2), w, fh, fill=False, ec="#444", lw=0.4, zorder=9))

    out = int((~((xs > xlim[0]) & (xs < xlim[1]) & (ys > ylim[0]) & (ys < ylim[1]))).sum())
    ax.text(0.02, 0.96, f"{out} outlying embassies fall outside this view (counted in the chart)", transform=ax.transAxes, fontsize=8.5, color=MUTED, va="top", zorder=9)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    # north arrow, scale bar
    ax.text(0.975, 0.945, "N ↑", transform=ax.transAxes, ha="right", fontsize=10, color=INK)
    sb = 2000
    bx0, by0 = xlim[0] + W * 0.03, ylim[0] + H * 0.045
    ax.plot([bx0, bx0 + sb], [by0, by0], color="#222", lw=1.5, zorder=9)
    ax.text(bx0 + sb / 2, by0 + H * 0.012, "2 km", ha="center", va="bottom", fontsize=9, color=INK, zorder=9)

    fig.text(0.04, 0.025, "Map by Jeremy Chia", fontsize=7.5, color=MUTED)
    fig.text(0.975, 0.032, "Source: OpenStreetMap contributors (diplomatic=embassy; one chancery per country) • Flags: flagcdn.com",
             fontsize=7.5, color=MUTED, ha="right")
    fig.text(0.975, 0.018, "Districts: ALKIS Berlin (Geoportal Berlin) • Water & green: OpenStreetMap • ETRS89 / UTM 33N • EPSG:25833",
             fontsize=7.5, color="#8a9693", ha="right")
    fig.savefig(HERE / "embassies_of_berlin.png", dpi=150, facecolor=BG)
    print("saved")


if __name__ == "__main__":
    main()
