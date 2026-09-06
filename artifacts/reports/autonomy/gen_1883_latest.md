# Autonomy public-indicator hunt gen 1883

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T215307Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma725_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2182 | 0.5862 | 1.2013 | 0.0061 | 0.2011 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma725_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1895 | 0.5756 | 1.0518 | 0.0055 | 0.1919 | ok | RAN |
| SOLUSDT | 4 | `sma725_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.0891 | 0.5435 | 0.4256 | 0.0017 | 0.1232 | ok | RAN |
| SOLUSDT | 8 | `sma725_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0160 | 0.5407 | 0.0785 | 0.0003 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma725_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9583 | 0.5488 | -0.2655 | -0.0009 | 0.1302 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma725_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 0.9156 | 0.5602 | -0.5174 | -0.0019 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `sma725_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8967 | 0.5782 | -0.5378 | -0.0042 | 0.1088 | ok | RAN |
| ETHUSDT | 8 | `sma725_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8785 | 0.5548 | -0.6549 | -0.0050 | 0.1096 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma725_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma725_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
