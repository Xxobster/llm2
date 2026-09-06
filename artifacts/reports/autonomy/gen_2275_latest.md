# Autonomy public-indicator hunt gen 2275

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T214107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma776_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.2502 | 0.5928 | 1.3177 | 0.0065 | 0.1856 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma776_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2022 | 0.5722 | 1.1405 | 0.0058 | 0.1833 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma776_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.2880 | 0.5932 | 1.1736 | 0.0049 | 0.1271 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma776_above_at_h` | one_head_filter_pi_star | 143 | 11.6603 | 1.0946 | 0.5524 | 0.4593 | 0.0017 | 0.1189 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma776_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 0.9730 | 0.5525 | -0.1729 | -0.0006 | 0.1370 | ok | RAN |
| SOLUSDT | 4 | `sma776_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9515 | 0.5534 | -0.3050 | -0.0010 | 0.1408 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma776_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 0.8882 | 0.5603 | -0.5686 | -0.0046 | 0.1206 | ok | RAN |
| ETHUSDT | 4 | `sma776_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.8389 | 0.5563 | -0.8285 | -0.0068 | 0.1056 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma776_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma776_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma776_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma776_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma776_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma776_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
