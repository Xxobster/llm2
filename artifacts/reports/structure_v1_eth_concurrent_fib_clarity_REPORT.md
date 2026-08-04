# ETH concurrent Fibonacci + clarity grid (lockbox diagnostic)

**Evidence class:** `LOCKBOX_OPENED_CONTAMINATED` — May 2026 → 2026-08-02 07:00:00+00:00.
Not a promotion gate. Max earned readiness remains **LIVE_STOP / RESEARCH_ONLY** for scale.

## Anchors (same costs/engine)

| Arm | Trades | Net PnL | Profit factor |
|---|---:|---:|---:|
| One-way single | 345 | 17.11 | 2.101 |
| Hedge×3 uniform TP1%/hold6 | 1072 | 58.05 | 2.367 |

## Grid (168 arms)

- Clarity: none, mean_strength, range_chop, favor_confirm
- Book 3+ absolute TP: [0.233, 0.377, 0.618] (let-it-run)
- Book 3+ holds: [12, 18] bars
- Max per side K: [3, 4, 5, 6, 7, 8, 9]
- Arms beating hedge×3 on **both** net PnL and PF: **81**
- Arms with entry-bar exit rate > 25%: **0**

### Key finding: absolute Fibonacci TPs do not bite

For fixed clarity/hold/K, results for TP **0.233 / 0.377 / 0.618** are **identical**.
On 1h ETH over 12–18 bars a +23.3% (or larger) target almost never prints,
so book 3+ exits on **max-hold** (or SL). The lever that moves the needle is
**concurrency K** and **hold length**, not the fib number itself.

### Best arms

| Rank | Label | Trades | Net PnL | PF | Peak L |
|---|---|---:|---:|---:|---:|
| Best PnL & best PF (≥hedge3 trades) | `clarity=none|fib=0.233|hold=12|K=9` | 1441 | 156.91 | 2.768 | 9 |
| Best PF (any trade count) | `clarity=mean_strength|fib=0.233|hold=12|K=9` | 927 | 120.62 | 4.152 | 9 |
| Best mean_strength PnL | `clarity=mean_strength|fib=0.233|hold=18|K=9` | 853 | 126.05 | 3.740 | 9 |
| Best mean_strength PF | `clarity=mean_strength|fib=0.233|hold=12|K=9` | 927 | 120.62 | 4.152 | 9 |

### Clarity filters (direction not clear)

| Clarity | Effect vs add-ons | Best lockbox outcome |
|---|---|---|
| `none` | No block | Highest dollars; peak 9 concurrent; PF up with K |
| `mean_strength` | Skip weak-model add-ons | Lower trade count, **higher PF** (~3–4+) |
| `range_chop` | Skip add-ons in compressed range | Partial help; between favor and none |
| `favor_confirm` | Require oldest book +0.5×TP first | **Too strict** — almost single-book (cl_skip ~1070) |

### K sweep (clarity=none, hold=12, fib irrelevant)

| K | Net PnL | PF | Trades | vs hedge×3 PnL |
|---:|---:|---:|---:|---|
| 3 | 65.83 | 2.320 | 841 | PnL only (Δpnl +7.8) |
| 4 | 81.25 | 2.289 | 971 | PnL only (Δpnl +23.2) |
| 5 | 101.65 | 2.446 | 1102 | YES both (Δpnl +43.6) |
| 6 | 116.40 | 2.484 | 1217 | YES both (Δpnl +58.4) |
| 7 | 131.14 | 2.567 | 1311 | YES both (Δpnl +73.1) |
| 8 | 145.95 | 2.697 | 1386 | YES both (Δpnl +87.9) |
| 9 | 156.91 | 2.768 | 1441 | YES both (Δpnl +98.9) |

## Does this improve the strategy?

- Vs **hedge×3 uniform**: best arm net PnL **156.91** (+98.86 USDT) and PF **2.768** (vs 2.367). Improvement on *this contaminated window* comes from **more concurrent min-size books** + longer hold on add-ons, not from fib price targets.
- **mean_strength** is the only clarity that both thins choppy add-ons and lifts PF (best PF ~4.15) while still raising PnL vs hedge×3.
- **favor_confirm** does not improve; it collapses concurrency.
- Absolute fib TPs at +23–62% on 12–18h holds are **non-binding** — treat as “no TP / time exit” for book 3+.

## Readiness

- **Maximum earned status:** `LOCKBOX_OPENED_CONTAMINATED` diagnostic only.
- **Not** SHADOW_READY / micro-live from this batch.
- Next bounded step if pursuing: freeze **one** arm (recommend `mean_strength|hold=12|K=6..9` or `none|hold=12|K=5..7` for risk) and re-run on **settle outer out-of-sample**, with stacked-margin risk limits for live.

Source JSON: `structure_v1_eth_concurrent_fib_clarity_latest.json`

