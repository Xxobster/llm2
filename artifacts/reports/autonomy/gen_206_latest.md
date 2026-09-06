# Autonomy public-indicator hunt gen 206

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T225907Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma35_cross_down` | one_head_filter_pi_star | 23 | 2.4418 | 2.8385 | 0.6522 | 2.1798 | 0.0336 | 0.2174 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma35_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma35_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma35_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1911 | 0.6951 | 4.0619 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma35_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1649 | 0.6890 | 4.0090 | 0.0176 | 0.4146 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma35_cross_down` | one_head_filter_pi_star | 24 | 2.0321 | 2.6873 | 0.7083 | 1.8296 | 0.0159 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma35_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2071 | 0.5938 | 0.9657 | 0.0066 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `wma35_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1807 | 0.5912 | 0.8395 | 0.0058 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `wma35_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3749 | 0.5972 | 2.0213 | 0.0055 | 0.2407 | ok | RAN |
| SOLUSDT | 8 | `wma35_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3312 | 0.5896 | 1.8085 | 0.0049 | 0.2406 | ok | RAN |
| ETHUSDT | 8 | `wma35_cross_up` | one_head_filter_pi_star | 12 | 1.0431 | 1.0454 | 0.6667 | 0.0685 | 0.0021 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma35_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma35_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma35_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma35_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma35_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma35_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
