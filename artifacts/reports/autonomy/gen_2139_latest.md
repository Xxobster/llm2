# Autonomy public-indicator hunt gen 2139

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T030145Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma758_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.3125 | 0.5951 | 1.4874 | 0.0082 | 0.1902 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma758_above_at_h` | one_head_filter_pi_star | 114 | 9.3486 | 1.2302 | 0.5877 | 0.9181 | 0.0040 | 0.1316 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma758_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.0956 | 0.5746 | 0.5705 | 0.0029 | 0.1768 | ok | RAN |
| SOLUSDT | 4 | `sma758_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.0830 | 0.5530 | 0.3887 | 0.0015 | 0.1212 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma758_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9437 | 0.5433 | -0.3559 | -0.0012 | 0.1346 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma758_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9051 | 0.5482 | -0.5830 | -0.0021 | 0.1269 | ok | RAN |
| ETHUSDT | 8 | `sma758_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.9023 | 0.5647 | -0.5488 | -0.0038 | 0.1059 | ok | RAN |
| ETHUSDT | 4 | `sma758_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 0.8886 | 0.5660 | -0.5992 | -0.0045 | 0.1006 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma758_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma758_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma758_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma758_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma758_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma758_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
