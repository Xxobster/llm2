# Autonomy public-indicator hunt gen 1163

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T063438Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma622_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0285 | 0.6872 | 4.3725 | 0.0235 | 0.3897 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma622_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9114 | 0.6734 | 4.1574 | 0.0215 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma622_below_at_h` | one_head_filter_pi_star | 199 | 16.1890 | 1.8196 | 0.6683 | 3.5282 | 0.0122 | 0.3166 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma622_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.8372 | 0.6439 | 2.8936 | 0.0115 | 0.3258 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma622_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.7214 | 0.6567 | 3.2696 | 0.0112 | 0.3234 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma622_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.6109 | 0.6182 | 2.5852 | 0.0094 | 0.3030 | ok | RAN |
| ETHUSDT | 8 | `sma622_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1568 | 0.5976 | 0.8017 | 0.0057 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `sma622_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1480 | 0.5941 | 0.7668 | 0.0055 | 0.2118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma622_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma622_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma622_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma622_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma622_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma622_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
