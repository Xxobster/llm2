# Autonomy public-indicator hunt gen 217

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T234330Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema90_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9467 | 0.6935 | 4.3411 | 0.0230 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema90_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.8922 | 0.6853 | 4.2013 | 0.0216 | 0.3604 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema90_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2570 | 0.6941 | 4.3146 | 0.0183 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema90_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2174 | 0.6890 | 4.1795 | 0.0179 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema90_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2604 | 0.6089 | 1.2441 | 0.0084 | 0.2291 | ok | RAN |
| ETHUSDT | 8 | `ema90_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.2239 | 0.5968 | 1.1158 | 0.0073 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `ema90_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3199 | 0.5922 | 1.6813 | 0.0048 | 0.2621 | ok | RAN |
| SOLUSDT | 4 | `ema90_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3076 | 0.5905 | 1.6563 | 0.0047 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
