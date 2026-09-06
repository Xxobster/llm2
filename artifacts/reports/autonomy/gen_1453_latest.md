# Autonomy public-indicator hunt gen 1453

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T221313Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret251_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.2925 | 0.7079 | 4.9692 | 0.0283 | 0.3933 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret251_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0629 | 0.6885 | 4.5611 | 0.0242 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret251_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.8889 | 0.6509 | 3.5449 | 0.0137 | 0.3609 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret251_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.8816 | 0.6506 | 3.4985 | 0.0131 | 0.3614 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret251_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.6237 | 0.6183 | 2.7966 | 0.0095 | 0.2849 | ok | RAN |
| SOLUSDT | 8 | `ret251_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.6157 | 0.6301 | 2.6152 | 0.0090 | 0.2775 | ok | RAN |
| ETHUSDT | 4 | `ret251_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.1415 | 0.5954 | 0.7216 | 0.0050 | 0.2254 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret251_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.0241 | 0.5722 | 0.1360 | 0.0009 | 0.2320 | ok | RAN |
| BTCUSDT | 8 | `ret251_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret251_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret251_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret251_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret251_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret251_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
