#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys
from typing import List, Sequence

SPDX_LINE: str = "<!-- SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only -->\n"
HEAD_SCAN_BYTES: int = 1024


def run_git(args: Sequence[str]) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip())
    return r.stdout


def get_modified_svg_file_paths() -> List[Path]:
    output: str = run_git(["diff", "--name-only", "HEAD^", "HEAD"])
    return [
        Path(p) for p in output.splitlines()
        if p.lower().endswith(".svg") and Path(p).is_file()
    ]


def has_spdx_at_top(file_path: Path) -> bool:
    with file_path.open("rb") as f:
        return b"SPDX-License-Identifier:" in f.read(HEAD_SCAN_BYTES)


def insert_spdx(file_path: Path) -> None:
    ori_svg: str = file_path.read_text(encoding="utf-8", errors="ignore")
    new_svg: str
    if ori_svg.lstrip().startswith("<?xml"):
        idx: int = ori_svg.find("?>")
        if idx != -1:
            idx += 2
            seg0 = ori_svg[:idx]
            seg1 = ori_svg[idx:]
            if seg1.startswith('\n'):
                seg1 = seg1[1:]
            new_svg = seg0 + "\n" + SPDX_LINE + seg1
        else:
            new_svg = SPDX_LINE + ori_svg
    else:
        new_svg = SPDX_LINE + ori_svg

    file_path.write_text(new_svg, encoding="utf-8")


def main() -> int:
    files: List[Path] = get_modified_svg_file_paths()
    if not files:
        print("No modified SVG files in the latest git commit. Skip.")
        return 0

    for f in files:
        if has_spdx_at_top(f):
            print(f"{f} Already contains SPDX. Skip.")
            continue
        else:
            print(f"Adding SPDX to {f}")
            insert_spdx(f)

    return 0


if __name__ == "__main__":
    sys.exit(main())