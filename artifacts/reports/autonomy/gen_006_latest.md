# Autonomy public-indicator hunt gen 006

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260821T054051Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `aroon_cross_down` | one_head_filter_pi_star | 13 | 1.1114 | 6.8066 | 0.6923 | 2.1946 | 0.0351 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `aroon_cross_down` | one_head_filter_pi_star | 34 | 2.8097 | 1.7440 | 0.6471 | 1.3706 | 0.0244 | 0.3235 | TPM<MIN | RAN |
| ETHUSDT | 4 | `aroon_cross_up` | one_head_filter_pi_star | 20 | 1.9516 | 1.6283 | 0.6000 | 0.9321 | 0.0235 | 0.1500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `aroon_cross_up` | one_head_filter_pi_star | 28 | 2.5275 | 1.6524 | 0.5714 | 1.0829 | 0.0232 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8716 | 0.6789 | 4.1360 | 0.0217 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 8 | `aroon_cross_down` | one_head_filter_pi_star | 46 | 3.7977 | 1.5756 | 0.6522 | 1.3496 | 0.0204 | 0.2609 | TPM<MIN | RAN |
| ETHUSDT | 4 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7850 | 0.6651 | 3.7477 | 0.0202 | 0.3923 | EBR>35% | RAN |
| SOLUSDT | 4 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.2898 | 0.7006 | 4.5258 | 0.0188 | 0.3955 | EBR>35% | RAN |
| SOLUSDT | 8 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.2341 | 0.6957 | 4.1922 | 0.0183 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.2315 | 0.6108 | 1.1107 | 0.0075 | 0.1856 | ok | RAN |
| ETHUSDT | 8 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2239 | 0.5949 | 1.0333 | 0.0068 | 0.2025 | ok | RAN |
| SOLUSDT | 4 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.3458 | 0.5894 | 1.8183 | 0.0052 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3169 | 0.5877 | 1.7348 | 0.0048 | 0.2417 | ok | RAN |
| SOLUSDT | 8 | `aroon_cross_up` | one_head_filter_pi_star | 36 | 3.1384 | 1.1038 | 0.5556 | 0.2431 | 0.0019 | 0.1389 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `aroon_cross_up` | one_head_filter_pi_star | 21 | 1.9534 | 0.6320 | 0.3810 | -0.9177 | -0.0098 | 0.0952 | TPM<MIN | RAN |
| BTCUSDT | 4 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `aroon_up_dom_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `aroon_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `aroon_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `aroon_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `aroon_dn_dom_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `aroon_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `aroon_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
