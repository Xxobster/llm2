# Autonomy public-indicator hunt gen 265

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T030126Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema220_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0509 | 0.7037 | 4.4630 | 0.0246 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema220_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0047 | 0.6979 | 4.4702 | 0.0233 | 0.3854 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema220_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.2177 | 0.6973 | 4.4594 | 0.0171 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema220_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.0462 | 0.6872 | 3.9846 | 0.0153 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema220_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1920 | 0.6044 | 0.9800 | 0.0066 | 0.2088 | ok | RAN |
| ETHUSDT | 4 | `ema220_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1769 | 0.6011 | 0.9196 | 0.0062 | 0.2131 | ok | RAN |
| SOLUSDT | 4 | `ema220_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3335 | 0.5897 | 1.7167 | 0.0052 | 0.2667 | ok | RAN |
| SOLUSDT | 8 | `ema220_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.2884 | 0.5864 | 1.5179 | 0.0046 | 0.2618 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
