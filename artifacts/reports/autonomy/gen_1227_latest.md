# Autonomy public-indicator hunt gen 1227

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T125308Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma632_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1798 | 0.6932 | 4.5912 | 0.0257 | 0.4091 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma632_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0347 | 0.6878 | 4.2912 | 0.0236 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma632_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8613 | 0.6700 | 3.7136 | 0.0128 | 0.3399 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma632_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.6722 | 0.6585 | 3.1514 | 0.0110 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma632_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.6032 | 0.6265 | 2.5918 | 0.0092 | 0.3012 | ok | RAN |
| SOLUSDT | 8 | `sma632_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.5031 | 0.6129 | 2.1609 | 0.0083 | 0.3161 | ok | RAN |
| ETHUSDT | 4 | `sma632_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.2102 | 0.6095 | 1.0619 | 0.0075 | 0.2071 | ok | RAN |
| ETHUSDT | 8 | `sma632_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1943 | 0.6000 | 0.9750 | 0.0067 | 0.2118 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma632_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma632_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma632_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma632_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma632_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma632_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
