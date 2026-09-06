# Autonomy public-indicator hunt gen 510

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T183410Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma225_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0441 | 0.6957 | 4.6158 | 0.0241 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma225_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9785 | 0.6859 | 4.4040 | 0.0227 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma225_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.3502 | 0.7052 | 4.5749 | 0.0188 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma225_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1952 | 0.6959 | 4.2018 | 0.0173 | 0.3801 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma225_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2829 | 0.6054 | 1.3906 | 0.0095 | 0.2216 | ok | RAN |
| ETHUSDT | 4 | `wma225_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.2545 | 0.6126 | 1.2859 | 0.0087 | 0.2251 | ok | RAN |
| SOLUSDT | 8 | `wma225_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3191 | 0.5905 | 1.7154 | 0.0050 | 0.2619 | ok | RAN |
| SOLUSDT | 4 | `wma225_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2986 | 0.5871 | 1.5650 | 0.0047 | 0.2687 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma225_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma225_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma225_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma225_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma225_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma225_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
