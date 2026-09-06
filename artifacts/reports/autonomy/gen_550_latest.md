# Autonomy public-indicator hunt gen 550

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T211508Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma250_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0566 | 0.7065 | 4.6370 | 0.0242 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma250_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9792 | 0.6984 | 4.4094 | 0.0232 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma250_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2805 | 0.7000 | 4.5239 | 0.0181 | 0.3833 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma250_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1661 | 0.6890 | 4.0038 | 0.0168 | 0.3841 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma250_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.1943 | 0.6020 | 1.0229 | 0.0068 | 0.2296 | ok | RAN |
| ETHUSDT | 8 | `wma250_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1632 | 0.5833 | 0.8374 | 0.0058 | 0.2292 | ok | RAN |
| SOLUSDT | 8 | `wma250_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3509 | 0.5922 | 1.8301 | 0.0055 | 0.2670 | ok | RAN |
| SOLUSDT | 4 | `wma250_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3026 | 0.5842 | 1.5984 | 0.0047 | 0.2574 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma250_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma250_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma250_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma250_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma250_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma250_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
