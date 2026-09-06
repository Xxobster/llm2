# Autonomy public-indicator hunt gen 1923

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T012946Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma730_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2079 | 0.5814 | 1.1201 | 0.0057 | 0.1977 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma730_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.1704 | 0.5610 | 0.7464 | 0.0030 | 0.1057 | ok | RAN |
| ETHUSDT | 8 | `sma730_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.0220 | 0.5598 | 0.1401 | 0.0007 | 0.1739 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma730_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 0.9775 | 0.5280 | -0.1088 | -0.0004 | 0.1280 | ok | RAN |
| SOLUSDT | 4 | `sma730_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9519 | 0.5625 | -0.2909 | -0.0010 | 0.1354 | ok | RAN |
| SOLUSDT | 8 | `sma730_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.9337 | 0.5567 | -0.4064 | -0.0014 | 0.1392 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma730_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 0.9119 | 0.5603 | -0.4401 | -0.0035 | 0.1135 | ok | RAN |
| ETHUSDT | 8 | `sma730_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.8301 | 0.5486 | -0.9381 | -0.0071 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma730_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma730_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma730_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma730_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma730_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma730_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
