# Autonomy public-indicator hunt gen 1278

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T180712Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma705_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1688 | 0.7017 | 4.7309 | 0.0256 | 0.3978 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma705_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.0715 | 0.6927 | 4.5638 | 0.0243 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma705_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8586 | 0.6736 | 3.5930 | 0.0129 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma705_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8319 | 0.6562 | 3.5350 | 0.0124 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma705_above_at_h` | one_head_filter_pi_star | 185 | 15.1709 | 1.6391 | 0.6270 | 2.8555 | 0.0100 | 0.2919 | ok | RAN |
| ETHUSDT | 8 | `wma705_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2447 | 0.6066 | 1.2601 | 0.0088 | 0.2131 | ok | RAN |
| SOLUSDT | 8 | `wma705_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5146 | 0.6102 | 2.3789 | 0.0082 | 0.2825 | ok | RAN |
| ETHUSDT | 4 | `wma705_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1920 | 0.5969 | 1.0244 | 0.0069 | 0.2251 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma705_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma705_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
