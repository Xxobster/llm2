# Autonomy public-indicator hunt gen 875

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T225526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma570_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0437 | 0.6872 | 4.2920 | 0.0242 | 0.4022 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma570_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9823 | 0.6842 | 4.4805 | 0.0228 | 0.3732 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma570_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8400 | 0.6667 | 3.6755 | 0.0126 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma570_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.7932 | 0.6768 | 3.5132 | 0.0121 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma570_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 1.3037 | 0.6028 | 1.3842 | 0.0106 | 0.2270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma570_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.6461 | 0.6242 | 2.6444 | 0.0097 | 0.3121 | ok | RAN |
| SOLUSDT | 8 | `sma570_above_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.5440 | 0.6062 | 2.3373 | 0.0085 | 0.3000 | ok | RAN |
| ETHUSDT | 4 | `sma570_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.1805 | 0.6011 | 0.9470 | 0.0065 | 0.2131 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma570_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma570_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma570_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma570_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma570_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma570_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
