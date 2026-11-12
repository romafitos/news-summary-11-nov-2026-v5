"""news-summary-01 entry, v5 (Python 3.13, stdlib only).

Copies the summary in summary.txt beside this file to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
This file never edits the summary; it only copies it and checks
the copy matches, so the output is deterministic.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SRC = HERE / "summary.txt"
OUT.mkdir(parents=True, exist_ok=True)
if SRC.stat().st_size == 0:
    raise SystemExit("summary.txt is empty")
dest = OUT / "entry.txt"
shutil.copyfile(SRC, dest)
if dest.stat().st_size != SRC.stat().st_size:
    raise SystemExit("entry copy size mismatch")
if dest.read_bytes() != SRC.read_bytes():
    raise SystemExit("entry copy differs from summary")
