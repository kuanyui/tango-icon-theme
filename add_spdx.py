#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys
from typing import List, Sequence

SPDX_LINE: str = "<!-- SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only -->"
HEAD_SCAN_BYTES: int = 1024


def run_git(args: Sequence[str]) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip())
    return r.stdout


def get_modified_svg_file_paths() -> List[Path]:
    """Files that are staged (cached) but not yet committed."""
    # output: str = run_git(["diff", "--name-only", "HEAD^", "HEAD"])  # modified files in previous commit
    output: str = run_git([ "diff", "--cached", "--name-only", "--diff-filter=ACM" ])   # staged (cached) but not commited yet file.
    return [
        Path(p) for p in output.splitlines()
        if p.lower().endswith(".svg") and Path(p).is_file()
    ]


def has_spdx_in_file_header(file_path: Path) -> bool:
    with file_path.open("rb") as f:
        return b"SPDX-License-Identifier:" in f.read(HEAD_SCAN_BYTES)


def insert_spdx_header_to_file(file_path: Path) -> None:
    ori_svg: str = file_path.read_text(encoding="utf-8", errors="ignore")
    new_svg: str
    if ori_svg.lstrip().startswith("<?xml"):
        idx: int = ori_svg.find("?>")
        if idx != -1:
            idx += 2
            seg0 = ori_svg[:idx]
            seg1 = ori_svg[idx:]
            # NOTE: Inkscape seems always add extra new line after SPDX line...
            # if seg1.startswith('\n'):
            #     seg1 = seg1[1:]
            new_svg = seg0 + "\n" + SPDX_LINE + "\n" + seg1
        else:
            new_svg = SPDX_LINE + ori_svg
    else:
        new_svg = SPDX_LINE + ori_svg
    file_path.write_text(new_svg, encoding="utf-8")


def main() -> int:
    to_apply = "--apply" in sys.argv
    files: List[Path] = get_modified_svg_file_paths()
    if not files:
        return 0
    files_without_spdx: List[Path] = []
    for f in files:
        if has_spdx_in_file_header(f):
            continue
        files_without_spdx.append(f)
        if to_apply:
            print(f"[LOG] Add SPDX to {f}")
            insert_spdx_header_to_file(f)
        else:
            print(f"[WARN] {f} missing SPDX.")
    if to_apply:
        return 0
    else:
        if files_without_spdx:
            print(f"[WARN] Some modified SVG files have no SPDX comment. Please run `./add_spdx.py --apply`")
            return -1
        return 0


if __name__ == "__main__":
    sys.exit(main())
