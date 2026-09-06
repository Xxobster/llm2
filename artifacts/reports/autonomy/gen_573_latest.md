# Autonomy public-indicator hunt gen 573

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T224458Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret91_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8409 | 0.6735 | 3.8601 | 0.0210 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret91_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8459 | 0.6734 | 4.0623 | 0.0209 | 0.3719 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret91_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.2136 | 0.6772 | 4.4334 | 0.0165 | 0.3598 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret91_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.1758 | 0.6742 | 4.1910 | 0.0163 | 0.3708 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret91_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2620 | 0.6180 | 1.2846 | 0.0089 | 0.2360 | ok | RAN |
| ETHUSDT | 4 | `ret91_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2084 | 0.6082 | 1.0969 | 0.0071 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `ret91_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3729 | 0.5956 | 1.8829 | 0.0059 | 0.2568 | ok | RAN |
| SOLUSDT | 4 | `ret91_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3607 | 0.6000 | 1.8529 | 0.0058 | 0.2579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret91_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret91_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret91_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret91_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret91_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret91_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
