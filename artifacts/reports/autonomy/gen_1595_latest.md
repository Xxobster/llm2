# Autonomy public-indicator hunt gen 1595

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T173335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma687_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1613 | 0.5879 | 0.9006 | 0.0047 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `sma687_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1021 | 0.5691 | 0.6138 | 0.0033 | 0.1934 | ok | RAN |
| SOLUSDT | 8 | `sma687_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.1237 | 0.5556 | 0.5861 | 0.0023 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `sma687_above_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.0809 | 0.5333 | 0.3640 | 0.0015 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma687_below_at_h` | one_head_filter_pi_star | 198 | 16.1077 | 0.9375 | 0.5657 | -0.3853 | -0.0013 | 0.1414 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma687_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.8630 | 0.5408 | -0.8753 | -0.0031 | 0.1327 | ok | RAN |
| ETHUSDT | 8 | `sma687_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.8967 | 0.5563 | -0.5478 | -0.0042 | 0.1197 | ok | RAN |
| ETHUSDT | 4 | `sma687_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.7999 | 0.5460 | -1.2002 | -0.0086 | 0.1034 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma687_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma687_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma687_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma687_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma687_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma687_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
