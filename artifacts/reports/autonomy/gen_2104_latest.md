# Autonomy public-indicator hunt gen 2104

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T224624Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma4860_above_at_h` | one_head_filter_pi_star | 44 | 3.7467 | 1.7521 | 0.5909 | 1.3663 | 0.0103 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma4860_above_at_h` | one_head_filter_pi_star | 55 | 5.0864 | 1.5796 | 0.6000 | 1.3266 | 0.0089 | 0.1091 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma4860_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0115 | 0.5612 | 0.0932 | 0.0004 | 0.1373 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma4860_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 0.9971 | 0.5439 | -0.0210 | -0.0001 | 0.1385 | ok | RAN |
| SOLUSDT | 4 | `sma4860_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9802 | 0.5419 | -0.1519 | -0.0004 | 0.1355 | ok | RAN |
| ETHUSDT | 8 | `sma4860_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9618 | 0.5529 | -0.3105 | -0.0012 | 0.1360 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4860_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.7442 | 0.4865 | -1.4223 | -0.0136 | 0.1351 | ok | RAN |
| ETHUSDT | 8 | `sma4860_above_at_h` | one_head_filter_pi_star | 37 | 11.1653 | 0.7318 | 0.4865 | -1.6045 | -0.0159 | 0.1351 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
