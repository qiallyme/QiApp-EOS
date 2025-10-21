# QiVault Apps

Drop Qi apps here. Each app must include:
- `qi.yaml`  (declares id, name, entry, outputs)
- `main.py`  (exposes `boot(args)` and runs `core.run.go`)
- `core/hook.py` (returns Cockpit handshake dict)

Contract:
- Keep `core`, `ast`, `dat` folder names.
- Outputs default to `./dat/out`.
- Don’t rename Danger Zone files without updating the Cockpit.
