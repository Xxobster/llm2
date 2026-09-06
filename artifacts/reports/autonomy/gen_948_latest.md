# Autonomy public-indicator hunt gen 948

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T064901Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema945_below_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.9139 | 0.6730 | 3.9810 | 0.0206 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema945_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.7961 | 0.6527 | 3.8506 | 0.0193 | 0.3389 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema945_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.8438 | 0.6561 | 4.0537 | 0.0130 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema945_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7452 | 0.6420 | 3.6289 | 0.0116 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema945_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.7426 | 0.6508 | 2.5833 | 0.0103 | 0.2937 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema945_above_at_h` | one_head_filter_pi_star | 136 | 11.0895 | 1.5813 | 0.6103 | 2.2077 | 0.0091 | 0.3015 | ok | RAN |
| ETHUSDT | 8 | `ema945_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.1917 | 0.5970 | 0.8905 | 0.0074 | 0.2313 | ok | RAN |
| ETHUSDT | 4 | `ema945_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 1.1814 | 0.5954 | 0.8110 | 0.0072 | 0.2214 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema945_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema945_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema945_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema945_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema945_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema945_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
