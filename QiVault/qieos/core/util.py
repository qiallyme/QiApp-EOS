from pathlib import Path

IGNORE_DIRS = {
    ".git", ".obsidian", "node_modules", "__pycache__", "venv", ".venv", "dist", "build", ".npm", ".pnpm-store", "dat/tmp", "dat/out"
}
IGNORE_FILES = {".env", "service-account.json"}

def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & IGNORE_DIRS:
        return True
    if path.name in IGNORE_FILES:
        return True
    return False

def export_code_bundle(repo_root: Path) -> Path:
    out_dir = repo_root / "dat" / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    tgt = out_dir / "code_export.html"

    rows = []
    for p in sorted(repo_root.rglob("*")):
        if p.is_dir():
            continue
        if should_skip(p):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        rel = p.relative_to(repo_root)
        rows.append((str(rel), text))

    tgt.write_text(_render_html(rows), encoding="utf-8")
    return tgt

def _render_html(rows):
    css = """
    body{font-family:Roboto,system-ui,Segoe UI,Arial; margin:0; background:#fafafa; color:#111}
    header{position:sticky;top:0;background:#fff;border-bottom:1px solid #eee;padding:10px 16px;display:flex;gap:12px;align-items:center}
    .toggle{cursor:pointer;padding:6px 10px;border:1px solid #ddd;border-radius:6px}
    .wrap{display:grid;grid-template-columns:320px 1fr;height:calc(100vh - 52px)}
    nav{border-right:1px solid #eee;overflow:auto}
    main{overflow:auto}
    .file{padding:8px 12px;border-bottom:1px solid #f0f0f0;cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
    .file:hover{background:#f6f6f6}
    pre{margin:0;padding:16px;white-space:pre-wrap;word-break:break-word}
    .dark body{background:#0f0f10;color:#eaeaea}
    .dark header{background:#151517;border-bottom-color:#2a2a2a}
    .dark nav{border-right-color:#2a2a2a}
    .dark .file{border-bottom-color:#1f1f1f}
    .dark .file:hover{background:#1a1a1b}
    .dark pre{background:#141416}
    """
    js = """
    const files = %ROWS%;
    const list = document.getElementById('list');
    const pre  = document.getElementById('code');
    files.forEach(([name, text])=>{
      const div=document.createElement('div'); div.className='file'; div.textContent=name;
      div.onclick=()=>{ pre.textContent = text; location.hash = encodeURIComponent(name); };
      list.appendChild(div);
    });
    if(location.hash){
      const target = decodeURIComponent(location.hash.slice(1));
      const row = files.find(([n])=>n===target);
      if(row){ pre.textContent = row[1]; }
    } else if(files.length){ pre.textContent = files[0][1]; }
    document.getElementById('toggle').onclick=()=>{
      document.documentElement.classList.toggle('dark');
    };
    """
    rows_json = "[\n" + ",\n".join([f"[{_j(n)},{_j(t)}]" for n,t in rows]) + "\n]"
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Qi Code Export</title>
<style>{css}</style></head><body>
<header><strong>Qi Code Export</strong><div id="toggle" class="toggle">Toggle Theme</div></header>
<div class="wrap">
  <nav id="list"></nav>
  <main><pre id="code"></pre></main>
</div>
<script>{js.replace("%ROWS%", rows_json)}</script>
</body></html>"""

def _j(s:str)->str:
    return '"' + s.replace("\\","\\\\").replace('"','\\"').replace("\n","\\n") + '"'
