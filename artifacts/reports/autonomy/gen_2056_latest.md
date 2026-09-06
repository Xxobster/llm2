# Autonomy public-indicator hunt gen 2056

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T160908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4740_above_at_h` | one_head_filter_pi_star | 60 | 5.2914 | 1.4073 | 0.5833 | 1.0618 | 0.0068 | 0.1167 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4740_above_at_h` | one_head_filter_pi_star | 51 | 4.2835 | 1.4780 | 0.5686 | 0.9980 | 0.0067 | 0.0784 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma4740_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 0.9881 | 0.5437 | -0.0892 | -0.0002 | 0.1359 | ok | RAN |
| ETHUSDT | 8 | `sma4740_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9866 | 0.5575 | -0.1071 | -0.0004 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `sma4740_below_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 0.9670 | 0.5387 | -0.2521 | -0.0007 | 0.1387 | ok | RAN |
| ETHUSDT | 4 | `sma4740_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9572 | 0.5529 | -0.3458 | -0.0014 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4740_above_at_h` | one_head_filter_pi_star | 41 | 12.0975 | 0.6612 | 0.4634 | -2.1433 | -0.0204 | 0.1220 | ok | RAN |
| ETHUSDT | 4 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
