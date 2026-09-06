# Autonomy public-indicator hunt gen 388

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T233615Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema245_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9407 | 0.6959 | 4.2463 | 0.0230 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema245_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8529 | 0.6837 | 4.0914 | 0.0209 | 0.3878 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema245_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.2436 | 0.7011 | 4.5082 | 0.0175 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema245_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1586 | 0.6915 | 4.3402 | 0.0167 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema245_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2233 | 0.5989 | 1.1463 | 0.0076 | 0.2088 | ok | RAN |
| ETHUSDT | 8 | `ema245_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2142 | 0.6096 | 1.1097 | 0.0074 | 0.2139 | ok | RAN |
| SOLUSDT | 4 | `ema245_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3969 | 0.5957 | 1.9601 | 0.0062 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `ema245_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3811 | 0.6010 | 1.9441 | 0.0059 | 0.2591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema245_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema245_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema245_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema245_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema245_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema245_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
