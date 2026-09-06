# Autonomy public-indicator hunt gen 1057

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T173054Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2200_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0833 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2200_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 1.6027 | 0.6424 | 3.6876 | 0.0162 | 0.3052 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2200_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.5641 | 0.6401 | 3.4877 | 0.0153 | 0.3068 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2200_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.9609 | 0.6628 | 4.4905 | 0.0148 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2200_below_at_h` | one_head_filter_pi_star | 280 | 22.7786 | 1.7883 | 0.6500 | 4.0437 | 0.0121 | 0.3179 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2200_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.7271 | 0.6509 | 2.3442 | 0.0105 | 0.2736 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2200_above_at_h` | one_head_filter_pi_star | 96 | 7.8292 | 1.7707 | 0.6562 | 2.2019 | 0.0101 | 0.2396 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2200_above_at_h` | one_head_filter_pi_star | 13 | 4.0514 | 0.7311 | 0.3077 | -0.9452 | -0.0139 | 0.2308 | ok | RAN |
| ETHUSDT | 4 | `ema2200_above_at_h` | one_head_filter_pi_star | 15 | 4.6747 | 0.7236 | 0.3333 | -1.0654 | -0.0150 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `ema2200_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0668 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2200_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3426 | 0.2308 | -1.3975 | -0.0780 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2200_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2200_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2200_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
