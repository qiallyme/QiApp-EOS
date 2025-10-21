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
