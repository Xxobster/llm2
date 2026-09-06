# Autonomy public-indicator hunt gen 026

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T104012Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `dem_oversold_at_h` | one_head_filter_pi_star | 128 | 10.4681 | 2.1008 | 0.7266 | 3.8135 | 0.0268 | 0.4219 | EBR>35% | RAN |
| ETHUSDT | 4 | `dem_oversold_at_h` | one_head_filter_pi_star | 154 | 12.5945 | 2.1112 | 0.7208 | 4.0535 | 0.0259 | 0.4026 | EBR>35% | RAN |
| SOLUSDT | 8 | `dem_cross_up_03` | one_head_filter_pi_star | 42 | 3.4640 | 2.2563 | 0.7381 | 2.3132 | 0.0189 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `dem_oversold_at_h` | one_head_filter_pi_star | 122 | 9.9760 | 2.2038 | 0.6967 | 3.7211 | 0.0188 | 0.4426 | EBR>35% | RAN |
| SOLUSDT | 8 | `dem_oversold_at_h` | one_head_filter_pi_star | 100 | 8.1771 | 2.2111 | 0.6600 | 3.3784 | 0.0183 | 0.4400 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `dem_overbought_at_h` | one_head_filter_pi_star | 96 | 7.8782 | 1.8512 | 0.6562 | 2.9645 | 0.0132 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `dem_overbought_at_h` | one_head_filter_pi_star | 78 | 6.4372 | 1.1795 | 0.5769 | 0.6529 | 0.0059 | 0.2564 | ok | RAN |
| ETHUSDT | 8 | `dem_cross_up_03` | one_head_filter_pi_star | 59 | 5.1172 | 1.1422 | 0.5763 | 0.4307 | 0.0050 | 0.3051 | ok | RAN |
| SOLUSDT | 4 | `dem_overbought_at_h` | one_head_filter_pi_star | 140 | 11.4157 | 1.2545 | 0.5929 | 1.2546 | 0.0040 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `dem_cross_down_07` | one_head_filter_pi_star | 60 | 5.0109 | 1.0205 | 0.5167 | 0.0712 | 0.0003 | 0.1667 | ok | RAN |
| ETHUSDT | 4 | `dem_overbought_at_h` | one_head_filter_pi_star | 99 | 8.1696 | 0.9576 | 0.5556 | -0.1979 | -0.0015 | 0.1919 | ok | RAN |
| SOLUSDT | 4 | `dem_cross_down_07` | one_head_filter_pi_star | 11 | 1.1091 | 0.8623 | 0.6364 | -0.2237 | -0.0023 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 8 | `dem_cross_down_07` | one_head_filter_pi_star | 39 | 3.2183 | 0.4036 | 0.4103 | -2.0496 | -0.0215 | 0.0769 | TPM<MIN | RAN |
| BTCUSDT | 4 | `dem_overbought_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0486 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `dem_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `dem_cross_down_07` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `dem_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `dem_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `dem_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `dem_cross_down_07` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dem_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dem_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dem_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `dem_cross_down_07` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
