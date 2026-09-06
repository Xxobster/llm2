# Autonomy public-indicator hunt gen 2299

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T003435Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma779_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2205 | 0.5893 | 1.1937 | 0.0062 | 0.1964 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma779_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1942 | 0.5833 | 1.0227 | 0.0054 | 0.1786 | ok | RAN |
| SOLUSDT | 8 | `sma779_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0855 | 0.5504 | 0.4030 | 0.0016 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `sma779_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.0740 | 0.5639 | 0.3517 | 0.0013 | 0.1203 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma779_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.9412 | 0.5606 | -0.3625 | -0.0012 | 0.1364 | ok | RAN |
| SOLUSDT | 4 | `sma779_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9246 | 0.5594 | -0.4648 | -0.0016 | 0.1287 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma779_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 0.8736 | 0.5519 | -0.6650 | -0.0052 | 0.0974 | ok | RAN |
| ETHUSDT | 8 | `sma779_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 0.8415 | 0.5460 | -0.8972 | -0.0067 | 0.1104 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma779_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma779_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma779_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma779_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma779_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma779_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
