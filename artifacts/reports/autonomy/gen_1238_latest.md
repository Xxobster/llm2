# Autonomy public-indicator hunt gen 1238

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T140842Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma680_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0839 | 0.6952 | 4.6015 | 0.0245 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma680_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0216 | 0.6869 | 4.4735 | 0.0232 | 0.3636 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma680_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.0290 | 0.6906 | 3.9718 | 0.0149 | 0.3591 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma680_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8279 | 0.6564 | 3.5321 | 0.0128 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma680_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5689 | 0.6045 | 2.5682 | 0.0088 | 0.2881 | ok | RAN |
| SOLUSDT | 4 | `wma680_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5545 | 0.6087 | 2.4985 | 0.0086 | 0.2880 | ok | RAN |
| ETHUSDT | 8 | `wma680_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.2201 | 0.5976 | 1.0712 | 0.0079 | 0.2134 | ok | RAN |
| ETHUSDT | 4 | `wma680_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.1740 | 0.5856 | 0.9396 | 0.0063 | 0.2210 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma680_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma680_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
