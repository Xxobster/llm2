# Autonomy public-indicator hunt gen 281

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T040727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema260_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9355 | 0.6853 | 4.2685 | 0.0224 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema260_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8719 | 0.6818 | 4.1585 | 0.0212 | 0.3788 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema260_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0685 | 0.6771 | 4.2117 | 0.0157 | 0.3646 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema260_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0153 | 0.6719 | 4.0784 | 0.0153 | 0.3594 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema260_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2417 | 0.6111 | 1.2322 | 0.0081 | 0.2056 | ok | RAN |
| SOLUSDT | 8 | `ema260_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5024 | 0.6175 | 2.3805 | 0.0076 | 0.2678 | ok | RAN |
| ETHUSDT | 4 | `ema260_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2030 | 0.5956 | 1.0729 | 0.0071 | 0.2186 | ok | RAN |
| SOLUSDT | 4 | `ema260_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4544 | 0.6021 | 2.2079 | 0.0069 | 0.2618 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema260_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema260_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
