"""
batch_ingest.py -- run ingest.py over many raw sections.

Skips sections already recorded in wiki/log.md, so it is resumable and safe to re-run:
drop new raw files into raw/ai-engineering/ and run again -- only the new ones ingest.
That is the "drop a source in and it runs itself" path.

Usage:
    uv run batch_ingest.py --chapter 1     # just chapter 1
    uv run batch_ingest.py --list          # show what WOULD run, do nothing
    uv run batch_ingest.py                 # everything not yet done
"""
from __future__ import annotations
import argparse, subprocess, sys, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw" / "ai-engineering"
LOG = ROOT / "wiki" / "log.md"
EXEMPLARS = ["concepts/model-distillation.md", "entities/distilbert.md"]


def done_stems() -> set[str]:
    if not LOG.exists():
        return set()
    stems = set()
    for line in LOG.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\bingest\s+(\S+)", line)
        if m:
            stems.add(m.group(1))
    return stems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, help="only this chapter, e.g. 1")
    ap.add_argument("--list", action="store_true", help="show what would run, do nothing")
    args = ap.parse_args()

    pattern = f"ch{args.chapter:02d}-*.txt" if args.chapter else "*.txt"
    files = sorted(RAW.glob(pattern))
    if not files:
        sys.exit(f"No raw files match {pattern} in {RAW}")

    done = done_stems()
    todo = [f for f in files if f.stem not in done]
    print(f"{len(files)} matched | {len(files) - len(todo)} already done | {len(todo)} to ingest")

    if args.list or not todo:
        for f in todo:
            print("  would ingest:", f.name)
        return

    ok, fail = [], []
    for i, f in enumerate(todo, 1):
        print(f"\n[{i}/{len(todo)}] {f.name}")
        cmd = [sys.executable, "ingest.py", str(f.relative_to(ROOT)), "--exemplars", *EXEMPLARS]
        if subprocess.run(cmd).returncode == 0:
            ok.append(f.name)
        else:
            fail.append(f.name)

    print(f"\nDone. {len(ok)} ok, {len(fail)} failed.")
    for f in fail:
        print("  FAILED:", f)


if __name__ == "__main__":
    main()
