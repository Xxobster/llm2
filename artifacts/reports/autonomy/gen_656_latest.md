# Autonomy public-indicator hunt gen 656

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T040835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma1240_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1424 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1240_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0621 | 0.6891 | 4.1287 | 0.0226 | 0.3575 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma1240_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.9324 | 0.6776 | 4.0311 | 0.0209 | 0.3505 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1240_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.7464 | 0.6350 | 3.8565 | 0.0116 | 0.3139 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1240_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.7206 | 0.6374 | 3.7413 | 0.0115 | 0.3114 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1240_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.2378 | 0.5850 | 1.0668 | 0.0092 | 0.2041 | ok | RAN |
| SOLUSDT | 8 | `sma1240_above_at_h` | one_head_filter_pi_star | 85 | 6.9863 | 1.5358 | 0.6471 | 1.6871 | 0.0090 | 0.3176 | ok | RAN |
| SOLUSDT | 4 | `sma1240_above_at_h` | one_head_filter_pi_star | 88 | 7.2329 | 1.4192 | 0.6364 | 1.4040 | 0.0069 | 0.2841 | ok | RAN |
| ETHUSDT | 8 | `sma1240_above_at_h` | one_head_filter_pi_star | 121 | 9.9460 | 1.1002 | 0.5702 | 0.4460 | 0.0041 | 0.2149 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1240_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4938 | 0.3125 | -1.0772 | -0.0564 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1240_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0573 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
