# Autonomy public-indicator hunt gen 1061

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T175705Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret190_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.2117 | 0.7048 | 4.6265 | 0.0256 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret190_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.9674 | 0.6919 | 4.2087 | 0.0241 | 0.3779 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret190_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.0368 | 0.6706 | 3.8462 | 0.0157 | 0.3765 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret190_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.0512 | 0.6782 | 3.9431 | 0.0156 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret190_pos_at_h` | one_head_filter_pi_star | 207 | 17.0819 | 1.2601 | 0.5990 | 1.4020 | 0.0089 | 0.2319 | ok | RAN |
| SOLUSDT | 4 | `ret190_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4428 | 0.6117 | 2.1127 | 0.0067 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `ret190_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3377 | 0.6011 | 1.6690 | 0.0056 | 0.2713 | ok | RAN |
| ETHUSDT | 8 | `ret190_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1104 | 0.5895 | 0.5860 | 0.0039 | 0.2158 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret190_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret190_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret190_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret190_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret190_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret190_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
