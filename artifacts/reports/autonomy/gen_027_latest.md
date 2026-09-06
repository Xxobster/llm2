# Autonomy public-indicator hunt gen 027

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T105636Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `qstick_pos_at_h` | one_head_filter_pi_star | 19 | 1.7535 | 5.9502 | 0.8421 | 2.9182 | 0.0395 | 0.6316 | EBR>35% | RAN |
| ETHUSDT | 4 | `qstick_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8082 | 0.6789 | 3.8281 | 0.0206 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `qstick_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1871 | 0.6890 | 4.0490 | 0.0176 | 0.4146 | EBR>35% | RAN |
| SOLUSDT | 8 | `qstick_cross_up_0` | one_head_filter_pi_star | 81 | 6.6673 | 2.0556 | 0.7037 | 2.5543 | 0.0153 | 0.3827 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `qstick_cross_up_0` | one_head_filter_pi_star | 134 | 10.9466 | 1.5275 | 0.6493 | 2.1155 | 0.0147 | 0.3358 | ok | RAN |
| ETHUSDT | 8 | `qstick_neg_at_h` | one_head_filter_pi_star | 45 | 3.7439 | 1.3723 | 0.6222 | 0.8426 | 0.0100 | 0.1333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `qstick_cross_down_0` | one_head_filter_pi_star | 129 | 10.6036 | 1.2815 | 0.5969 | 1.1908 | 0.0084 | 0.1473 | ok | RAN |
| SOLUSDT | 8 | `qstick_cross_down_0` | one_head_filter_pi_star | 197 | 16.1627 | 1.4245 | 0.6041 | 2.1880 | 0.0062 | 0.2284 | ok | RAN |
| SOLUSDT | 4 | `qstick_pos_at_h` | one_head_filter_pi_star | 220 | 17.9389 | 1.3971 | 0.6000 | 2.1601 | 0.0059 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `qstick_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1755 | 0.5901 | 0.8244 | 0.0057 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `qstick_neg_at_h` | one_head_filter_pi_star | 15 | 1.2311 | 1.2017 | 0.5333 | 0.3221 | 0.0024 | 0.1333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `qstick_cross_down_0` | one_head_filter_pi_star | 13 | 1.1063 | 0.5391 | 0.3077 | -0.7768 | -0.0355 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `qstick_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `qstick_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `qstick_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `qstick_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `qstick_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `qstick_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `qstick_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `qstick_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `qstick_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `qstick_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `qstick_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `qstick_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
