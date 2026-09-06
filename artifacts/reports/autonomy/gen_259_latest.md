# Autonomy public-indicator hunt gen 259

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T023540Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma72_cross_up` | one_head_filter_pi_star | 22 | 1.8962 | 7.8895 | 0.6818 | 3.0117 | 0.0428 | 0.2273 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma72_cross_down` | one_head_filter_pi_star | 17 | 1.6619 | 1.6844 | 0.5882 | 1.0714 | 0.0216 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma72_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.7661 | 0.6800 | 3.7267 | 0.0200 | 0.3650 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma72_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.7273 | 0.6782 | 3.5780 | 0.0196 | 0.3762 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma72_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2717 | 0.6923 | 4.3426 | 0.0189 | 0.4083 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma72_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2015 | 0.6933 | 4.1581 | 0.0181 | 0.4110 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma72_cross_down` | one_head_filter_pi_star | 23 | 2.4770 | 1.8813 | 0.6957 | 1.4232 | 0.0157 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma72_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3639 | 0.6102 | 1.6573 | 0.0108 | 0.2260 | ok | RAN |
| ETHUSDT | 8 | `sma72_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.3583 | 0.6102 | 1.6154 | 0.0103 | 0.2147 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma72_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3761 | 0.5991 | 1.9844 | 0.0055 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `sma72_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3225 | 0.5962 | 1.7225 | 0.0048 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma72_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma72_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma72_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma72_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma72_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma72_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
