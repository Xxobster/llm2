# Autonomy public-indicator hunt gen 084

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T150254Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `mdi_high_at_h` | one_head_filter_pi_star | 151 | 12.3353 | 2.1102 | 0.7020 | 4.2424 | 0.0260 | 0.3974 | EBR>35% | RAN |
| ETHUSDT | 4 | `mdi_cross_down_20` | one_head_filter_pi_star | 17 | 1.4087 | 1.7008 | 0.5882 | 1.0063 | 0.0235 | 0.2941 | TPM<MIN | RAN |
| ETHUSDT | 4 | `mdi_high_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.9087 | 0.6821 | 3.8225 | 0.0223 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 4 | `mdi_high_at_h` | one_head_filter_pi_star | 145 | 11.8568 | 2.1562 | 0.6897 | 3.8301 | 0.0173 | 0.4414 | EBR>35% | RAN |
| SOLUSDT | 8 | `mdi_high_at_h` | one_head_filter_pi_star | 129 | 10.5484 | 1.9900 | 0.6667 | 3.3180 | 0.0159 | 0.4574 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `mdi_cross_up_25` | one_head_filter_pi_star | 40 | 3.3202 | 1.2867 | 0.6000 | 0.7277 | 0.0122 | 0.2250 | TPM<MIN | RAN |
| ETHUSDT | 8 | `mdi_cross_down_20` | one_head_filter_pi_star | 31 | 2.5593 | 1.3029 | 0.5806 | 0.6024 | 0.0114 | 0.2581 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `mdi_low_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2532 | 0.6135 | 1.1834 | 0.0081 | 0.2147 | ok | RAN |
| SOLUSDT | 8 | `mdi_low_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.4374 | 0.6000 | 2.2654 | 0.0064 | 0.2537 | ok | RAN |
| SOLUSDT | 4 | `mdi_low_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4268 | 0.6066 | 2.2535 | 0.0062 | 0.2512 | ok | RAN |
| ETHUSDT | 8 | `mdi_low_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.1547 | 0.5987 | 0.7423 | 0.0051 | 0.2038 | ok | RAN |
| SOLUSDT | 8 | `mdi_cross_down_20` | one_head_filter_pi_star | 14 | 1.3835 | 1.3245 | 0.6429 | 0.4682 | 0.0043 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `mdi_cross_up_25` | one_head_filter_pi_star | 27 | 2.3634 | 1.0183 | 0.5556 | 0.0427 | 0.0010 | 0.2222 | TPM<MIN | RAN |
| SOLUSDT | 4 | `mdi_cross_down_20` | one_head_filter_pi_star | 12 | 1.1858 | 0.9621 | 0.5833 | -0.0582 | -0.0006 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `mdi_low_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `mdi_low_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `mdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `mdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `mdi_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `mdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `mdi_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mdi_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `mdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mdi_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
