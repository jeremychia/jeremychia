"""render each doc here as paste-ready html; needs the markdown package (pip install markdown)."""
import re
import markdown

for name in ("self-assessment", "pl4-pathway"):
  src = open(f"{name}.md").read()
  src = re.sub(r"<details>.*?</details>", "", src, flags=re.S)  # the compilation note stays in the markdown only
  src = re.sub(r"`(\[[^`]+\])`", r"\1", src)  # value tags as plain text, not code
  body = markdown.markdown(src, extensions=["tables", "sane_lists"])
  style = "body{font-family:Arial,sans-serif;font-size:11pt;max-width:1200px}table{border-collapse:collapse;margin:8px 0}td,th{border:1px solid #999;padding:6px;vertical-align:top;text-align:left}th{background:#eee}blockquote{border-left:3px solid #999;margin:8px 0;padding-left:12px;color:#333}"
  open(f"{name}.html", "w").write(f'<!doctype html><html><head><meta charset="utf-8"><title>{name}</title><style>{style}</style></head><body>{body}</body></html>')
