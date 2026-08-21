"""Tiny policy helpers for contamination tracks that must never promote."""

from __future__ import annotations

import os
import sys


def refuse_orange_pnl_optimization(*, argv: list[str] | None = None, context: str) -> None:
    """Abort orange / oracle_leaky Profit and Loss (P&L) optimization unless forensics allowlisted.

    Set environment ``LLM2_ALLOW_ORANGE_FORENSICS=1`` *and* pass
    ``--i-accept-contamination-forensics`` only when intentionally rebuilding
    forensic residual diagnostics — never for pack freeze or live.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    allow_env = os.environ.get("LLM2_ALLOW_ORANGE_FORENSICS", "").strip() in {"1", "true", "TRUE", "yes"}
    allow_flag = "--i-accept-contamination-forensics" in args
    if allow_env and allow_flag:
        print(
            f"[ORANGE_FORENSICS] allowed once for diagnostics only — {context}. "
            "Promotion and pack freeze remain FORBIDDEN.",
            flush=True,
        )
        return
    print(
        "REFUSED: orange / oracle_leaky Profit-and-Loss (P&L) optimization is sealed (D-058).\n"
        f"  context: {context}\n"
        "  oracle_leaky = contamination forensics only; pred_leaky packs must not freeze.\n"
        "  Research budget is structure_v1_no_retrace / true-cyan causal alphas.\n"
        "  Residual-only rebuild requires BOTH:\n"
        "    LLM2_ALLOW_ORANGE_FORENSICS=1\n"
        "    --i-accept-contamination-forensics\n",
        file=sys.stderr,
        flush=True,
    )
    raise SystemExit(3)
