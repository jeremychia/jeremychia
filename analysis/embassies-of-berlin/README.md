# Embassies of Berlin

Poster map replicating the "Embassies of Paris" design for Berlin: a flag per resident embassy, an embassies-per-Bezirk bar chart, districts, water and green areas.

Run: `uv run --with geopandas,matplotlib,requests,pandas,shapely,pyproj,pillow python build_map.py` → `embassies_of_berlin.png`. Downloads are cached in `data/`, so reruns are offline.

## Plan (as approved)

**Context.** Recreate the Paris poster for Berlin. The poster is a static map with labelled district polygons, water and green areas, a flag for each embassy at its location, a per-district bar chart, a title and subtitle, a scale bar, a north arrow and a source footer.

**Layout of this folder**
- `build_map.py`: single script running the pipeline below
- `data/`: cached downloads and the cleaned embassy table
- `embassies_of_berlin.png`: output (2700×1770)

**Pipeline**
1. **Embassy list.** *Planned:* scrape Wikipedia's list of diplomatic missions. *Built instead:* OpenStreetMap `diplomatic=embassy` via Overpass, because it already carries coordinates and a country code, so no geocoding step was needed. Embassies are filtered to one chancery per country; residences, cultural sections and the EU mission are dropped.
2. **Boundaries.** The 12 Bezirke from the ALKIS open data, in EPSG:25833 (ETRS89 / UTM 33N).
3. **Water and green.** OSM water polygons plus forests and parks, clipped to the city outline. Palette: cream background, beige districts, steel-blue water, sage green.
4. **Flags.** PNGs from flagcdn.com by ISO-2 code. Each flag is drawn at its true proportions with exact map-unit extents, so the image and its border always line up.
5. **Overlap handling.** Flags are pushed apart by a relaxation loop, with a dot and a leader line at the true location.
6. **Layout.** Bold title, subtitle with the computed count, bar chart (counts per Bezirk), map, "N ↑", 2 km scale bar, credit and source footer.

**Verification**
- Counts: every embassy is assigned to a district (0 unassigned), and the chart sums to the total (158).
- Visual check against the Paris poster: flags legible, borders aligned, no overlaps.
- Rerun uses the cache, so it is deterministic and offline.

## Deviations and caveats
- Map is zoomed on the embassy core, because most embassies sit in a small central area. A note on the map says how many outlying embassies fall outside the view; they are still counted in the chart.
- Counts depend on OSM completeness (158 here) and may differ from the official list. A few OSM entries lack a country tag and are patched by name in `NAME_FIX`.
