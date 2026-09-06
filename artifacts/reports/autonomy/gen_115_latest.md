# Autonomy public-indicator hunt gen 115

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T170130Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema13_cross_down` | one_head_filter_pi_star | 12 | 1.0161 | 3.2260 | 0.8333 | 1.5196 | 0.0248 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema13_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema13_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8008 | 0.6771 | 3.8681 | 0.0205 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema13_cross_up` | one_head_filter_pi_star | 54 | 4.4414 | 1.7095 | 0.6296 | 1.6444 | 0.0184 | 0.2407 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema13_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema13_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1640 | 0.6890 | 3.9888 | 0.0178 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema13_cross_down` | one_head_filter_pi_star | 76 | 6.3942 | 1.8437 | 0.6579 | 2.1996 | 0.0096 | 0.1316 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema13_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 8 | `ema13_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.4319 | 0.6009 | 2.2731 | 0.0063 | 0.2535 | ok | RAN |
| ETHUSDT | 8 | `ema13_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1792 | 0.5860 | 0.8317 | 0.0059 | 0.2038 | ok | RAN |
| SOLUSDT | 4 | `ema13_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3751 | 0.5953 | 2.0376 | 0.0055 | 0.2465 | ok | RAN |
| ETHUSDT | 8 | `ema13_cross_down` | one_head_filter_pi_star | 56 | 5.0437 | 1.0836 | 0.5536 | 0.2528 | 0.0023 | 0.1786 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema13_cross_up` | one_head_filter_pi_star | 14 | 1.1946 | 0.8109 | 0.5714 | -0.3117 | -0.0039 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema13_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema13_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema13_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema13_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema13_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema13_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema13_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema13_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema13_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema13_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema13_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
