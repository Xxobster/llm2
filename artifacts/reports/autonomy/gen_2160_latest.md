# Autonomy public-indicator hunt gen 2160

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T064139Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5000_above_at_h` | one_head_filter_pi_star | 59 | 4.9554 | 2.6555 | 0.6441 | 2.5934 | 0.0159 | 0.1017 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5000_above_at_h` | one_head_filter_pi_star | 45 | 3.8319 | 1.8513 | 0.6000 | 1.5100 | 0.0112 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5000_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.0023 | 0.5599 | 0.0185 | 0.0001 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `sma5000_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 0.9959 | 0.5362 | -0.0301 | -0.0001 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `sma5000_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9883 | 0.5575 | -0.0932 | -0.0004 | 0.1357 | ok | RAN |
| SOLUSDT | 8 | `sma5000_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 0.9674 | 0.5397 | -0.2432 | -0.0007 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5000_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.7820 | 0.5000 | -1.3413 | -0.0122 | 0.1579 | ok | RAN |
| ETHUSDT | 8 | `sma5000_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.7726 | 0.5000 | -1.1707 | -0.0123 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5000_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5000_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
