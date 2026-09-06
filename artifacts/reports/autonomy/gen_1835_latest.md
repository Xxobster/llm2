# Autonomy public-indicator hunt gen 1835

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T173607Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma718_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2663 | 0.5890 | 1.3849 | 0.0073 | 0.1779 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma718_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.2630 | 0.6000 | 1.4258 | 0.0071 | 0.1886 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma718_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.1382 | 0.5714 | 0.5893 | 0.0025 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `sma718_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.0841 | 0.5433 | 0.3819 | 0.0016 | 0.1102 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma718_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9637 | 0.5619 | -0.2277 | -0.0008 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma718_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 0.8712 | 0.5343 | -0.8228 | -0.0028 | 0.1275 | ok | RAN |
| ETHUSDT | 4 | `sma718_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.8836 | 0.5571 | -0.6044 | -0.0048 | 0.1143 | ok | RAN |
| ETHUSDT | 8 | `sma718_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 0.8299 | 0.5513 | -0.9786 | -0.0071 | 0.1154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma718_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma718_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma718_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma718_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma718_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma718_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
