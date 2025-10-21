# Qi-App EOS Developer Guide (Windows-only)

> Version 0.1 • Updated: 2025-10-19
> Scope: Windows 10/11, Python 3.11, zero Docker, zero Node.
> Goal: Flat, portable, double-clickable mini-app skeletons you can resell, reuse, or embed in the QiVerse Cockpit.

---

## 1) What this includes

* **`qieos/`**: the base template every Qi mini-app starts from
* **`qimini/`**: a Hello-World template proving launch, outputs, and GUI popup
* Standardized **Danger Zone** contract so the Cockpit can load any app immediately
* Portable **virtualenv** bootstrap (Windows) and **double-click run** scripts
* Built-in **code exporter** (HTML file tree + contents)
* `.env.example`, `.gitignore`, `.obsidianignore` wired for your stack
* Revenue-aware licensing guidance and enterprise hooks

---

## 2) Prerequisites

* **Windows 10/11**
* **Python 3.11** (`py --version` should show 3.11.x)
* Optional: **Git** (for version control)
* No Node required for these Python templates. We’ll add React/Vite variants later.

---

## 3) Directory layout (what you’ll have)

```
QiVault/
└─ apps/
   ├─ qieos/      # base EOS template
   └─ qimini/     # hello-world template built on EOS
```

You can place these folders anywhere (even on a USB). They’re self-contained.

---

## 4) Danger Zone: do not rename/move

Inside each app:

* `qi.yaml`
* `main.py`
* `core/hook.py`

If you rename or move those, the Cockpit and EOS rules won’t recognize your app.

---

## 5) The EOS template (qieos/)

### 5.1 Structure

```
qieos/
├─ qi.yaml
├─ main.py
├─ ai.rules
├─ readme.md
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ .obsidianignore
├─ run-win.bat
├─ install-win.bat
├─ core/
│  ├─ run.py
│  ├─ hook.py
│  ├─ ui.py
│  └─ util.py
├─ ast/
│  ├─ ico/qi.svg
│  ├─ tpl/base.html
│  └─ smpl/sample.txt
└─ dat/
   ├─ in/.keep
   ├─ out/.keep
   └─ tmp/.keep
```

### 5.2 Files (copy/paste exact)

#### `qi.yaml`

```yaml
app:
  id: qieos
  name: Qi-App EOS
  ver: 0.1.0
  desc: "QiVerse root template for modular app integration."
  auth: QiAlly
  cat: core
  cockpit: true
  entry: main.py
  out: ["json"]
  mode: eos

paths:
  base_out: "./dat/out"
  base_tmp: "./dat/tmp"
```

#### `main.py`

```python
from core.run import go
import json, sys, yaml, pathlib

def boot(args=None):
    """Launch app locally or via QiCockpit."""
    here = pathlib.Path(__file__).parent
    cfg = yaml.safe_load((here / "qi.yaml").read_text(encoding="utf-8"))
    # load .env if present
    try:
        from dotenv import load_dotenv
        load_dotenv(here / ".env")
    except Exception:
        pass
    return go(args or {}, cfg)

if __name__ == "__main__":
    args = {}
    if len(sys.argv) > 1:
        args["in"] = sys.argv[1]
    print(json.dumps(boot(args), ensure_ascii=False, indent=2))
```

#### `ai.rules`

```
# Qi-App EOS Rules (Windows)
1) Folder names are fixed: core, ast, dat.
2) Every app exposes boot() in main.py and go() in core/run.py.
3) qi.yaml must exist and declare entry + outputs.
4) Apps write to ./dat/out by default.
5) Cockpit handshake lives in core/hook.py.
6) Do not rename qi.yaml, main.py, or core/hook.py.
7) No secrets in git. Use .env and .env.example.
8) Code exporter must exclude venv/, node_modules/, dist/, build/, __pycache__/.
```

#### `readme.md`

```markdown
# Qi-App EOS (Windows)

Origin template for all QiVerse mini-apps. Flat, portable, double-clickable.

## Danger Zone
- `qi.yaml`, `main.py`, `core/hook.py` — do not rename or relocate.

## Run (double-click)
- `run-win.bat`

## Install (optional; creates venv)
- `install-win.bat`

## CLI examples
```powershell
python main.py                # sanity run
python main.py dat/in/foo     # pass input path
python -m core.ui --help      # full CLI
python -m core.ui --export    # export code bundle HTML to dat/out/
```

## Structure
- `core/` logic (run.py, ui.py, hook.py, util.py)
- `ast/`  assets (ico, tpl, smpl)
- `dat/`  in/out/tmp working dirs
```

#### `requirements.txt`

```
PySimpleGUI>=5.0.0
python-dotenv>=1.0.1
PyYAML>=6.0.2
rich>=13.7.1
```

#### `.env.example`

