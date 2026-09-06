# Autonomy public-indicator hunt gen 2312

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T020738Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5380_above_at_h` | one_head_filter_pi_star | 46 | 3.9170 | 2.1800 | 0.6304 | 1.9341 | 0.0138 | 0.0870 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5380_above_at_h` | one_head_filter_pi_star | 60 | 5.1091 | 1.7185 | 0.6000 | 1.5952 | 0.0113 | 0.1167 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5380_above_at_h` | one_head_filter_pi_star | 28 | 8.1726 | 1.1185 | 0.5357 | 0.4615 | 0.0047 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5380_below_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9883 | 0.5410 | -0.0909 | -0.0002 | 0.1307 | ok | RAN |
| ETHUSDT | 8 | `sma5380_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9895 | 0.5575 | -0.0841 | -0.0003 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `sma5380_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9810 | 0.5588 | -0.1575 | -0.0006 | 0.1294 | ok | RAN |
| SOLUSDT | 8 | `sma5380_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 0.9312 | 0.5304 | -0.5189 | -0.0014 | 0.1385 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5380_above_at_h` | one_head_filter_pi_star | 38 | 5.3904 | 0.6113 | 0.4474 | -1.7439 | -0.0233 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5380_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5380_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
