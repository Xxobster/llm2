# Autonomy public-indicator hunt gen 588

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T234514Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema495_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.1123 | 0.6907 | 4.6621 | 0.0247 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema495_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.8361 | 0.6618 | 3.8938 | 0.0201 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema495_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8703 | 0.6617 | 3.7086 | 0.0130 | 0.3383 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema495_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8814 | 0.6600 | 3.6805 | 0.0128 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema495_above_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.6723 | 0.6243 | 2.8287 | 0.0099 | 0.2832 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema495_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.2165 | 0.6026 | 1.0293 | 0.0078 | 0.1921 | ok | RAN |
| SOLUSDT | 8 | `ema495_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.4910 | 0.5943 | 2.2088 | 0.0076 | 0.2743 | ok | RAN |
| ETHUSDT | 8 | `ema495_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1259 | 0.5963 | 0.6281 | 0.0048 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema495_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema495_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema495_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema495_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
