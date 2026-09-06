# Autonomy public-indicator hunt gen 1683

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T024525Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma698_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1215 | 0.5682 | 0.6900 | 0.0037 | 0.1932 | ok | RAN |
| SOLUSDT | 8 | `sma698_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.1748 | 0.5652 | 0.7431 | 0.0031 | 0.1391 | ok | RAN |
| SOLUSDT | 4 | `sma698_above_at_h` | one_head_filter_pi_star | 125 | 10.2506 | 1.0887 | 0.5440 | 0.4006 | 0.0017 | 0.1200 | ok | RAN |
| ETHUSDT | 8 | `sma698_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.0050 | 0.5508 | 0.0318 | 0.0002 | 0.1711 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma698_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9565 | 0.5578 | -0.2653 | -0.0009 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma698_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 0.9219 | 0.5490 | -0.4935 | -0.0017 | 0.1324 | ok | RAN |
| ETHUSDT | 8 | `sma698_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 0.9050 | 0.5643 | -0.5006 | -0.0039 | 0.1214 | ok | RAN |
| ETHUSDT | 4 | `sma698_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 0.8704 | 0.5407 | -0.6684 | -0.0052 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma698_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma698_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0670 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma698_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma698_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma698_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma698_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
