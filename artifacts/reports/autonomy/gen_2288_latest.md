# Autonomy public-indicator hunt gen 2288

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T231442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5320_above_at_h` | one_head_filter_pi_star | 47 | 4.0022 | 2.4039 | 0.6596 | 2.1670 | 0.0171 | 0.0851 | ok | RAN |
| SOLUSDT | 8 | `sma5320_above_at_h` | one_head_filter_pi_star | 55 | 4.6834 | 2.1192 | 0.6364 | 2.0191 | 0.0141 | 0.1091 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5320_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.0001 | 0.5599 | 0.0011 | 0.0000 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `sma5320_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 0.9785 | 0.5413 | -0.1673 | -0.0004 | 0.1284 | ok | RAN |
| ETHUSDT | 4 | `sma5320_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9743 | 0.5569 | -0.2100 | -0.0008 | 0.1317 | ok | RAN |
| SOLUSDT | 8 | `sma5320_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9427 | 0.5241 | -0.4413 | -0.0012 | 0.1286 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5320_above_at_h` | one_head_filter_pi_star | 36 | 5.1067 | 0.6753 | 0.4444 | -1.2439 | -0.0177 | 0.1389 | ok | RAN |
| ETHUSDT | 8 | `sma5320_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 0.6362 | 0.4444 | -2.2920 | -0.0213 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
