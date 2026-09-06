# Autonomy public-indicator hunt gen 505

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T181400Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema820_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.9141 | 0.6758 | 4.0708 | 0.0217 | 0.3607 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema820_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8852 | 0.6787 | 3.9566 | 0.0208 | 0.3620 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema820_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.8710 | 0.6609 | 3.9751 | 0.0131 | 0.3133 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema820_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.7624 | 0.6538 | 3.5990 | 0.0118 | 0.2949 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema820_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.6327 | 0.6370 | 2.3526 | 0.0096 | 0.3111 | ok | RAN |
| SOLUSDT | 8 | `ema820_above_at_h` | one_head_filter_pi_star | 144 | 11.7418 | 1.5543 | 0.6111 | 2.1931 | 0.0082 | 0.3056 | ok | RAN |
| ETHUSDT | 8 | `ema820_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1859 | 0.6087 | 0.8574 | 0.0070 | 0.2174 | ok | RAN |
| ETHUSDT | 4 | `ema820_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.1473 | 0.5833 | 0.7121 | 0.0054 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema820_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema820_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
