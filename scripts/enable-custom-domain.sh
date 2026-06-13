#!/usr/bin/env bash
# Enable a custom GitHub Pages domain for the portfolio site.
# Usage: ./scripts/enable-custom-domain.sh www.example.com
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <hostname>" >&2
  echo "Example: $0 www.giselleevitakoch.com" >&2
  exit 1
fi

HOST="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BASE="https://${HOST%/}/"

python3 - "$HOST" "$BASE" "$ROOT" <<'PY'
import json, pathlib, re, sys
host, base, root = sys.argv[1:4]
root = pathlib.Path(root)
config = json.loads((root / "site-config.json").read_text())
config["canonicalUrl"] = base
config["customDomain"] = host
(root / "site-config.json").write_text(json.dumps(config, indent=2) + "\n")
html = (root / "index.html").read_text()
html = re.sub(r'content="https://[^"]+/portfolio/og-image\.png"', f'content="{base}og-image.png"', html)
html = re.sub(r'content="https://[^"]+/portfolio/"', f'content="{base}"', html)
(root / "index.html").write_text(html)
print(f"Updated site-config.json and index.html for {base}")
PY

echo "$HOST" > "$ROOT/CNAME"
echo "Wrote CNAME -> $HOST"
echo "Next: commit CNAME + changes, push main, then set the same hostname under GitHub repo Settings → Pages → Custom domain."
