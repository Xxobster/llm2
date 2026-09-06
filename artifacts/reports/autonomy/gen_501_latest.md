# Autonomy public-indicator hunt gen 501

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T175838Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret73_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7726 | 0.6701 | 3.6659 | 0.0205 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret73_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.7117 | 0.6721 | 3.4551 | 0.0189 | 0.3825 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret73_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.2750 | 0.6789 | 4.5516 | 0.0174 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret73_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1515 | 0.6811 | 4.2333 | 0.0164 | 0.3730 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret73_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.3587 | 0.6196 | 1.7466 | 0.0114 | 0.2337 | ok | RAN |
| ETHUSDT | 4 | `ret73_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.3392 | 0.6190 | 1.6808 | 0.0108 | 0.2275 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret73_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3995 | 0.6022 | 2.0113 | 0.0062 | 0.2527 | ok | RAN |
| SOLUSDT | 8 | `ret73_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3479 | 0.6082 | 1.8034 | 0.0056 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret73_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret73_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0459 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret73_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret73_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret73_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret73_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
