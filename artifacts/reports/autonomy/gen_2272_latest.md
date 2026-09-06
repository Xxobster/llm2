# Autonomy public-indicator hunt gen 2272

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T211933Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5280_above_at_h` | one_head_filter_pi_star | 48 | 4.0873 | 2.1345 | 0.6458 | 1.9463 | 0.0145 | 0.1250 | ok | RAN |
| SOLUSDT | 8 | `sma5280_above_at_h` | one_head_filter_pi_star | 58 | 4.9388 | 1.9817 | 0.6379 | 1.9295 | 0.0126 | 0.1034 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5280_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.0076 | 0.5643 | 0.0619 | 0.0002 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `sma5280_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.0045 | 0.5608 | 0.0367 | 0.0001 | 0.1276 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5280_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 0.9900 | 0.5399 | -0.0778 | -0.0002 | 0.1288 | ok | RAN |
| SOLUSDT | 8 | `sma5280_below_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 0.9476 | 0.5353 | -0.4021 | -0.0011 | 0.1282 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5280_above_at_h` | one_head_filter_pi_star | 33 | 9.7370 | 0.9108 | 0.5152 | -0.4256 | -0.0043 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `sma5280_above_at_h` | one_head_filter_pi_star | 35 | 10.3272 | 0.7225 | 0.4857 | -1.4885 | -0.0162 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
