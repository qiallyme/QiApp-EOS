# Code Export — /workspaces/QiApp-EOS

## Directory Tree
```text
QiApp-EOS/
└── .gitignore
└── Developer Guide (Windows-only).md
└── LICENSE
└── QiVault/
│   └── apps/
│   │   └── README.md
│   └── qieos/
│   │   └── .env.example
│   │   └── .gitignore
│   │   └── .obsidianignore
│   │   └── ai.rules
│   │   └── ast/
│   │   │   └── smpl/
│   │   │   │   └── sample.txt
│   │   │   └── tpl/
│   │   │   │   └── base.html
│   │   └── core/
│   │   │   └── hook.py
│   │   │   └── run.py
│   │   │   └── ui.py
│   │   │   └── util.py
│   │   └── dat/
│   │   │   └── in/
│   │   │   │   └── .keep
│   │   │   └── out/
│   │   │   │   └── .keep
│   │   │   └── tmp/
│   │   │   │   └── .keep
│   │   └── install-win.bat
│   │   └── main.py
│   │   └── qi.yaml
│   │   └── readme.md
│   │   └── requirements.txt
│   │   └── run-win.bat
│   └── qimini/
│   │   └── .gitignore
│   │   └── .obsidianignore
│   │   └── ai.rules
│   │   └── ast/
│   │   │   └── smpl/
│   │   │   │   └── sample.txt
│   │   │   └── tpl/
│   │   │   │   └── base.html
│   │   └── core/
│   │   │   └── hook.py
│   │   │   └── run.py
│   │   │   └── ui.py
│   │   └── dat/
│   │   │   └── in/
│   │   │   │   └── .keep
│   │   │   └── out/
│   │   │   │   └── .keep
│   │   │   └── tmp/
│   │   │   │   └── .keep
│   │   └── install-win.bat
│   │   └── main.py
│   │   └── qi.yaml
│   │   └── requirements.txt
│   │   └── run-win.bat
└── README.md
└── qi_code_extract.py
```

---
## Files

### .gitignore

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Dependency directories
node_modules/
jspm_packages/
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional caches
.npm
.eslintcache
.stylelintcache

# REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn v3
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/sdks
!.yarn/versions

# Frontend frameworks output
.next
.nuxt
dist
out
.cache
.parcel-cache
.vuepress/dist
.temp
.svelte-kit/
**/.vitepress/dist
**/.vitepress/cache
.docusaurus

# Serverless & misc
.serverless/
.fusebox/
.dynamodb/
.firebase/
.tern-port
.vscode-test

# Vite logs
vite.config.js.timestamp-*
vite.config.ts.timestamp-*

# Python (repo root)
__pycache__/
*.pyc
.venv/
venv/
build/
dist/

# App outputs anywhere
**/dat/out/
**/dat/tmp/

# dotenv
.env
.env.*
!.env.example

# OS/editor junk
.DS_Store
Thumbs.db
.idea/
.vscode/

```

### Developer Guide (Windows-only).md

```md
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

```

### LICENSE

```
QiAlly Commons License v0.1 (Draft)

Personal use and businesses with ≤ $150k annual gross: free

Above threshold or multi-employee teams: paid license (subscription or per-seat)

Redistribution allowed only with license intact; no resale of code itself

Offer Enterprise Add-Ons:

Branded builds and custom manifests

SSO, audit logging, remote config

Priority SLA and onboarding

Private connectors (HoneyBook, Drive SA, Zep2Mail workflows)

Nothing in code changes for this yet; it’s policy. You can add a LICENSE later and a license.json flag in qi.yaml if you want apps to display license status in the UI.

15) Troubleshooting

Double-click script closes instantly: run from PowerShell to see the error. Usually Python not found or blocked by antivirus.

Venv fails to create: ensure py launcher exists (py --version). If not, install Python 3.11 from python.org and re-run.

No popup in QiMini: PySimpleGUI import failed. Check dat/out/result.json for success; then run install-win.bat.

Exporter shows empty: ensure the repo has files beyond ignored dirs, and you ran in the correct folder.

16) Roadmap hooks (already accounted for)

Cockpit handshake via core/hook.py

Stable entrypoints: boot() in main.py, go() in core/run.py

Flat structure: core, ast, dat

React/Vite/Tauri/Electron templates will follow with the same Danger Zone contract and Windows run scripts

Supabase/OpenAI/Gemini/Cloudflare/etc. env slots reserved in .env.example
```

### QiVault/apps/README.md

```md
# QiVault Apps

Drop Qi apps here. Each app must include:
- `qi.yaml`  (declares id, name, entry, outputs)
- `main.py`  (exposes `boot(args)` and runs `core.run.go`)
- `core/hook.py` (returns Cockpit handshake dict)

