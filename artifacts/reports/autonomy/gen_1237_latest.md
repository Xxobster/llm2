# Autonomy public-indicator hunt gen 1237

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T134923Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret220_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 2.1950 | 0.7059 | 4.6185 | 0.0271 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret220_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.9361 | 0.6842 | 3.9560 | 0.0236 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret220_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9924 | 0.6686 | 3.8447 | 0.0148 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret220_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.9485 | 0.6618 | 3.9557 | 0.0139 | 0.3578 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret220_pos_at_h` | one_head_filter_pi_star | 162 | 13.2095 | 1.5466 | 0.6235 | 2.3556 | 0.0083 | 0.2963 | ok | RAN |
| ETHUSDT | 4 | `ret220_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2283 | 0.5902 | 1.1408 | 0.0078 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `ret220_pos_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.4202 | 0.6190 | 1.9307 | 0.0066 | 0.2738 | ok | RAN |
| ETHUSDT | 8 | `ret220_pos_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.0648 | 0.5729 | 0.3535 | 0.0023 | 0.2161 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret220_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret220_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret220_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret220_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret220_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret220_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
