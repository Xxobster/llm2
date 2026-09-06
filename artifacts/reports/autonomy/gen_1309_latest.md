# Autonomy public-indicator hunt gen 1309

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T211333Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret230_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.1723 | 0.7095 | 4.7354 | 0.0271 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret230_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.0329 | 0.6946 | 4.1958 | 0.0244 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret230_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.8633 | 0.6497 | 3.5104 | 0.0131 | 0.3672 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret230_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.7675 | 0.6556 | 3.2707 | 0.0122 | 0.3611 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret230_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2551 | 0.6140 | 1.2282 | 0.0087 | 0.2281 | ok | RAN |
| ETHUSDT | 8 | `ret230_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2456 | 0.5956 | 1.2287 | 0.0084 | 0.2295 | ok | RAN |
| SOLUSDT | 8 | `ret230_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4582 | 0.6117 | 2.1671 | 0.0074 | 0.2766 | ok | RAN |
| SOLUSDT | 4 | `ret230_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.3468 | 0.5964 | 1.5608 | 0.0057 | 0.2831 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret230_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret230_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret230_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret230_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret230_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret230_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
