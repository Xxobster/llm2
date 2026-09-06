# Autonomy public-indicator hunt gen 2491

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T001239Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma805_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.1643 | 0.5876 | 0.9614 | 0.0049 | 0.1701 | ok | RAN |
| ETHUSDT | 4 | `sma805_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1505 | 0.5833 | 0.8748 | 0.0043 | 0.1722 | ok | RAN |
| SOLUSDT | 8 | `sma805_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1213 | 0.5576 | 0.6338 | 0.0022 | 0.1091 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma805_above_at_h` | one_head_filter_pi_star | 135 | 11.0080 | 0.9740 | 0.5259 | -0.1282 | -0.0005 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `sma805_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9478 | 0.5490 | -0.3265 | -0.0011 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma805_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.8943 | 0.5446 | -0.6791 | -0.0024 | 0.1386 | ok | RAN |
| ETHUSDT | 4 | `sma805_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 0.8447 | 0.5338 | -0.7641 | -0.0065 | 0.1053 | ok | RAN |
| ETHUSDT | 8 | `sma805_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8129 | 0.5333 | -1.0633 | -0.0081 | 0.0970 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma805_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma805_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma805_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma805_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma805_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma805_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
