# Autonomy public-indicator hunt gen 128

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T175232Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret24_cross_down_0` | one_head_filter_pi_star | 49 | 4.1643 | 2.0455 | 0.6122 | 2.1296 | 0.0294 | 0.2245 | ok | RAN |
| ETHUSDT | 8 | `ret24_cross_up_0` | one_head_filter_pi_star | 42 | 3.5147 | 1.6059 | 0.5714 | 1.2309 | 0.0219 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret24_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7835 | 0.6651 | 3.7295 | 0.0201 | 0.3828 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret24_cross_down_0` | one_head_filter_pi_star | 25 | 2.1100 | 2.5571 | 0.6800 | 1.8122 | 0.0200 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret24_neg_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.7482 | 0.6698 | 3.6120 | 0.0198 | 0.3860 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret24_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2235 | 0.6946 | 4.2202 | 0.0183 | 0.4072 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret24_cross_up_0` | one_head_filter_pi_star | 18 | 1.6325 | 1.8326 | 0.5556 | 1.0940 | 0.0168 | 0.2222 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret24_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.0597 | 0.6784 | 3.8738 | 0.0166 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret24_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.4646 | 0.6065 | 2.3757 | 0.0068 | 0.2546 | ok | RAN |
| ETHUSDT | 8 | `ret24_pos_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.2156 | 0.6013 | 1.0039 | 0.0066 | 0.1961 | ok | RAN |
| SOLUSDT | 8 | `ret24_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3663 | 0.5894 | 1.9622 | 0.0054 | 0.2464 | ok | RAN |
| ETHUSDT | 4 | `ret24_pos_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.0402 | 0.5871 | 0.2056 | 0.0014 | 0.1871 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret24_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret24_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret24_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret24_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret24_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret24_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret24_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret24_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret24_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret24_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret24_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret24_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
