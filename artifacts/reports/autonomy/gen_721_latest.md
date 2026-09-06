# Autonomy public-indicator hunt gen 721

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T084215Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1360_below_at_h` | one_head_filter_pi_star | 297 | 24.2622 | 1.7060 | 0.6566 | 3.9562 | 0.0177 | 0.3232 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1360_below_at_h` | one_head_filter_pi_star | 300 | 24.5073 | 1.6739 | 0.6533 | 3.8038 | 0.0171 | 0.3200 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1360_above_at_h` | one_head_filter_pi_star | 66 | 5.6161 | 1.4470 | 0.6212 | 1.2810 | 0.0167 | 0.2576 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1360_below_at_h` | one_head_filter_pi_star | 278 | 22.7323 | 1.7181 | 0.6367 | 3.8010 | 0.0116 | 0.3129 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1360_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.7123 | 0.6304 | 3.7181 | 0.0115 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1360_above_at_h` | one_head_filter_pi_star | 67 | 5.7012 | 1.3121 | 0.6119 | 0.9803 | 0.0113 | 0.2388 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1360_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6276 | 0.6585 | 2.2064 | 0.0091 | 0.2764 | ok | RAN |
| SOLUSDT | 4 | `ema1360_above_at_h` | one_head_filter_pi_star | 99 | 8.0725 | 1.5184 | 0.6263 | 1.7099 | 0.0077 | 0.2727 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1360_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0653 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1360_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0846 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1360_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1360_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1360_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
