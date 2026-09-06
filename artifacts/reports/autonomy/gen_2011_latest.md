# Autonomy public-indicator hunt gen 2011

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T103337Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma742_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.2089 | 0.5815 | 1.2078 | 0.0062 | 0.1793 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma742_below_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.1383 | 0.5789 | 0.7930 | 0.0039 | 0.1988 | ok | RAN |
| SOLUSDT | 4 | `sma742_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.1058 | 0.5537 | 0.4566 | 0.0019 | 0.1074 | ok | RAN |
| SOLUSDT | 8 | `sma742_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0590 | 0.5396 | 0.2887 | 0.0011 | 0.1295 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma742_below_at_h` | one_head_filter_pi_star | 215 | 17.4907 | 0.9127 | 0.5442 | -0.5647 | -0.0018 | 0.1302 | ok | RAN |
| SOLUSDT | 4 | `sma742_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.8840 | 0.5455 | -0.7242 | -0.0026 | 0.1313 | ok | RAN |
| ETHUSDT | 4 | `sma742_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8754 | 0.5541 | -0.6494 | -0.0051 | 0.1081 | ok | RAN |
| ETHUSDT | 8 | `sma742_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.8246 | 0.5500 | -0.9877 | -0.0076 | 0.1125 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma742_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma742_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma742_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma742_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma742_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma742_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
