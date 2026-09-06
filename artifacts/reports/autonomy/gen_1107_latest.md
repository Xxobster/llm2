# Autonomy public-indicator hunt gen 1107

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T235502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma613_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9524 | 0.6811 | 4.1073 | 0.0230 | 0.3946 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma613_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8922 | 0.6735 | 3.9568 | 0.0206 | 0.3776 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma613_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8000 | 0.6650 | 3.4766 | 0.0119 | 0.3150 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma613_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.6852 | 0.6550 | 3.1797 | 0.0110 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma613_above_at_h` | one_head_filter_pi_star | 161 | 13.1280 | 1.6173 | 0.6149 | 2.5941 | 0.0095 | 0.3043 | ok | RAN |
| SOLUSDT | 4 | `sma613_above_at_h` | one_head_filter_pi_star | 157 | 12.8748 | 1.5902 | 0.6178 | 2.4047 | 0.0095 | 0.3185 | ok | RAN |
| ETHUSDT | 4 | `sma613_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1901 | 0.6038 | 0.9381 | 0.0068 | 0.1950 | ok | RAN |
| ETHUSDT | 8 | `sma613_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1290 | 0.5926 | 0.6730 | 0.0048 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma613_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma613_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma613_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma613_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma613_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma613_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
