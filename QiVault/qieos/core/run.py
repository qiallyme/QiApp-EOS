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
