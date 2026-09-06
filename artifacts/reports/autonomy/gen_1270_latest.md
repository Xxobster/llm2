# Autonomy public-indicator hunt gen 1270

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T172305Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma700_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0960 | 0.7068 | 4.6247 | 0.0243 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma700_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9184 | 0.6856 | 4.1892 | 0.0219 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma700_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8925 | 0.6788 | 3.7168 | 0.0133 | 0.3523 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma700_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.7794 | 0.6579 | 3.3200 | 0.0122 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma700_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2669 | 0.6034 | 1.3414 | 0.0093 | 0.2241 | ok | RAN |
| SOLUSDT | 4 | `wma700_above_at_h` | one_head_filter_pi_star | 174 | 14.2689 | 1.5692 | 0.6092 | 2.5280 | 0.0090 | 0.2989 | ok | RAN |
| SOLUSDT | 8 | `wma700_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5513 | 0.6136 | 2.4583 | 0.0086 | 0.2784 | ok | RAN |
| ETHUSDT | 4 | `wma700_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1955 | 0.5926 | 1.0045 | 0.0073 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma700_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
