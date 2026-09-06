# Autonomy public-indicator hunt gen 1899

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T231918Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma727_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1641 | 0.5763 | 0.9440 | 0.0047 | 0.1864 | ok | RAN |
| ETHUSDT | 8 | `sma727_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1226 | 0.5730 | 0.7322 | 0.0037 | 0.1798 | ok | RAN |
| SOLUSDT | 8 | `sma727_above_at_h` | one_head_filter_pi_star | 119 | 9.8904 | 1.0481 | 0.5462 | 0.2230 | 0.0009 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `sma727_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.0196 | 0.5396 | 0.0970 | 0.0004 | 0.1151 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma727_below_at_h` | one_head_filter_pi_star | 207 | 16.8399 | 0.9033 | 0.5362 | -0.6191 | -0.0021 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `sma727_below_at_h` | one_head_filter_pi_star | 210 | 17.0839 | 0.8820 | 0.5381 | -0.7688 | -0.0025 | 0.1286 | ok | RAN |
| ETHUSDT | 4 | `sma727_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.8580 | 0.5481 | -0.7144 | -0.0058 | 0.0963 | ok | RAN |
| ETHUSDT | 8 | `sma727_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.8267 | 0.5475 | -1.0348 | -0.0072 | 0.1117 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma727_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma727_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma727_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma727_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma727_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma727_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
