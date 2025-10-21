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
