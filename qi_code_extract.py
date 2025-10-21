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
