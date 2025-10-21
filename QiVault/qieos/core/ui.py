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
