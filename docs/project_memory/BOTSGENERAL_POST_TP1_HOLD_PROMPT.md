# tradesim: post-TP1 residual hold extension

Implement this in `C:\projects\botsgeneral\packages\tradesim`, not in LLM2.
LLM2 must keep using the shared engine and must not create a second simulator.

## Goal

After take-profit leg index `N` fills, let the residual position use a longer
maximum hold. Prefer a `Signal.max_hold_bars_after_leg: dict[int, int] | None`,
for example `{0: 24}` after TP1.

Document whether the value is:

1. a total hold measured from original entry; or
2. a new remaining hold measured from the TP1 fill bar.

The second meaning matches the ordinary meaning of “extend the hold after TP1”
and is preferred if live parity is feasible.

## Required safeguards

1. Keep the existing shared entry-bar resolution for stop, target, break-even,
   trail and liquidation. Existing `EXEC-010` through `EXEC-020` must remain
   green.
2. Keep `BreakEvenConfig(trigger_on_leg=...)` unchanged; add hold mutation only.
3. Add a bound conformance test, for example `EXEC-021`, where TP1 fills, the
   residual would exit at the old hold, then survives under the post-leg rule
   and exits via max-hold, TP2 or break-even as specified.
4. Add an end-to-end fixture for `tp_legs + trigger_on_leg break-even +
   post-leg hold`.
5. Define the touch-bar ordering for protective-level and hold updates.
6. Reject non-executable partial legs under the existing quantity-step rules.
7. Update `TRADESIM_BACKTEST_ENGINE_GUIDE.md` and
   `STRATEGY_TO_TRADESIM_CONTRACT.md`.
8. Run `tradesim-conformance` in the botsgeneral environment and report GREEN.

Until this feature exists, LLM2 uses only a clearly labelled fixed
`max_hold_bars` measured from entry.
