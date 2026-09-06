# Autonomy public-indicator hunt gen 107

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T163154Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret8_pos_at_h` | one_head_filter_pi_star | 42 | 3.5042 | 4.2940 | 0.8333 | 3.4733 | 0.0259 | 0.5000 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret8_cross_up_0` | one_head_filter_pi_star | 93 | 7.6430 | 2.7250 | 0.7312 | 3.8959 | 0.0206 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret8_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8082 | 0.6789 | 3.8281 | 0.0205 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret8_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2237 | 0.6928 | 4.1547 | 0.0181 | 0.4157 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret8_cross_up_0` | one_head_filter_pi_star | 178 | 14.5410 | 1.5673 | 0.6517 | 2.7113 | 0.0159 | 0.3539 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret8_cross_down_0` | one_head_filter_pi_star | 133 | 10.9119 | 1.6146 | 0.6391 | 2.3213 | 0.0082 | 0.1880 | ok | RAN |
| SOLUSDT | 4 | `ret8_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.4199 | 0.6019 | 2.2505 | 0.0062 | 0.2546 | ok | RAN |
| ETHUSDT | 4 | `ret8_pos_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.1708 | 0.5890 | 0.8066 | 0.0057 | 0.2086 | ok | RAN |
| ETHUSDT | 8 | `ret8_neg_at_h` | one_head_filter_pi_star | 33 | 2.7455 | 1.0712 | 0.6061 | 0.1606 | 0.0021 | 0.0909 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret8_cross_down_0` | one_head_filter_pi_star | 122 | 10.0282 | 0.9964 | 0.5574 | -0.0164 | -0.0001 | 0.1393 | ok | RAN |
| BTCUSDT | 4 | `ret8_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret8_cross_down_0` | one_head_filter_pi_star | 13 | 1.1063 | 0.4457 | 0.2308 | -1.0589 | -0.0518 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret8_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret8_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret8_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret8_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret8_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret8_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret8_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret8_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret8_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret8_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret8_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret8_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