Contract:
- Keep `core`, `ast`, `dat` folder names.
- Outputs default to `./dat/out`.
- Don’t rename Danger Zone files without updating the Cockpit.

```

### QiVault/qieos/.env.example

```
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

### QiVault/qieos/.gitignore

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Dependency directories
node_modules/
jspm_packages/
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional caches
.npm
.eslintcache
.stylelintcache

# REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn v3
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/sdks
!.yarn/versions

# Frontend frameworks output
.next
.nuxt
dist
out
.cache
.parcel-cache
.vuepress/dist
.temp
.svelte-kit/
**/.vitepress/dist
**/.vitepress/cache
.docusaurus

# Serverless & misc
.serverless/
.fusebox/
.dynamodb/
.firebase/
.tern-port
.vscode-test

# Vite logs
vite.config.js.timestamp-*
vite.config.ts.timestamp-*

# Python (repo root)
__pycache__/
*.pyc
.venv/
venv/
build/
dist/

# App outputs anywhere
**/dat/out/
**/dat/tmp/

# dotenv
.env
.env.*
!.env.example

# OS/editor junk
.DS_Store
Thumbs.db
.idea/
.vscode/

```

### QiVault/qieos/.obsidianignore

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

### QiVault/qieos/ai.rules

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

### QiVault/qieos/ast/smpl/sample.txt

```
Qi sample input file.

```

### QiVault/qieos/ast/tpl/base.html

```html
<!doctype html><meta charset="utf-8"><title>Qi Base</title>
<link rel="icon" href="../ico/qi.svg">
<style>body{font-family:Roboto,Arial; padding:24px}</style>
<h1>Qi Base Template</h1>
<p>Replace me.</p>

```

### QiVault/qieos/core/hook.py

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

### QiVault/qieos/core/run.py

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

### QiVault/qieos/core/ui.py

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

### QiVault/qieos/core/util.py

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

### QiVault/qieos/dat/in/.keep

```

```

### QiVault/qieos/dat/out/.keep

```

```

### QiVault/qieos/dat/tmp/.keep

```

```

### QiVault/qieos/install-win.bat

```bat
@echo off
py -3 -m venv .venv
call .venv\Scripts\pip install -r requirements.txt
echo [Qi] Installed.
pause

```

### QiVault/qieos/main.py

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

### QiVault/qieos/qi.yaml

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

### QiVault/qieos/readme.md

```md
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
Structure
core/ logic (run.py, ui.py, hook.py, util.py)

ast/ assets (ico, tpl, smpl)

dat/ in/out/tmp working dirs

## 3) Add missing icons so your HTML link isn’t broken

### Create `QiVault/qieos/ast/ico/qi.svg`
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#2c38ff"/>
      <stop offset="1" stop-color="#7a1bff"/>
    </linearGradient>
  </defs>
  <circle cx="32" cy="32" r="30" fill="url(#g)"/>
  <text x="32" y="39" font-size="28" text-anchor="middle" fill="#fff" font-family="Arial, sans-serif">Qi</text>
</svg>
Create QiVault/qimini/ast/ico/qi.svg (same file is fine)
xml
Copy code

Your existing ast/tpl/base.html in both apps already points to ../ico/qi.svg, so once these files exist, favicons resolve.
```

### QiVault/qieos/requirements.txt

```
PySimpleGUI>=5.0.0
python-dotenv>=1.0.1
PyYAML>=6.0.2
rich>=13.7.1
```

### QiVault/qieos/run-win.bat

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

### QiVault/qimini/.gitignore

```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Dependency directories
node_modules/
jspm_packages/
web_modules/

# TypeScript cache
*.tsbuildinfo

# Optional caches
.npm
.eslintcache
.stylelintcache

# REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn v3
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/sdks
!.yarn/versions

# Frontend frameworks output
.next
.nuxt
dist
out
.cache
.parcel-cache
.vuepress/dist
.temp
.svelte-kit/
**/.vitepress/dist
**/.vitepress/cache
.docusaurus

# Serverless & misc
.serverless/
.fusebox/
.dynamodb/
.firebase/
.tern-port
.vscode-test

# Vite logs
vite.config.js.timestamp-*
vite.config.ts.timestamp-*

# Python (repo root)
__pycache__/
*.pyc
.venv/
venv/
build/
dist/

# App outputs anywhere
**/dat/out/
**/dat/tmp/

# dotenv
.env
.env.*
!.env.example

# OS/editor junk
.DS_Store
Thumbs.db
.idea/
.vscode/

```

### QiVault/qimini/.obsidianignore

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

### QiVault/qimini/ai.rules

```
# QiMini Rules (Windows)
1) Keep core, ast, dat folder names.
2) Expose boot() in main.py and go() in core/run.py.
3) qi.yaml must exist and match entry main.py.
4) Default writes to ./dat/out.
5) Do not remove core/hook.py if Cockpit discovery is required.
6) No secrets in git (.env, service-account.json ignored).

