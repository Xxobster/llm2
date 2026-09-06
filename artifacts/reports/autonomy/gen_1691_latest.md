# Autonomy public-indicator hunt gen 1691

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T035428Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma699_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1278 | 0.5749 | 0.7184 | 0.0036 | 0.1737 | ok | RAN |
| SOLUSDT | 8 | `sma699_above_at_h` | one_head_filter_pi_star | 112 | 9.1846 | 1.1986 | 0.5625 | 0.8241 | 0.0035 | 0.1339 | ok | RAN |
| ETHUSDT | 8 | `sma699_below_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1098 | 0.5714 | 0.6267 | 0.0033 | 0.1964 | ok | RAN |
| SOLUSDT | 4 | `sma699_above_at_h` | one_head_filter_pi_star | 116 | 9.5126 | 1.1864 | 0.5517 | 0.8065 | 0.0033 | 0.1121 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma699_below_at_h` | one_head_filter_pi_star | 199 | 16.1890 | 0.9421 | 0.5528 | -0.3580 | -0.0012 | 0.1407 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma699_below_at_h` | one_head_filter_pi_star | 195 | 15.8636 | 0.9066 | 0.5487 | -0.5941 | -0.0020 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `sma699_above_at_h` | one_head_filter_pi_star | 129 | 10.6036 | 0.9366 | 0.5659 | -0.3083 | -0.0026 | 0.1163 | ok | RAN |
| ETHUSDT | 8 | `sma699_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8921 | 0.5578 | -0.5817 | -0.0043 | 0.1088 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma699_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma699_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma699_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma699_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma699_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma699_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
