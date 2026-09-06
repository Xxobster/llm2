# Autonomy public-indicator hunt gen 2075

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T184558Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma750_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1620 | 0.5780 | 0.9193 | 0.0047 | 0.1908 | ok | RAN |
| ETHUSDT | 8 | `sma750_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1398 | 0.5706 | 0.7865 | 0.0043 | 0.1808 | ok | RAN |
| SOLUSDT | 8 | `sma750_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.1071 | 0.5538 | 0.4908 | 0.0020 | 0.1231 | ok | RAN |
| SOLUSDT | 4 | `sma750_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0730 | 0.5515 | 0.3501 | 0.0014 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma750_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 0.9388 | 0.5550 | -0.3792 | -0.0013 | 0.1300 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma750_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.8896 | 0.5476 | -0.7066 | -0.0024 | 0.1238 | ok | RAN |
| ETHUSDT | 8 | `sma750_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 0.8995 | 0.5746 | -0.5015 | -0.0042 | 0.1194 | ok | RAN |
| ETHUSDT | 4 | `sma750_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 0.7863 | 0.5359 | -1.1908 | -0.0097 | 0.1046 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma750_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma750_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma750_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma750_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