```

### QiVault/qimini/ast/smpl/sample.txt

```
QiMini sample input file.

```

### QiVault/qimini/ast/tpl/base.html

```html
<!doctype html><meta charset="utf-8"><title>Qi Base</title>
<link rel="icon" href="../ico/qi.svg">
<style>body{font-family:Roboto,Arial; padding:24px}</style>
<h1>Qi Base Template</h1>
<p>Replace me.</p>

```

### QiVault/qimini/core/hook.py

```python
def hook(meta):
    return {
        "id": meta["app"]["id"],
        "name": meta["app"]["name"],
        "entry": meta["app"]["entry"],
        "ver": meta["app"]["ver"],
        "out": meta["app"]["out"],
        "mode": meta["app"]["mode"],
    }

```

### QiVault/qimini/core/run.py

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

### QiVault/qimini/core/ui.py

```python
import argparse, json
from .run import go
from pathlib import Path
import yaml

def parse():
    p = argparse.ArgumentParser(prog="qimini", description="QiMini CLI")
    p.add_argument("--in", dest="in_", help="input path", default=None)
    p.add_argument("--out", dest="out", help="output dir override", default=None)
    return p.parse_args()

def _load_cfg():
    here = Path(__file__).resolve().parent.parent
    return yaml.safe_load((here / "qi.yaml").read_text(encoding="utf-8"))

def main():
    args = parse()
    cfg = _load_cfg()
    if args.out:
        cfg["paths"]["base_out"] = args.out
    res = go({"in": args.in_} if args.in_ else {}, cfg)
    print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

```

### QiVault/qimini/dat/in/.keep

```

```

### QiVault/qimini/dat/out/.keep

```

```

### QiVault/qimini/dat/tmp/.keep

```

```

### QiVault/qimini/install-win.bat

```bat
@echo off
py -3 -m venv .venv
call .venv\Scripts\pip install -r requirements.txt
echo [QiMini] Installed.
pause

```

### QiVault/qimini/main.py

```python
from core.run import go
import json, sys, yaml, pathlib

def boot(args=None):
    here = pathlib.Path(__file__).parent
    cfg = yaml.safe_load((here / "qi.yaml").read_text(encoding="utf-8"))
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

### QiVault/qimini/qi.yaml

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

### QiVault/qimini/requirements.txt

```
PySimpleGUI>=5.0.0
python-dotenv>=1.0.1
PyYAML>=6.0.2
rich>=13.7.1

```

### QiVault/qimini/run-win.bat

```bat
@echo off
setlocal
IF NOT EXIST .venv (
  echo [QiMini] Creating venv...
  py -3 -m venv .venv
  call .venv\Scripts\pip install -r requirements.txt
)
call .venv\Scripts\python main.py
pause

```

### README.md

```md
# QiApp-EOS
Bootstrap template for QiVerse QiMinis Apps/applets and tools to be used with QiCockpit

```

### qi_code_extract.py

