# Autonomy public-indicator hunt gen 1731

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T080448Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma705_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.2424 | 0.5826 | 1.0174 | 0.0041 | 0.1304 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma705_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1307 | 0.5783 | 0.7333 | 0.0039 | 0.1988 | ok | RAN |
| ETHUSDT | 4 | `sma705_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.1220 | 0.5767 | 0.6877 | 0.0036 | 0.1840 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma705_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 0.9967 | 0.5271 | -0.0157 | -0.0001 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `sma705_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9760 | 0.5607 | -0.1516 | -0.0005 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma705_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9157 | 0.5528 | -0.5284 | -0.0018 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `sma705_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 0.8890 | 0.5615 | -0.5748 | -0.0044 | 0.1077 | ok | RAN |
| ETHUSDT | 4 | `sma705_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8833 | 0.5507 | -0.5911 | -0.0047 | 0.1159 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma705_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma705_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma705_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma705_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma705_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
