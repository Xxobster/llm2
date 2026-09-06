# Autonomy public-indicator hunt gen 1291

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T191900Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma643_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0378 | 0.6889 | 4.2499 | 0.0238 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma643_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.9675 | 0.6758 | 4.0667 | 0.0231 | 0.3956 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma643_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 1.8049 | 0.6700 | 3.5289 | 0.0124 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma643_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7908 | 0.6683 | 3.5135 | 0.0121 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma643_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.6627 | 0.6301 | 2.5926 | 0.0102 | 0.3219 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma643_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2225 | 0.6124 | 1.1337 | 0.0080 | 0.2135 | ok | RAN |
| SOLUSDT | 4 | `sma643_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.4998 | 0.6074 | 1.9650 | 0.0079 | 0.3037 | ok | RAN |
| ETHUSDT | 4 | `sma643_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2134 | 0.6087 | 1.0484 | 0.0077 | 0.2298 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma643_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma643_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma643_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma643_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma643_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma643_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
