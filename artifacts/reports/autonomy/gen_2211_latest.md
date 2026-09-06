# Autonomy public-indicator hunt gen 2211

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T135707Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma768_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.2417 | 0.6056 | 1.2851 | 0.0066 | 0.1833 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma768_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1993 | 0.5739 | 1.0912 | 0.0057 | 0.1818 | ok | RAN |
| SOLUSDT | 8 | `sma768_above_at_h` | one_head_filter_pi_star | 118 | 9.8073 | 1.2305 | 0.5932 | 0.9475 | 0.0042 | 0.1186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma768_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 0.9962 | 0.5435 | -0.0191 | -0.0001 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma768_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9092 | 0.5473 | -0.5732 | -0.0019 | 0.1343 | ok | RAN |
| SOLUSDT | 4 | `sma768_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 0.8655 | 0.5415 | -0.8620 | -0.0029 | 0.1317 | ok | RAN |
| ETHUSDT | 8 | `sma768_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.8811 | 0.5556 | -0.6709 | -0.0049 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `sma768_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.7665 | 0.5316 | -1.3365 | -0.0103 | 0.1076 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma768_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma768_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma768_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma768_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma768_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma768_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
