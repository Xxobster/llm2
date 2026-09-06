# Autonomy public-indicator hunt gen 1500

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T024745Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema972_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema972_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.7881 | 0.6638 | 3.8776 | 0.0186 | 0.3448 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema972_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 1.7327 | 0.6463 | 3.6378 | 0.0180 | 0.3293 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema972_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.8365 | 0.6545 | 4.0291 | 0.0129 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema972_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.6891 | 0.6478 | 3.4599 | 0.0110 | 0.2996 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema972_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.7514 | 0.6610 | 2.4978 | 0.0106 | 0.2966 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema972_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.5786 | 0.6165 | 2.1584 | 0.0088 | 0.3233 | ok | RAN |
| ETHUSDT | 8 | `ema972_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 1.2083 | 0.5873 | 0.8977 | 0.0079 | 0.2302 | ok | RAN |
| ETHUSDT | 4 | `ema972_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.1784 | 0.5840 | 0.8078 | 0.0070 | 0.2160 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema972_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema972_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema972_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema972_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema972_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
