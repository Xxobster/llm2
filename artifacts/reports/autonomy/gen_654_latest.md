# Autonomy public-indicator hunt gen 654

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T040010Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma315_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.0256 | 0.7017 | 4.4521 | 0.0237 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma315_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.9643 | 0.6966 | 4.2410 | 0.0225 | 0.3876 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma315_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2683 | 0.6994 | 4.3774 | 0.0177 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma315_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2027 | 0.6905 | 4.1912 | 0.0171 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma315_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2067 | 0.5990 | 1.0766 | 0.0073 | 0.2284 | ok | RAN |
| SOLUSDT | 4 | `wma315_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4030 | 0.5918 | 2.0097 | 0.0063 | 0.2653 | ok | RAN |
| ETHUSDT | 8 | `wma315_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.1639 | 0.5859 | 0.8759 | 0.0058 | 0.2273 | ok | RAN |
| SOLUSDT | 8 | `wma315_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3469 | 0.5990 | 1.7956 | 0.0055 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma315_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma315_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma315_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma315_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma315_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma315_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
