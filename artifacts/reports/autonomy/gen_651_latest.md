# Autonomy public-indicator hunt gen 651

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T034816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma382_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0934 | 0.7112 | 4.7106 | 0.0243 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma382_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9419 | 0.6882 | 4.2934 | 0.0225 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma382_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1173 | 0.6811 | 4.2602 | 0.0156 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma382_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.9780 | 0.6701 | 4.0197 | 0.0142 | 0.3660 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma382_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5528 | 0.6203 | 2.5686 | 0.0086 | 0.2727 | ok | RAN |
| SOLUSDT | 8 | `sma382_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5380 | 0.6201 | 2.4318 | 0.0083 | 0.2626 | ok | RAN |
| ETHUSDT | 8 | `sma382_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2150 | 0.5978 | 1.1108 | 0.0074 | 0.2228 | ok | RAN |
| ETHUSDT | 4 | `sma382_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2048 | 0.5885 | 1.0840 | 0.0072 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma382_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma382_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma382_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma382_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma382_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma382_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
