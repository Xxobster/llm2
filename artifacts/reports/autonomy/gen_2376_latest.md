# Autonomy public-indicator hunt gen 2376

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T104524Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5540_above_at_h` | one_head_filter_pi_star | 50 | 4.6946 | 2.6529 | 0.6800 | 2.5817 | 0.0178 | 0.1000 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5540_above_at_h` | one_head_filter_pi_star | 51 | 4.5631 | 1.8059 | 0.6078 | 1.6356 | 0.0115 | 0.1176 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5540_below_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 0.9738 | 0.5342 | -0.2041 | -0.0005 | 0.1273 | ok | RAN |
| ETHUSDT | 8 | `sma5540_below_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9829 | 0.5572 | -0.1375 | -0.0005 | 0.1295 | ok | RAN |
| SOLUSDT | 8 | `sma5540_below_at_h` | one_head_filter_pi_star | 310 | 25.2191 | 0.9677 | 0.5290 | -0.2466 | -0.0007 | 0.1355 | ok | RAN |
| ETHUSDT | 4 | `sma5540_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9660 | 0.5569 | -0.2816 | -0.0011 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5540_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.9147 | 0.5000 | -0.3712 | -0.0042 | 0.1667 | ok | RAN |
| ETHUSDT | 8 | `sma5540_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.7647 | 0.5000 | -1.2224 | -0.0129 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5540_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5540_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5540_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5540_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
