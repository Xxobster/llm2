# Autonomy public-indicator hunt gen 1659

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T000021Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma695_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.3300 | 0.6124 | 1.7377 | 0.0090 | 0.1798 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma695_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1162 | 0.5754 | 0.6670 | 0.0036 | 0.1899 | ok | RAN |
| SOLUSDT | 8 | `sma695_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.2045 | 0.5652 | 0.8543 | 0.0036 | 0.1304 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma695_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.0893 | 0.5405 | 0.4360 | 0.0017 | 0.1149 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma695_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9030 | 0.5396 | -0.6155 | -0.0021 | 0.1386 | ok | RAN |
| ETHUSDT | 8 | `sma695_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 0.9399 | 0.5694 | -0.3150 | -0.0023 | 0.1111 | ok | RAN |
| SOLUSDT | 8 | `sma695_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 0.8923 | 0.5463 | -0.6914 | -0.0024 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `sma695_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 0.9162 | 0.5515 | -0.4199 | -0.0033 | 0.1103 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma695_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma695_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma695_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma695_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma695_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
