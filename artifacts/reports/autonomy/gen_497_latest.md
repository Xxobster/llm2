# Autonomy public-indicator hunt gen 497

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T174257Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema800_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 2.1363 | 0.6976 | 4.5425 | 0.0246 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema800_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.1020 | 0.6942 | 4.3947 | 0.0240 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema800_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.8974 | 0.6667 | 4.0956 | 0.0134 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema800_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.8090 | 0.6508 | 3.9295 | 0.0125 | 0.3056 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema800_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.6356 | 0.6418 | 2.3894 | 0.0097 | 0.3284 | ok | RAN |
| ETHUSDT | 4 | `ema800_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2679 | 0.6048 | 1.3137 | 0.0093 | 0.1976 | ok | RAN |
| SOLUSDT | 8 | `ema800_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.6376 | 0.6190 | 2.3649 | 0.0092 | 0.3254 | ok | RAN |
| ETHUSDT | 8 | `ema800_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1267 | 0.5833 | 0.6454 | 0.0049 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema800_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema800_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
