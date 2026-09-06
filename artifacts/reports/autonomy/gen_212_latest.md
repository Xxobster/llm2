# Autonomy public-indicator hunt gen 212

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T232201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema42_cross_up` | one_head_filter_pi_star | 17 | 1.4409 | 14.4016 | 0.8235 | 3.0572 | 0.0534 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema42_cross_down` | one_head_filter_pi_star | 23 | 1.9630 | 4.4766 | 0.8261 | 2.5420 | 0.0336 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema42_cross_down` | one_head_filter_pi_star | 15 | 1.8244 | 1.9068 | 0.5333 | 1.4190 | 0.0233 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema42_cross_down` | one_head_filter_pi_star | 12 | 1.0242 | 2.3146 | 0.7500 | 1.1317 | 0.0222 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema42_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8312 | 0.6866 | 3.9805 | 0.0213 | 0.3779 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema42_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8133 | 0.6869 | 3.9044 | 0.0211 | 0.3738 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema42_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1660 | 0.6848 | 4.0273 | 0.0177 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema42_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1148 | 0.6790 | 3.8974 | 0.0171 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema42_cross_up` | one_head_filter_pi_star | 16 | 1.3926 | 1.2157 | 0.5625 | 0.3548 | 0.0087 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema42_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2197 | 0.5963 | 1.0118 | 0.0069 | 0.2112 | ok | RAN |
| ETHUSDT | 4 | `ema42_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2158 | 0.5951 | 1.0022 | 0.0067 | 0.2086 | ok | RAN |
| SOLUSDT | 4 | `ema42_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3774 | 0.6019 | 2.0325 | 0.0055 | 0.2407 | ok | RAN |
| SOLUSDT | 8 | `ema42_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3604 | 0.6000 | 1.9466 | 0.0053 | 0.2465 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema42_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema42_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema42_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema42_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema42_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema42_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
