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