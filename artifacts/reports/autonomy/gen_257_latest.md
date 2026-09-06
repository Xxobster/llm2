# Autonomy public-indicator hunt gen 257

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T022702Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema180_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0748 | 0.7053 | 4.6207 | 0.0244 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema180_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0106 | 0.6943 | 4.5221 | 0.0231 | 0.3679 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema180_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2279 | 0.6964 | 4.2484 | 0.0175 | 0.3869 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema180_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2149 | 0.6971 | 4.3215 | 0.0175 | 0.3771 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema180_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.2544 | 0.6067 | 1.2973 | 0.0086 | 0.2135 | ok | RAN |
| ETHUSDT | 4 | `ema180_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1629 | 0.5895 | 0.8611 | 0.0059 | 0.2263 | ok | RAN |
| SOLUSDT | 8 | `ema180_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3048 | 0.5900 | 1.6149 | 0.0048 | 0.2600 | ok | RAN |
| SOLUSDT | 4 | `ema180_above_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2965 | 0.5833 | 1.5957 | 0.0047 | 0.2647 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema180_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema180_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema180_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema180_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
