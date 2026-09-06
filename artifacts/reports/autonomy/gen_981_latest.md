# Autonomy public-indicator hunt gen 981

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T103008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret193_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 2.2772 | 0.7081 | 4.7623 | 0.0272 | 0.3975 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret193_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.0507 | 0.6964 | 4.3398 | 0.0254 | 0.3929 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret193_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0977 | 0.6747 | 3.8797 | 0.0155 | 0.3735 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret193_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.8283 | 0.6527 | 3.2013 | 0.0129 | 0.3593 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret193_pos_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.2233 | 0.5990 | 1.1407 | 0.0076 | 0.2396 | ok | RAN |
| SOLUSDT | 8 | `ret193_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.4803 | 0.6188 | 2.2549 | 0.0075 | 0.2762 | ok | RAN |
| SOLUSDT | 4 | `ret193_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4386 | 0.6082 | 2.1345 | 0.0069 | 0.2577 | ok | RAN |
| ETHUSDT | 4 | `ret193_pos_at_h` | one_head_filter_pi_star | 206 | 16.9994 | 1.1743 | 0.5922 | 0.9670 | 0.0063 | 0.2330 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret193_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret193_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret193_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret193_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret193_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret193_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