```env
# Database
SUPABASE_URL=
SUPABASE_ANON_KEY=
SUPABASE_SERVICE_KEY=

# AI
OPENAI_API_KEY=
GEMINI_API_KEY=

# Hosting/CDN
CLOUDFLARE_ACCOUNT_ID=
CLOUDFLARE_API_TOKEN=

# Mail (you said Zep2Mail + Zoho)
ZEP2MAIL_API_KEY=
ZOHO_MAIL_USER=
ZOHO_MAIL_APP_PASSWORD=

# Storage/Media
CLOUDINARY_URL=
GOOGLE_APPLICATION_CREDENTIALS=./service-account.json

# CRM/PM
HONEYBOOK_API_KEY=

# Misc
QIALly_ENV=dev
```

#### `.gitignore`

```
# env & secrets
.env
*.pem
service-account.json

# python
__pycache__/
*.pyc
.venv/
venv/
build/
dist/

# node
node_modules/
.npm/
.pnpm-store/
pnpm-lock.yaml

# os/editor
.DS_Store
Thumbs.db
.idea/
.vscode/

# app outputs
dat/out/
dat/tmp/

# obsidian vault noise
.obsidian/
```

#### `.obsidianignore`

```
venv/
.venv/
node_modules/
dist/
build/
__pycache__/
dat/out/
dat/tmp/
```

#### `run-win.bat`

```bat
@echo off
setlocal
IF NOT EXIST .venv (
  echo [Qi] Creating venv...
  py -3 -m venv .venv
  call .venv\Scripts\pip install -r requirements.txt
)
call .venv\Scripts\python main.py
pause
```

#### `install-win.bat`

```bat
@echo off
py -3 -m venv .venv
call .venv\Scripts\pip install -r requirements.txt
echo [Qi] Installed.
pause
```

#### `core/run.py`

```python
from pathlib import Path
from datetime import datetime
import json

def go(args, cfg):
    """Primary logic entrypoint. Keep returns structured."""
    out_dir = Path(cfg["paths"]["base_out"])
    out_dir.mkdir(parents=True, exist_ok=True)

    # trivial heartbeat for sanity
    stamp = datetime.now().isoformat(timespec="seconds")
    result = {
        "app": cfg["app"]["id"],
        "ver": cfg["app"]["ver"],
        "ok": True,
        "ts": stamp,
        "note": "Qi-App EOS heartbeat",
        "args": args
    }
    (out_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result
```

#### `core/hook.py`

```python
def hook(meta):
    """Registers this app with QiCockpit."""
    return {
        "id": meta["app"]["id"],
        "name": meta["app"]["name"],
        "entry": meta["app"]["entry"],
        "ver": meta["app"]["ver"],
        "out": meta["app"]["out"],
        "mode": meta["app"]["mode"],
    }
```

#### `core/ui.py`

```python
import argparse, json
from .run import go
from pathlib import Path
import yaml

def parse():
    p = argparse.ArgumentParser(prog="qieos", description="Qi-App EOS CLI")
    p.add_argument("--in", dest="in_", help="input path", default=None)
    p.add_argument("--out", dest="out", help="output dir override", default=None)
    p.add_argument("--export", action="store_true", help="export code bundle (HTML)")
    return p.parse_args()

def _load_cfg():
    here = Path(__file__).resolve().parent.parent
    return yaml.safe_load((here / "qi.yaml").read_text(encoding="utf-8"))

def main():
    args = parse()
    cfg = _load_cfg()
    if args.out:
        cfg["paths"]["base_out"] = args.out

    if args.export:
        from .util import export_code_bundle
        html = export_code_bundle(repo_root=Path(__file__).parent.parent)
        print(json.dumps({"export": str(html)}, indent=2))
        return

    res = go({"in": args.in_} if args.in_ else {}, cfg)
    print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```

#### `core/util.py`

```python
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
```

#### `ast/ico/qi.svg`

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#07c"/><text x="32" y="38" font-size="28" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif">Qi</text></svg>
```

#### `ast/tpl/base.html`

```html
<!doctype html><meta charset="utf-8"><title>Qi Base</title>
<link rel="icon" href="../ico/qi.svg">
<style>body{font-family:Roboto,Arial; padding:24px}</style>
<h1>Qi Base Template</h1>
<p>Replace me.</p>
```

---

## 6) The Hello-World template (qimini/)

It’s identical to EOS with small changes:

#### `qimini/qi.yaml`

```yaml
app:
  id: qimini
  name: QiMini
  ver: 0.1.0
  desc: "Hello-World proof template."
  auth: QiAlly
  cat: demo
  cockpit: true
  entry: main.py
  out: ["txt","json"]
  mode: app

paths:
  base_out: "./dat/out"
  base_tmp: "./dat/tmp"
```

#### `qimini/core/run.py`

```python
from pathlib import Path
from datetime import datetime
import json

