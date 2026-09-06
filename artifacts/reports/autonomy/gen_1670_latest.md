# Autonomy public-indicator hunt gen 1670

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T005739Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma438_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1624 | 0.5955 | 0.9311 | 0.0050 | 0.1966 | ok | RAN |
| ETHUSDT | 8 | `wma438_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1552 | 0.5851 | 0.9216 | 0.0047 | 0.1915 | ok | RAN |
| SOLUSDT | 8 | `wma438_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.1261 | 0.5758 | 0.6571 | 0.0025 | 0.1576 | ok | RAN |
| SOLUSDT | 4 | `wma438_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 1.0549 | 0.5783 | 0.3019 | 0.0011 | 0.1566 | ok | RAN |
| SOLUSDT | 4 | `wma438_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0559 | 0.5440 | 0.3129 | 0.0010 | 0.1044 | ok | RAN |
| SOLUSDT | 8 | `wma438_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.0264 | 0.5506 | 0.1502 | 0.0005 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma438_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8126 | 0.5269 | -1.2160 | -0.0076 | 0.0968 | ok | RAN |
| ETHUSDT | 8 | `wma438_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8062 | 0.5301 | -1.2342 | -0.0080 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma438_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma438_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma438_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma438_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma438_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma438_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
