"""
run_eval.py -- run the 20-question eval set against the frozen wiki.

Emits a markdown run file in the SAME format as the Project 1 RAG eval runs, so the
unmodified rag-book judge.py can score it without changes:

    ## Q<n> <question>
    **A:** <answer>
    **Retrieved:** <routed pages> | hop: <hopped pages>
    ---

Parity notes:
  - Same 20 questions, same judge, same book corpus as the RAG baseline.
  - The wiki is FROZEN; this script never writes to wiki/.
  - Build-blind holds: ingest never saw these questions.

Usage:
    uv run run_eval.py                      # wiki with 1-hop link following
    uv run run_eval.py --no-hop             # ablation: routing only, no link following
    uv run run_eval.py --out myrun.md       # custom output path
    uv run run_eval.py --limit 3            # smoke test on the first 3 questions
"""
from __future__ import annotations
import argparse, datetime, sys, time
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from eval_set import EVAL_SET          # noqa: E402  (copied from rag-book)
import query as Q                      # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-hop", action="store_true", help="ablation: no Related-link following")
    ap.add_argument("--out", default=None, help="output markdown path")
    ap.add_argument("--limit", type=int, default=None, help="only the first N questions")
    ap.add_argument("--max-pages", type=int, default=Q.MAX_PAGES,
                    help="cap on routed pages (3 = RAG-comparable budget)")
    ap.add_argument("--bm25", action="store_true", help="union router picks with BM25 top-k")
    ap.add_argument("--bm25-k", type=int, default=Q.BM25_K)
    args = ap.parse_args()

    hop = not args.no_hop
    out = Path(args.out) if args.out else ROOT / (
        f"eval_run_wiki_p{args.max_pages}{'_nohop' if args.no_hop else '_hop'}"
        f"{f'_bm25k{args.bm25_k}' if args.bm25 else ''}.md")

    from anthropic import Anthropic
    load_dotenv(ROOT / ".env")
    client = Anthropic()

    items = EVAL_SET[: args.limit] if args.limit else EVAL_SET
    print(f"[{Q.VERSION} | model={Q.MODEL} | hop={hop} | max_pages={args.max_pages} | "
          f"bm25={'k=' + str(args.bm25_k) if args.bm25 else 'off'}] "
          f"{len(items)} question(s) -> {out.name}")

    lines = [
        f"# Wiki eval run ({'with' if hop else 'without'} 1-hop link following)",
        "",
        f"- date: {datetime.date.today().isoformat()}",
        f"- system: llm-wiki (frozen), {Q.VERSION}",
        f"- model: {Q.MODEL}",
        f"- link following: {'ON (1 hop)' if hop else 'OFF (routing only)'}",
        f"- max routed pages: {args.max_pages}",
        f"- bm25 union: {'ON, k=' + str(args.bm25_k) if args.bm25 else 'OFF'}",
        "",
        "---",
        "",
    ]

    t0 = time.time()
    total_ctx = []
    for i, item in enumerate(items, 1):
        qid = item.get("id", i)
        question = item["question"]
        cat = item.get("category", "")
        print(f"  [{i}/{len(items)}] Q{qid} ({cat}) ...", end="", flush=True)
        try:
            r = Q.run(client, question, hop=hop, max_pages=args.max_pages,
                      bm25=args.bm25, bm25_k=args.bm25_k)
            ans = r["answer"]
            retrieved = ", ".join(r["routed"]) or "(none)"
            hopped = ", ".join(r["hopped"]) or "(none)"
            bm = ", ".join(r.get("bm25", [])) or "(none)"
            ctx = r.get("context_chars", 0)
            total_ctx.append(ctx)
        except Exception as e:                      # keep the run going; record the failure
            ans = f"[ERROR: {e}]"
            retrieved, hopped, bm, ctx = "(error)", "(error)", "(error)", 0
        print(" done")

        lines += [
            f"## Q{qid} {question}",
            "",
            f"**Category:** {cat}",
            "",
            f"**A:** {ans}",
            "",
            f"**Retrieved:** {retrieved} | bm25: {bm} | hop: {hopped} | context_chars: {ctx}",
            "",
            "---",
            "",
        ]

    if total_ctx:
        avg = sum(total_ctx) / len(total_ctx)
        lines += ["", f"_Average context per question: {avg:,.0f} chars "
                      f"(~{avg / 4:,.0f} tokens)_", ""]
        print(f"Average context: {avg:,.0f} chars (~{avg/4:,.0f} tokens)")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {out} in {time.time() - t0:.0f}s")
    print(f"Next: copy to rag-book and judge there:\n"
          f"  Copy-Item {out.name} ..\\rag-book\\\n"
          f"  cd ..\\rag-book ; uv run score_run.py {out.name}")


if __name__ == "__main__":
    main()
