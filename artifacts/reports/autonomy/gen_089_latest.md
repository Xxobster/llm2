# Autonomy public-indicator hunt gen 089

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T152142Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema12_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8283 | 0.6847 | 3.9569 | 0.0214 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema12_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0204 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema12_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2040 | 0.6964 | 4.1280 | 0.0180 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema12_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema12_cross_up` | one_head_filter_pi_star | 39 | 3.2084 | 2.2672 | 0.7436 | 1.9852 | 0.0175 | 0.3590 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema12_cross_down` | one_head_filter_pi_star | 12 | 1.0161 | 2.5334 | 0.8333 | 1.1882 | 0.0134 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema12_above_at_h` | one_head_filter_pi_star | 152 | 12.5433 | 1.2778 | 0.6053 | 1.2143 | 0.0090 | 0.2105 | ok | RAN |
| ETHUSDT | 4 | `ema12_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2179 | 0.5963 | 1.0035 | 0.0070 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `ema12_cross_down` | one_head_filter_pi_star | 94 | 7.9087 | 1.5802 | 0.6277 | 1.8096 | 0.0067 | 0.1170 | ok | RAN |
| ETHUSDT | 8 | `ema12_cross_up` | one_head_filter_pi_star | 88 | 7.2378 | 1.1905 | 0.5909 | 0.6986 | 0.0059 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `ema12_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3863 | 0.5943 | 2.0664 | 0.0058 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ema12_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3751 | 0.5953 | 2.0376 | 0.0055 | 0.2465 | ok | RAN |
| ETHUSDT | 8 | `ema12_cross_down` | one_head_filter_pi_star | 52 | 4.6834 | 1.0778 | 0.5769 | 0.2323 | 0.0022 | 0.1731 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema12_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6235 | 0.3333 | -0.7532 | -0.0366 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema12_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema12_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema12_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema12_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
