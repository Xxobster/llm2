# Autonomy public-indicator hunt gen 430

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T092804Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma175_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0361 | 0.6974 | 4.6203 | 0.0244 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma175_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9748 | 0.6935 | 4.4660 | 0.0230 | 0.3719 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma175_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2450 | 0.6964 | 4.2981 | 0.0181 | 0.3869 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma175_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2793 | 0.6966 | 4.4725 | 0.0181 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma175_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2548 | 0.6075 | 1.2809 | 0.0085 | 0.2258 | ok | RAN |
| SOLUSDT | 8 | `wma175_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3198 | 0.5874 | 1.6894 | 0.0050 | 0.2621 | ok | RAN |
| SOLUSDT | 4 | `wma175_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.3005 | 0.5931 | 1.5903 | 0.0047 | 0.2647 | ok | RAN |
| ETHUSDT | 4 | `wma175_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1323 | 0.5904 | 0.6988 | 0.0047 | 0.2234 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma175_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma175_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma175_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma175_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma175_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma175_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
