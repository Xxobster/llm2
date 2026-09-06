# Autonomy public-indicator hunt gen 197

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T222158Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret52_cross_up_0` | one_head_filter_pi_star | 13 | 1.4052 | 2.0268 | 0.6923 | 1.1328 | 0.0219 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret52_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7360 | 0.6684 | 3.6095 | 0.0200 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret52_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.6983 | 0.6732 | 3.5257 | 0.0191 | 0.3561 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret52_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1305 | 0.6994 | 3.9600 | 0.0175 | 0.4049 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret52_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1166 | 0.6975 | 3.9807 | 0.0172 | 0.4012 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret52_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.3544 | 0.6087 | 1.6869 | 0.0106 | 0.2283 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret52_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3057 | 0.6045 | 1.4795 | 0.0093 | 0.2316 | ok | RAN |
| SOLUSDT | 8 | `ret52_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.4960 | 0.6095 | 2.5360 | 0.0070 | 0.2571 | ok | RAN |
| SOLUSDT | 4 | `ret52_pos_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.4072 | 0.5962 | 2.1440 | 0.0060 | 0.2596 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret52_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret52_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret52_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret52_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret52_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret52_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret52_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret52_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret52_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret52_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
