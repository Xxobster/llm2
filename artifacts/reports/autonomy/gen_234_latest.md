# Autonomy public-indicator hunt gen 234

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T005331Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret68_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.8702 | 0.6902 | 4.0849 | 0.0221 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret68_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7816 | 0.6667 | 3.7470 | 0.0205 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret68_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.3141 | 0.6968 | 4.6515 | 0.0186 | 0.3830 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret68_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.3362 | 0.6994 | 4.5179 | 0.0184 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret68_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.3359 | 0.6257 | 1.6752 | 0.0106 | 0.2353 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret68_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3019 | 0.6102 | 1.4680 | 0.0096 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `ret68_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3848 | 0.6087 | 1.9641 | 0.0058 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `ret68_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3744 | 0.6071 | 1.9611 | 0.0057 | 0.2449 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret68_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret68_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret68_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret68_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret68_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret68_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
