#!/usr/bin/env python3
"""Build an offline, single-file preview with hash-authorised inline assets."""
from pathlib import Path
import argparse, base64, hashlib, re
ROOT = Path(__file__).resolve().parents[1]

def build(output: Path) -> None:
    site=ROOT/'site'
    html=(site/'index.html').read_text(encoding='utf-8')
    css=(site/'assets/style.css').read_text(encoding='utf-8')
    data=(site/'data/brief.js').read_text(encoding='utf-8')
    js=(site/'assets/app.js').read_text(encoding='utf-8')
    digest=lambda s: "'sha256-"+base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()+"'"
    csp=f"default-src 'none'; script-src {digest(data)} {digest(js)}; style-src {digest(css)}; img-src data:; object-src 'none'; base-uri 'none'; form-action 'none'"
    html=re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]+>',f'<meta http-equiv="Content-Security-Policy" content="{csp}">',html)
    icon=base64.b64encode((site/'assets/favicon.svg').read_bytes()).decode()
    html=html.replace('href="assets/favicon.svg"',f'href="data:image/svg+xml;base64,{icon}"')
    html=html.replace('<link rel="stylesheet" href="assets/style.css">','<style>'+css+'</style>')
    html=html.replace('<script defer src="data/brief.js"></script>','').replace('<script defer src="assets/app.js"></script>','')
    html=html.replace('</body>','<script>'+data+'</script>\n<script>'+js+'</script>\n</body>')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(html,encoding='utf-8')
    print(f'Preview built: {output} ({output.stat().st_size:,} bytes)')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'kirish-brief-preview.html')
    build(parser.parse_args().output)
