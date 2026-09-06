# Autonomy public-indicator hunt gen 1064

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T183203Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma2260_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1286 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2260_above_at_h` | one_head_filter_pi_star | 58 | 5.0788 | 1.4895 | 0.6207 | 1.2728 | 0.0184 | 0.2241 | ok | RAN |
| ETHUSDT | 4 | `sma2260_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.6145 | 0.6429 | 3.7078 | 0.0162 | 0.3095 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2260_above_at_h` | one_head_filter_pi_star | 43 | 3.8897 | 1.4327 | 0.6047 | 1.0084 | 0.0155 | 0.2326 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2260_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5165 | 0.6334 | 3.3592 | 0.0144 | 0.3050 | ok | RAN |
| SOLUSDT | 8 | `sma2260_below_at_h` | one_head_filter_pi_star | 295 | 23.9988 | 1.8276 | 0.6441 | 4.2044 | 0.0120 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2260_above_at_h` | one_head_filter_pi_star | 82 | 6.8153 | 1.9152 | 0.6829 | 2.4589 | 0.0120 | 0.2683 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2260_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7093 | 0.6373 | 3.7922 | 0.0106 | 0.3170 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2260_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.6862 | 0.6613 | 1.7271 | 0.0099 | 0.2742 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2260_above_at_h` | one_head_filter_pi_star | 10 | 1.8365 | 0.4943 | 0.3000 | -1.2919 | -0.0624 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2260_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
