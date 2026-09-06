# Autonomy public-indicator hunt gen 1947

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T035013Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma733_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2300 | 0.5930 | 1.2844 | 0.0062 | 0.1802 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma733_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.2583 | 0.5847 | 1.0643 | 0.0043 | 0.1102 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma733_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1373 | 0.5767 | 0.8156 | 0.0041 | 0.1746 | ok | RAN |
| SOLUSDT | 4 | `sma733_above_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.0634 | 0.5417 | 0.2912 | 0.0012 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma733_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9508 | 0.5510 | -0.2990 | -0.0010 | 0.1276 | ok | RAN |
| SOLUSDT | 8 | `sma733_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9340 | 0.5495 | -0.4134 | -0.0014 | 0.1287 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma733_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.9178 | 0.5742 | -0.4427 | -0.0032 | 0.1032 | ok | RAN |
| ETHUSDT | 4 | `sma733_above_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 0.8455 | 0.5503 | -0.8715 | -0.0065 | 0.1065 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma733_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma733_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4039 | 0.2105 | -1.4311 | -0.0694 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma733_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma733_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma733_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma733_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
