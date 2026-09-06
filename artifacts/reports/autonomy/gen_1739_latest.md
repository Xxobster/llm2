# Autonomy public-indicator hunt gen 1739

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T084904Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma706_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2554 | 0.5951 | 1.3478 | 0.0070 | 0.1963 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma706_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.1185 | 0.5455 | 0.5370 | 0.0022 | 0.1157 | ok | RAN |
| ETHUSDT | 8 | `sma706_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.0608 | 0.5764 | 0.3902 | 0.0019 | 0.1675 | ok | RAN |
| SOLUSDT | 8 | `sma706_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.0656 | 0.5420 | 0.3182 | 0.0012 | 0.1221 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma706_below_at_h` | one_head_filter_pi_star | 213 | 17.3280 | 1.0009 | 0.5728 | 0.0057 | 0.0000 | 0.1268 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma706_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9122 | 0.5459 | -0.5475 | -0.0019 | 0.1378 | ok | RAN |
| ETHUSDT | 8 | `sma706_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 0.9405 | 0.5769 | -0.2991 | -0.0023 | 0.1000 | ok | RAN |
| ETHUSDT | 4 | `sma706_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8674 | 0.5479 | -0.6945 | -0.0054 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma706_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0658 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma706_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma706_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma706_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma706_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma706_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
