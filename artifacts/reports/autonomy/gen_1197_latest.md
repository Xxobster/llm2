# Autonomy public-indicator hunt gen 1197

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T100008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret214_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.2390 | 0.7159 | 4.9225 | 0.0282 | 0.3977 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret214_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1692 | 0.7056 | 4.5652 | 0.0272 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret214_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.9596 | 0.6720 | 3.7727 | 0.0147 | 0.3763 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret214_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9620 | 0.6684 | 3.8876 | 0.0144 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret214_pos_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.5780 | 0.6257 | 2.5026 | 0.0085 | 0.2749 | ok | RAN |
| SOLUSDT | 8 | `ret214_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.5357 | 0.6205 | 2.3648 | 0.0080 | 0.2892 | ok | RAN |
| ETHUSDT | 4 | `ret214_pos_at_h` | one_head_filter_pi_star | 199 | 16.3575 | 1.1916 | 0.5879 | 0.9685 | 0.0065 | 0.2211 | ok | RAN |
| ETHUSDT | 8 | `ret214_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.1213 | 0.5672 | 0.6597 | 0.0045 | 0.2289 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret214_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5803 | 0.3158 | -0.8946 | -0.0447 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret214_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret214_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret214_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret214_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret214_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
