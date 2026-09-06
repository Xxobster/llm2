# Autonomy public-indicator hunt gen 249

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T015412Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema160_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1666 | 0.7083 | 4.9679 | 0.0252 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema160_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0095 | 0.6954 | 4.5035 | 0.0237 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema160_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2075 | 0.6989 | 4.2942 | 0.0176 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema160_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.2327 | 0.6995 | 4.4177 | 0.0174 | 0.3661 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema160_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1454 | 0.5864 | 0.7560 | 0.0053 | 0.2304 | ok | RAN |
| SOLUSDT | 8 | `ema160_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.3262 | 0.5902 | 1.7262 | 0.0050 | 0.2634 | ok | RAN |
| SOLUSDT | 4 | `ema160_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3253 | 0.5879 | 1.7081 | 0.0050 | 0.2714 | ok | RAN |
| ETHUSDT | 4 | `ema160_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1253 | 0.5882 | 0.6675 | 0.0045 | 0.2193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema160_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
