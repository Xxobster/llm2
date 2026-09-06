# Autonomy public-indicator hunt gen 364

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T173830Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema215_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9674 | 0.6943 | 4.3133 | 0.0229 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema215_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9351 | 0.6939 | 4.2919 | 0.0223 | 0.3827 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema215_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2383 | 0.6949 | 4.3685 | 0.0176 | 0.3785 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema215_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2724 | 0.7029 | 4.4081 | 0.0175 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema215_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2193 | 0.5978 | 1.1409 | 0.0077 | 0.2235 | ok | RAN |
| SOLUSDT | 4 | `ema215_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4555 | 0.6096 | 2.2068 | 0.0069 | 0.2674 | ok | RAN |
| ETHUSDT | 8 | `ema215_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1786 | 0.6000 | 0.9316 | 0.0062 | 0.2054 | ok | RAN |
| SOLUSDT | 8 | `ema215_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.2533 | 0.5758 | 1.3706 | 0.0041 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema215_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema215_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema215_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema215_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema215_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema215_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
