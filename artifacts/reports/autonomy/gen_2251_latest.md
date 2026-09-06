# Autonomy public-indicator hunt gen 2251

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T184644Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma773_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1596 | 0.5806 | 0.9193 | 0.0045 | 0.1774 | ok | RAN |
| ETHUSDT | 8 | `sma773_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1358 | 0.5843 | 0.7846 | 0.0041 | 0.1807 | ok | RAN |
| SOLUSDT | 8 | `sma773_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0966 | 0.5547 | 0.4476 | 0.0018 | 0.1172 | ok | RAN |
| SOLUSDT | 4 | `sma773_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.0159 | 0.5274 | 0.0816 | 0.0003 | 0.1233 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma773_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9328 | 0.5635 | -0.4159 | -0.0015 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma773_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 0.9144 | 0.5417 | -0.5577 | -0.0018 | 0.1296 | ok | RAN |
| ETHUSDT | 8 | `sma773_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 0.8771 | 0.5556 | -0.6077 | -0.0050 | 0.1032 | ok | RAN |
| ETHUSDT | 4 | `sma773_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 0.8380 | 0.5541 | -0.8862 | -0.0067 | 0.1083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma773_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma773_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma773_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma773_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma773_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma773_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
