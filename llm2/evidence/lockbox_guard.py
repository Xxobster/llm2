"""Fail-closed seal for the forward research lockbox.

Any script that would evaluate or Finplot bars on/after ``FORWARD_LOCKBOX_START``
must opt in explicitly. Silent peeks are refused; authorized peeks append the
peek log and stamp ``LOCKBOX_OPENED_CONTAMINATED``.

Copying databases does not reseal the calendar (see ``refuse_copy_as_pristine_holdout``).
Outer-fold settle (bars strictly before the lockbox) never needs this gate.
"""

from __future__ import annotations

import os
from typing import Any, Iterable, Sequence

from llm2.evidence.peek_log import append_peek, default_peek_log_path
from llm2.paths import FORWARD_LOCKBOX_START
from llm2.research_policy import PolicyError

# CLI flags / env names (exact strings so greps stay unambiguous)
CLI_ACCEPT_CONTAMINATE = "--i-accept-lockbox-contamination"
CLI_ACCEPT_FINPLOT = "--i-accept-finplot-lockbox"
ENV_ACCEPT_CONTAMINATE = "LLM2_I_ACCEPT_LOCKBOX_CONTAMINATION"
ENV_ACCEPT_FINPLOT = "LLM2_I_ACCEPT_FINPLOT_LOCKBOX"

__all__ = [
    "CLI_ACCEPT_CONTAMINATE",
    "CLI_ACCEPT_FINPLOT",
    "ENV_ACCEPT_CONTAMINATE",
    "ENV_ACCEPT_FINPLOT",
    "window_includes_forward_lockbox",
    "env_accepts_lockbox_contamination",
    "env_accepts_finplot_lockbox",
    "add_lockbox_guard_args",
    "require_lockbox_access",
    "seal_finplot_unless_authorized",
]


def window_includes_forward_lockbox(
    window_start: str,
    window_end: str | None = None,
) -> bool:
    """True if the evaluation window can contain bars on/after the lockbox start."""
    import pandas as pd

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    w0 = pd.Timestamp(window_start, tz="UTC")
    if w0 >= lock:
        return True
    if window_end is None or str(window_end).strip() in {"", "unknown", "None"}:
        return False
    try:
        w1 = pd.Timestamp(window_end, tz="UTC")
    except (TypeError, ValueError):
        return False
    # Half-open overlap with [lock, +inf)
    return w1 > lock


def env_accepts_lockbox_contamination() -> bool:
    v = (os.environ.get(ENV_ACCEPT_CONTAMINATE) or "").strip().lower()
    return v in {"1", "true", "yes", "i_accept"}


def env_accepts_finplot_lockbox() -> bool:
    v = (os.environ.get(ENV_ACCEPT_FINPLOT) or "").strip().lower()
    return v in {"1", "true", "yes", "i_accept"}


def add_lockbox_guard_args(parser: Any) -> None:
    """Attach dual opt-in flags used by Finplot / lockbox hunt scripts."""
    parser.add_argument(
        CLI_ACCEPT_CONTAMINATE,
        action="store_true",
        dest="i_accept_lockbox_contamination",
        help=(
            "REQUIRED to evaluate bars on/after FORWARD_LOCKBOX_START. "
            "Records LOCKBOX_OPENED_CONTAMINATED in the peek log. Prefer outer-fold settle."
        ),
    )
    parser.add_argument(
        CLI_ACCEPT_FINPLOT,
        action="store_true",
        dest="i_accept_finplot_lockbox",
        help=(
            "REQUIRED together with contamination accept to open Finplot/interactive charts "
            "on the forward lockbox. Default is report-only (no chart)."
        ),
    )


def seal_finplot_unless_authorized(*, open_finplot: bool, accepted_finplot: bool) -> bool:
    """Return whether Finplot may open; force TRADESIM_NO_PLOT when sealed."""
    if open_finplot and accepted_finplot:
        os.environ.pop("TRADESIM_NO_PLOT", None)
        return True
    os.environ["TRADESIM_NO_PLOT"] = "1"
    return False


def require_lockbox_access(
    *,
    experiment_id: str,
    window_start: str,
    purpose: str,
    window_end: str | None = None,
    symbols: Sequence[str] | None = None,
    arms: str | Iterable[Any] | None = None,
    n_arms: int | None = None,
    accepted_contamination: bool = False,
    open_finplot: bool = False,
    accepted_finplot: bool = False,
    notes: str = "",
    path: Any = None,
    allow_env: bool = True,
) -> dict[str, Any] | None:
    """Refuse silent lockbox peeks; authorize only with explicit accept + peek log.

    Returns the peek record when access was needed and granted, else ``None`` when
    the window does not touch the forward lockbox (no contamination risk).
    """
    if not window_includes_forward_lockbox(window_start, window_end):
        return None

    accepted = bool(accepted_contamination)
    finplot_ok = bool(accepted_finplot)
    if allow_env:
        accepted = accepted or env_accepts_lockbox_contamination()
        finplot_ok = finplot_ok or env_accepts_finplot_lockbox()

    if not accepted:
        raise PolicyError(
            f"Forward lockbox sealed (bars on/after {FORWARD_LOCKBOX_START}). "
            f"Refusing experiment_id={experiment_id!r} purpose={purpose!r}. "
            f"Pass {CLI_ACCEPT_CONTAMINATE} (or {ENV_ACCEPT_CONTAMINATE}=1 for batch) "
            "only when you intentionally contaminate this holdout; prefer outer-fold "
            "settle for quotable evidence. Finplot defaults to off."
        )

    if open_finplot and not finplot_ok:
        raise PolicyError(
            f"Finplot / interactive chart on the forward lockbox is sealed. "
            f"Pass BOTH {CLI_ACCEPT_CONTAMINATE} AND {CLI_ACCEPT_FINPLOT} "
            f"(or {ENV_ACCEPT_FINPLOT}=1). Prefer --no-show / TRADESIM_NO_PLOT report-only."
        )

    seal_finplot_unless_authorized(open_finplot=open_finplot, accepted_finplot=finplot_ok)

    sym_note = ""
    if symbols:
        sym_note = "symbols=" + ",".join(str(s).upper() for s in symbols)
    peek_notes = " | ".join(
        x for x in (notes, sym_note, f"finplot={'yes' if open_finplot and finplot_ok else 'no'}") if x
    )
    record = append_peek(
        experiment_id=experiment_id,
        window_start=str(window_start),
        window_end=str(window_end or "open_ended"),
        purpose=purpose,
        arms=arms if arms is not None else (list(symbols) if symbols else None),
        n_arms=n_arms if n_arms is not None else (len(symbols) if symbols else None),
        evidence_class="LOCKBOX_OPENED_CONTAMINATED",
        notes=peek_notes,
        path=path or default_peek_log_path(),
        extra={
            "gate": "require_lockbox_access",
            "open_finplot": bool(open_finplot and finplot_ok),
            "symbols": list(symbols) if symbols else None,
        },
    )
    return record
