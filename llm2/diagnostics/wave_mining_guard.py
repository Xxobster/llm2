"""Machine-enforceable guard: no wave-mining module may touch the analytic (non-causal) wave.

``llm2.diagnostics.wave`` produces two waves on purpose and says so loudly: ``causal_wave``
is the only one that may ever become a feature, trigger or signal, and ``analytic_wave`` is
zero-phase, whole-series, and exists for charts and descriptive summaries only. That
separation is easy to state and easy to violate by accident — a stray
``from llm2.diagnostics.wave import analytic_wave`` at the top of a mining module would
compile, run, and quietly hand every metric a look into the future.

This module is the machine-enforceable version of that rule for the five modules that mine
the wave for tradeable structure (metrics, motifs, events, cross-series panel, structure
breaks). Two checks, both cheap and both meant to be called unconditionally:

``forbid_analytic_import``
    Call once, at import time, with ``globals()``. Raises immediately if the module being
    loaded has ``analytic_wave`` bound in its namespace — whether via a direct import, a
    ``from ... import *``, or a re-export.

``assert_causal_mining_caller``
    A stack-walk, defense-in-depth check for code that reaches ``analytic_wave`` dynamically
    (``getattr``, a callback, an inherited helper) rather than through a static import that
    ``forbid_analytic_import`` can see. It raises if any frame belonging to a mining module
    has a live reference to ``analytic_wave`` in scope, or if a mining-module frame appears
    anywhere in the call chain above a live call to ``analytic_wave`` itself.
"""

from __future__ import annotations

import inspect

# Full module names, so a rename or a copy-paste into a new file cannot silently escape the
# guard the way a bare basename match could.
MINING_MODULES: frozenset[str] = frozenset(
    {
        "llm2.diagnostics.wavemetrics",
        "llm2.diagnostics.wavemotif",
        "llm2.diagnostics.waveevent",
        "llm2.diagnostics.wavepanel",
        "llm2.diagnostics.structurebreak",
    }
)


class NonCausalWaveError(RuntimeError):
    """A wave-mining module imported, referenced, or called the non-causal analytic wave."""


def forbid_analytic_import(module_globals: dict) -> None:
    """Refuse to finish loading a mining module that has ``analytic_wave`` in its namespace.

    Call this at the top of every module in :data:`MINING_MODULES`, immediately after the
    import block, with ``globals()`` from that module::

        from llm2.diagnostics.wave_mining_guard import forbid_analytic_import
        forbid_analytic_import(globals())

    A later definition of a *local* name called ``analytic_wave`` (there is no reason one
    would exist) would also trip this, which is the conservative and correct side to err on.
    """
    name = module_globals.get("__name__", "<unknown module>")
    if "analytic_wave" in module_globals:
        raise NonCausalWaveError(
            f"{name} has 'analytic_wave' bound in its module namespace. The analytic wave "
            "is zero-phase and whole-series (non-causal) and is display-only by design — "
            "see llm2.diagnostics.wave module docstring. A mining module may build metrics, "
            "triggers or targets from causal_wave only. Remove the import."
        )


def assert_causal_mining_caller() -> None:
    """Stack-walk guard for dynamic access to the analytic wave from a mining module.

    Two independent checks, either one sufficient to raise:

    1. Any frame whose module is in :data:`MINING_MODULES` has ``analytic_wave`` bound in
       its globals or locals (e.g. imported lazily inside a function body).
    2. A frame executing inside ``analytic_wave`` itself (by function name, since it can be
       called via ``wave.analytic_wave`` without a local binding) has a mining-module frame
       anywhere above it in the call chain.

    Intended to be called from any dynamic dispatch point in the mining modules (a plugin
    registry, a callback table) where a static import-time check cannot see the eventual
    target. Cheap enough to call on every dispatch: the stack is typically a handful of
    frames deep in this codebase.
    """
    frames = inspect.stack()
    try:
        for frame_info in frames:
            mod_name = frame_info.frame.f_globals.get("__name__", "")
            if mod_name not in MINING_MODULES:
                continue
            if "analytic_wave" in frame_info.frame.f_globals or "analytic_wave" in frame_info.frame.f_locals:
                raise NonCausalWaveError(
                    f"{mod_name} has a live reference to analytic_wave in scope while a "
                    "mining function is executing. Mining modules may only use causal_wave."
                )

        for i, frame_info in enumerate(frames):
            if frame_info.function != "analytic_wave":
                continue
            for caller in frames[i + 1 :]:
                caller_mod = caller.frame.f_globals.get("__name__", "")
                if caller_mod in MINING_MODULES:
                    raise NonCausalWaveError(
                        f"{caller_mod} called analytic_wave (non-causal, display-only), "
                        "directly or via an intermediate frame. Mining modules may only "
                        "use causal_wave."
                    )
    finally:
        # Frame objects hold references that would otherwise leak past this function.
        del frames
