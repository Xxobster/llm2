# Autonomy public-indicator hunt gen 2235

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T165252Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma771_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2471 | 0.5988 | 1.3136 | 0.0068 | 0.1860 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma771_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.0772 | 0.5575 | 0.4538 | 0.0023 | 0.1724 | ok | RAN |
| SOLUSDT | 8 | `sma771_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.1161 | 0.5500 | 0.5621 | 0.0021 | 0.1286 | ok | RAN |
| SOLUSDT | 4 | `sma771_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0664 | 0.5556 | 0.3212 | 0.0012 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma771_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9661 | 0.5561 | -0.2074 | -0.0007 | 0.1317 | ok | RAN |
| SOLUSDT | 8 | `sma771_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9475 | 0.5481 | -0.3311 | -0.0011 | 0.1298 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma771_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.9085 | 0.5752 | -0.4956 | -0.0038 | 0.1176 | ok | RAN |
| ETHUSDT | 4 | `sma771_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8270 | 0.5515 | -0.9864 | -0.0072 | 0.0909 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma771_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma771_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma771_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma771_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma771_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma771_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
