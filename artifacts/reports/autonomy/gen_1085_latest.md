# Autonomy public-indicator hunt gen 1085

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T211314Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret198_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0044 | 0.6954 | 4.3464 | 0.0237 | 0.3736 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret198_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.0160 | 0.6821 | 4.1790 | 0.0235 | 0.4046 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret198_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0701 | 0.6845 | 3.9330 | 0.0156 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret198_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8806 | 0.6538 | 3.5753 | 0.0136 | 0.3626 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret198_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5520 | 0.6264 | 2.5206 | 0.0086 | 0.2637 | ok | RAN |
| SOLUSDT | 4 | `ret198_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4615 | 0.6100 | 2.2493 | 0.0070 | 0.2650 | ok | RAN |
| ETHUSDT | 4 | `ret198_pos_at_h` | one_head_filter_pi_star | 205 | 16.8507 | 1.2016 | 0.5902 | 1.0922 | 0.0069 | 0.2341 | ok | RAN |
| ETHUSDT | 8 | `ret198_pos_at_h` | one_head_filter_pi_star | 204 | 16.7685 | 1.1433 | 0.5882 | 0.7743 | 0.0053 | 0.2255 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret198_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6894 | 0.3158 | -0.6415 | -0.0323 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret198_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0432 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret198_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret198_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret198_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret198_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
