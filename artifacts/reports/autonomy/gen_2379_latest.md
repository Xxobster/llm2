# Autonomy public-indicator hunt gen 2379

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T110918Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma790_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.3011 | 0.5964 | 1.5152 | 0.0080 | 0.1928 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma790_below_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.2409 | 0.5975 | 1.2799 | 0.0065 | 0.1761 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma790_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.2415 | 0.5868 | 1.0140 | 0.0042 | 0.1322 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma790_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0719 | 0.5468 | 0.3472 | 0.0013 | 0.1151 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma790_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 0.9893 | 0.5550 | -0.0674 | -0.0002 | 0.1422 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma790_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 0.9520 | 0.5724 | -0.2437 | -0.0020 | 0.0987 | ok | RAN |
| SOLUSDT | 8 | `sma790_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 0.8946 | 0.5455 | -0.6683 | -0.0023 | 0.1313 | ok | RAN |
| ETHUSDT | 8 | `sma790_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.8515 | 0.5563 | -0.8226 | -0.0060 | 0.1062 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma790_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma790_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma790_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma790_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma790_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma790_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
