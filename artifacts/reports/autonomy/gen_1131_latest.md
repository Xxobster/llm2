# Autonomy public-indicator hunt gen 1131

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T024006Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma616_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0528 | 0.6878 | 4.4056 | 0.0240 | 0.4021 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma616_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0444 | 0.6839 | 4.4454 | 0.0239 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma616_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 1.8141 | 0.6635 | 3.6419 | 0.0122 | 0.3128 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma616_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 1.7618 | 0.6630 | 3.2997 | 0.0118 | 0.3315 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma616_above_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.6918 | 0.6289 | 2.7899 | 0.0105 | 0.3145 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma616_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5384 | 0.6096 | 2.1817 | 0.0086 | 0.3219 | ok | RAN |
| ETHUSDT | 8 | `sma616_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 1.1960 | 0.6026 | 0.9471 | 0.0071 | 0.2252 | ok | RAN |
| ETHUSDT | 4 | `sma616_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1295 | 0.5849 | 0.6789 | 0.0048 | 0.2201 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma616_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma616_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma616_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma616_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma616_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma616_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
