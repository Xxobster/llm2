# Autonomy public-indicator hunt gen 147

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T190710Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma90_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9542 | 0.6970 | 4.4262 | 0.0234 | 0.3737 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma90_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.9072 | 0.6866 | 4.2359 | 0.0227 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma90_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2903 | 0.6941 | 4.3999 | 0.0187 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma90_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2265 | 0.6890 | 4.1794 | 0.0182 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma90_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.3008 | 0.6054 | 1.4638 | 0.0093 | 0.2324 | ok | RAN |
| ETHUSDT | 4 | `sma90_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2906 | 0.6066 | 1.4227 | 0.0089 | 0.2295 | ok | RAN |
| SOLUSDT | 8 | `sma90_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3090 | 0.5952 | 1.6436 | 0.0047 | 0.2571 | ok | RAN |
| SOLUSDT | 4 | `sma90_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2847 | 0.5922 | 1.5436 | 0.0044 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma90_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma90_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma90_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma90_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
