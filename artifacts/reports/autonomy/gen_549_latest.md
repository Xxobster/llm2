# Autonomy public-indicator hunt gen 549

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T211115Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret85_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8917 | 0.6717 | 4.1733 | 0.0214 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret85_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7834 | 0.6633 | 3.7831 | 0.0201 | 0.3618 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret85_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.1814 | 0.6789 | 4.3143 | 0.0164 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret85_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.1326 | 0.6720 | 4.1908 | 0.0158 | 0.3602 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret85_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.2998 | 0.6180 | 1.4517 | 0.0098 | 0.2303 | ok | RAN |
| ETHUSDT | 4 | `ret85_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2963 | 0.6141 | 1.4490 | 0.0096 | 0.2228 | ok | RAN |
| SOLUSDT | 4 | `ret85_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3705 | 0.6031 | 1.9163 | 0.0057 | 0.2577 | ok | RAN |
| SOLUSDT | 8 | `ret85_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3567 | 0.5968 | 1.8215 | 0.0057 | 0.2688 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret85_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret85_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret85_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret85_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret85_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret85_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
