# Autonomy public-indicator hunt gen 2123

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T010522Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma756_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.3309 | 0.6111 | 1.7724 | 0.0088 | 0.1778 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma756_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2029 | 0.5890 | 1.0716 | 0.0054 | 0.2025 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma756_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 0.9609 | 0.5161 | -0.1955 | -0.0008 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma756_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 0.9141 | 0.5197 | -0.4315 | -0.0018 | 0.1260 | ok | RAN |
| SOLUSDT | 8 | `sma756_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 0.9153 | 0.5446 | -0.5505 | -0.0019 | 0.1408 | ok | RAN |
| SOLUSDT | 4 | `sma756_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.8912 | 0.5468 | -0.6864 | -0.0024 | 0.1232 | ok | RAN |
| ETHUSDT | 8 | `sma756_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.9238 | 0.5630 | -0.3766 | -0.0031 | 0.1259 | ok | RAN |
| ETHUSDT | 4 | `sma756_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.8938 | 0.5613 | -0.5714 | -0.0045 | 0.1032 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma756_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma756_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma756_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma756_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma756_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma756_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