def go(args, cfg):
    out_dir = Path(cfg["paths"]["base_out"]); out_dir.mkdir(parents=True, exist_ok=True)
    hello = f"Hello World from {cfg['app']['name']} at {datetime.now().isoformat(timespec='seconds')}"
    (out_dir / "hello.txt").write_text(hello, encoding="utf-8")

    # optional GUI popup when run from double-click scripts
    try:
      import PySimpleGUI as sg
      sg.theme("LightGrey1")
      sg.popup(hello, title="QiMini", keep_on_top=True)
    except Exception:
      pass

    result = {"app": cfg["app"]["id"], "ok": True, "hello": hello}
    (out_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result
```

Everything else matches `qieos/`.

---

## 7) Step-by-step: run it now (Windows)

1. **Place** `qieos/` and `qimini/` anywhere (e.g., `D:\QiVault\apps\` or a USB drive).
2. **Double-click** `qimini/run-win.bat`.

   * It creates a `.venv` if missing and installs Python deps.
   * A popup shows “Hello World…”
   * Outputs are in `qimini/dat/out/`:

     * `hello.txt`
     * `result.json`
3. **Optional CLI**

   * In the app folder, Shift+Right-click → Open PowerShell →
     `python main.py`
     `python -m core.ui --export` → creates `dat/out/code_export.html`

---

## 8) Create your own app from EOS

1. Copy the base:

   ```
   cd D:\QiVault\apps
   xcopy /E /I qieos qiscribe
   ```
2. Edit `qiscribe/qi.yaml`:

   * `id: qiscribe`
   * `name: QiScribe`
   * `desc: "Message transcript compiler."`
   * `out: ["pdf","json","txt"]`
   * Leave `entry: main.py` as is.
3. Put your logic in `qiscribe/core/run.py` (keep function name `go`).
4. Double-click `qiscribe/run-win.bat`.
   Now it’s recognized by the Cockpit the same way as any other QiApp.

---

## 9) Environment & integrations (your stack)

* Supabase, OpenAI, Gemini, Cloudflare, Zep2Mail, Zoho Mail, Cloudinary, Drive, HoneyBook env keys are **optional**.
* Add real values to `.env` (copy from `.env.example`).
* Apps will load `.env` automatically if present.
* For Google Drive service account, drop `service-account.json` and set the path in `.env` (it’s `.gitignore`d).

**Note on Drive links:** if you prefer sharing links rather than API calls, just store the share URLs in your app’s config or metadata. Authentication stays with the user who opens the link. No API required.

---

## 10) Portability

* These apps are designed to **run from a USB**.
* First run creates a local `.venv` in the app folder and installs requirements.
* No global installs needed.

---

## 11) Built-in “Code Extractor”

From the app folder:

```
python -m core.ui --export
```

Generates `dat/out/code_export.html` with a left-pane file list and right-pane file contents, ignoring venv, node_modules, dist, build, caches, and outputs.

---

## 12) Standard CLI flags (Windows)

* `--in` path to input file or folder
* `--out` override output directory
* `--export` generate the HTML code bundle

Examples:

```
python main.py dat/in/sample.txt
python -m core.ui --out D:\Exports\MyApp
python -m core.ui --export
```

---

## 13) Branding & UI defaults

* Fonts: **Roboto** (primary), **system UI** fallback
* Default **Light** theme; dark toggle in HTML exporter
* Minimal CSS, glass-adjacent, consistent with QiCockpit

---

## 14) Revenue & licensing (future options)

Start **private** while iterating. When you’re ready to share:

* **QiAlly Commons License v0.1 (Draft)**

  * Personal use and businesses with **≤ $150k annual gross**: free
  * Above threshold or multi-employee teams: paid license (subscription or per-seat)
  * Redistribution allowed only with license intact; no resale of code itself
  * Offer **Enterprise Add-Ons**:

    * Branded builds and custom manifests
    * SSO, audit logging, remote config
    * Priority SLA and onboarding
    * Private connectors (HoneyBook, Drive SA, Zep2Mail workflows)

Nothing in code changes for this yet; it’s policy. You can add a `LICENSE` later and a `license.json` flag in `qi.yaml` if you want apps to display license status in the UI.

---

## 15) Troubleshooting

* **Double-click script closes instantly:** run from PowerShell to see the error. Usually Python not found or blocked by antivirus.
* **Venv fails to create:** ensure `py` launcher exists (`py --version`). If not, install Python 3.11 from python.org and re-run.
* **No popup in QiMini:** PySimpleGUI import failed. Check `dat/out/result.json` for success; then run `install-win.bat`.
* **Exporter shows empty:** ensure the repo has files beyond ignored dirs, and you ran in the correct folder.

---

## 16) Roadmap hooks (already accounted for)

* **Cockpit handshake** via `core/hook.py`
* **Stable entrypoints**: `boot()` in `main.py`, `go()` in `core/run.py`
* **Flat structure**: `core`, `ast`, `dat`
* **React/Vite/Tauri/Electron** templates will follow with the same Danger Zone contract and Windows run scripts
* **Supabase/OpenAI/Gemini/Cloudflare/etc.** env slots reserved in `.env.example`

---

## 17) Quick checklist (print this)

* [ ] Copy `qieos/` to new app folder
* [ ] Edit `qi.yaml` IDs, name, desc, outputs
* [ ] Implement logic in `core/run.py::go()`
* [ ] Double-click `run-win.bat`
* [ ] Verify `dat/out/` artifacts
* [ ] Optionally: `python -m core.ui --export` for code bundle
* [ ] Commit with `.env` excluded
* [ ] Ready for Cockpit

---

If you follow this doc exactly, you get a working, Windows-native, plug-and-play QiApp that connects to the QiVerse on first run and doesn’t waste your time with toolchain drama.
