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