```python
#!/usr/bin/env python3
"""
Qi Code Extractor (Markdown)
- Makes a single .md you can share with me (or a judge, or your future self).
- Tree at top, then headers and contents per file.
- Skips libraries/build junk by default.

Usage:
  python qi_code_extract.py                # export from current folder
  python qi_code_extract.py --root D:\work --out D:\out\bundle.md
  python qi_code_extract.py --max-bytes 300000
"""

from __future__ import annotations
import argparse
import os
from pathlib import Path
from typing import Iterable

# ---------------------------
# Ignore rules (tight + sane)
# ---------------------------
IGNORE_DIRS = {
    ".git", ".obsidian", ".idea", ".vscode",
    "node_modules", ".npm", ".pnpm-store",
    "__pycache__", "venv", ".venv",
    "dist", "build", ".ruff_cache", ".mypy_cache",
    "dat/out", "dat/tmp", "ast/ico",
}
IGNORE_FILES = {
    ".env", ".env.local", ".DS_Store", "Thumbs.db",
    "pnpm-lock.yaml", "package-lock.json"
}
# Optional: skip common big/binary types by extension
BINARY_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svgz",
    ".pdf", ".zip", ".gz", ".7z", ".rar", ".exe", ".dll", ".so",
    ".ttf", ".otf", ".woff", ".woff2", ".mp4", ".mov", ".avi",
    ".mp3", ".wav", ".ogg", ".wasm", ".svg", ".ico",
}

# Map extension -> code fence hint
LANG_MAP = {
    ".py": "python",
    ".ps1": "powershell",
    ".cmd": "bat", ".bat": "bat",
    ".sh": "bash",
    ".js": "javascript", ".cjs": "javascript", ".mjs": "javascript",
    ".ts": "ts",
    ".tsx": "tsx", ".jsx": "jsx",
    ".json": "json", ".jsonc": "json",
    ".yml": "yaml", ".yaml": "yaml",
    ".toml": "toml",
    ".ini": "ini", ".cfg": "ini", ".conf": "ini",
    ".html": "html", ".htm": "html",
    ".css": "css",
    ".md": "md",
    ".sql": "sql",
    ".rs": "rust",
    ".go": "go",
    ".java": "java",
    ".cs": "csharp",
    ".cpp": "cpp", ".cc": "cpp", ".cxx": "cpp", ".h": "cpp", ".hpp": "cpp",
}

def is_ignored(path: Path, root: Path) -> bool:
    """Skip if path lies within any ignored directory or is an ignored filename."""
    # normalize relative parts for matching
    rel = path.relative_to(root)
    parts = [p.replace("\\", "/") for p in rel.parts]

    # dir checks: if any prefix path equals an ignore dir
    for i in range(1, len(parts) + 1):
        sub = "/".join(parts[:i])
        # match either exact dir name or normalized 'dir/subdir' patterns we listed (e.g., dat/out)
        if sub in IGNORE_DIRS:
            return True
        # also match just the leaf folder name
        if i == len(parts) and rel.is_dir() and parts[-1] in IGNORE_DIRS:
            return True

    # file name checks
    if rel.name in IGNORE_FILES:
        return True

    return False

def is_probably_text(p: Path, max_bytes: int) -> bool:
    """Heuristic: skip binary or huge files."""
    if p.suffix.lower() in BINARY_EXTS:
        return False
    try:
        size = p.stat().st_size
        if size > max_bytes:
            return False
    except OSError:
        return False
    try:
        with p.open("rb") as f:
            chunk = f.read(4096)
        # binary null heuristic
        if b"\x00" in chunk:
            return False
        # try utf-8 decode
        chunk.decode("utf-8")
        return True
    except Exception:
        return False

def build_tree(root: Path, files: Iterable[Path]) -> str:
    """Make a pretty tree of included files only."""
    # gather dirs that contain included files
    dirs = set()
    for f in files:
        d = f.parent
        while d != root and root in d.parents:
            dirs.add(d)
            d = d.parent
    lines = [f"# Code Export — {root.resolve()}",
             "",
             "## Directory Tree",
             "```text"]
    # print tree
    # root line
    lines.append(root.name + "/")
    # collect all display paths
    to_show = sorted(list(dirs) + list(files))
    # build indent map
    for p in to_show:
        rel = p.relative_to(root)
        depth = len(rel.parts)
        indent = "│   " * (depth - 1)
        name = rel.name + ("/" if p.is_dir() else "")
        bullet = "└── " if depth > 0 else ""
        if p.is_dir():
            lines.append(f"{indent}{('└── ' if depth>0 else '')}{name}")
        else:
            lines.append(f"{indent}{('└── ' if depth>0 else '')}{name}")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)

def fence_lang(path: Path) -> str:
    return LANG_MAP.get(path.suffix.lower(), "")

def collect_files(root: Path, max_bytes: int) -> list[Path]:
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            if is_ignored(p, root):
                # skip whole subtree
                # optimization: if ignored dir, don't descend (rglob still will; we filter anyway)
                continue
            else:
                continue
        # files
        if is_ignored(p, root):
            continue
        if not is_probably_text(p, max_bytes):
            continue
        files.append(p)
    return files

def write_markdown(root: Path, out_path: Path, files: list[Path]) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    parts = [build_tree(root, files)]
    parts.append("---")
    parts.append("## Files")
    parts.append("")
    for f in files:
        rel = f.relative_to(root).as_posix()
        lang = fence_lang(f)
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            # last-ditch: latin-1; if it fails, skip
            try:
                text = f.read_text(encoding="latin-1")
            except Exception:
                continue
        parts.append(f"### {rel}")
        parts.append("")
        parts.append(f"```{lang}".rstrip())
        parts.append(text)
        parts.append("```")
        parts.append("")
    out_path.write_text("\n".join(parts), encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Qi Code Extractor → Markdown bundle")
    parser.add_argument("--root", default=".", help="Root directory to export (default: .)")
    parser.add_argument("--out", default=None, help="Output .md path (default: dat/out/code_export.md if exists, else ./code_export.md)")
    parser.add_argument("--max-bytes", type=int, default=200_000, help="Skip files larger than this (default: 200kB)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"[Qi] Root not found: {root}")

    # default out placement
    if args.out:
        out_path = Path(args.out)
    else:
        dat_out = root / "dat" / "out"
        out_path = dat_out / "code_export.md" if dat_out.exists() else root / "code_export.md"

    files = collect_files(root, args.max_bytes)
    write_markdown(root, out_path, files)
    print(f"[Qi] Exported {len(files)} files → {out_path}")

if __name__ == "__main__":
    main()

```
