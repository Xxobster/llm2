# Autonomy public-indicator hunt gen 1803

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T144117Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma714_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.2164 | 0.5824 | 1.1901 | 0.0061 | 0.1882 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma714_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1781 | 0.5852 | 0.9914 | 0.0052 | 0.1818 | ok | RAN |
| SOLUSDT | 4 | `sma714_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.0449 | 0.5372 | 0.2058 | 0.0009 | 0.1157 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma714_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 0.9876 | 0.5242 | -0.0599 | -0.0002 | 0.1290 | ok | RAN |
| SOLUSDT | 4 | `sma714_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9406 | 0.5528 | -0.3698 | -0.0012 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `sma714_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 0.9611 | 0.5745 | -0.1924 | -0.0015 | 0.1064 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma714_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.8982 | 0.5446 | -0.6478 | -0.0022 | 0.1337 | ok | RAN |
| ETHUSDT | 8 | `sma714_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8838 | 0.5578 | -0.6341 | -0.0049 | 0.1156 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma714_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma714_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma714_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma714_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma714_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma714_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
