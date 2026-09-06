# Autonomy public-indicator hunt gen 548

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T210728Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema445_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.9850 | 0.6822 | 4.4243 | 0.0232 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema445_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8273 | 0.6683 | 4.0422 | 0.0206 | 0.3606 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema445_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 1.8404 | 0.6604 | 3.6851 | 0.0123 | 0.3443 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema445_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7437 | 0.6524 | 3.3494 | 0.0115 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema445_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5948 | 0.6149 | 2.5978 | 0.0091 | 0.2816 | ok | RAN |
| ETHUSDT | 4 | `ema445_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.2533 | 0.6105 | 1.2400 | 0.0087 | 0.1977 | ok | RAN |
| SOLUSDT | 8 | `ema445_above_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.4817 | 0.6061 | 2.1601 | 0.0078 | 0.2970 | ok | RAN |
| ETHUSDT | 8 | `ema445_above_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.2176 | 0.5964 | 1.0716 | 0.0076 | 0.2048 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema445_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema445_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema445_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema445_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema445_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema445_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
