# Autonomy public-indicator hunt gen 270

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T032059Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma70_cross_up` | one_head_filter_pi_star | 19 | 1.5795 | 5.2748 | 0.6316 | 2.3843 | 0.0316 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma70_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8588 | 0.6842 | 3.9776 | 0.0217 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma70_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.7730 | 0.6744 | 3.7311 | 0.0205 | 0.3721 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma70_cross_down` | one_head_filter_pi_star | 34 | 2.9019 | 1.9221 | 0.6765 | 1.5068 | 0.0187 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma70_cross_down` | one_head_filter_pi_star | 20 | 1.6573 | 1.6264 | 0.6500 | 0.9728 | 0.0183 | 0.3000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma70_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1295 | 0.6832 | 3.9322 | 0.0172 | 0.4099 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma70_below_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.0558 | 0.6752 | 3.7026 | 0.0164 | 0.4140 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma70_cross_down` | one_head_filter_pi_star | 12 | 1.0413 | 1.1731 | 0.5833 | 0.2665 | 0.0082 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma70_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2727 | 0.6049 | 1.2347 | 0.0081 | 0.2160 | ok | RAN |
| ETHUSDT | 4 | `wma70_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2492 | 0.5976 | 1.1575 | 0.0076 | 0.2073 | ok | RAN |
| ETHUSDT | 8 | `wma70_cross_up` | one_head_filter_pi_star | 16 | 1.4130 | 1.1514 | 0.5000 | 0.2409 | 0.0060 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma70_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3527 | 0.6000 | 1.9087 | 0.0052 | 0.2465 | ok | RAN |
| SOLUSDT | 8 | `wma70_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3270 | 0.5943 | 1.7757 | 0.0048 | 0.2453 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma70_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma70_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma70_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma70_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
