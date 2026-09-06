# Autonomy public-indicator hunt gen 1915

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T004709Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma729_below_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2416 | 0.5915 | 1.2819 | 0.0068 | 0.1951 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma729_below_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.2154 | 0.5858 | 1.1551 | 0.0062 | 0.1775 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma729_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.3042 | 0.5913 | 1.2017 | 0.0053 | 0.1304 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma729_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 0.9966 | 0.5500 | -0.0171 | -0.0001 | 0.1071 | ok | RAN |
| SOLUSDT | 4 | `sma729_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9232 | 0.5512 | -0.4862 | -0.0016 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma729_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 0.8862 | 0.5320 | -0.7252 | -0.0025 | 0.1281 | ok | RAN |
| ETHUSDT | 8 | `sma729_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.8761 | 0.5625 | -0.6922 | -0.0050 | 0.1062 | ok | RAN |
| ETHUSDT | 4 | `sma729_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 0.8172 | 0.5414 | -1.0221 | -0.0078 | 0.1083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma729_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma729_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0694 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma729_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma729_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma729_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma729_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
