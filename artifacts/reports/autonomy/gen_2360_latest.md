# Autonomy public-indicator hunt gen 2360

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T082341Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5500_above_at_h` | one_head_filter_pi_star | 58 | 5.4457 | 2.1197 | 0.6724 | 2.2188 | 0.0142 | 0.1207 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5500_above_at_h` | one_head_filter_pi_star | 51 | 4.3428 | 1.8395 | 0.6078 | 1.6434 | 0.0131 | 0.1176 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5500_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0126 | 0.5625 | 0.1001 | 0.0004 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5500_below_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 0.9660 | 0.5314 | -0.2634 | -0.0007 | 0.1289 | ok | RAN |
| SOLUSDT | 8 | `sma5500_below_at_h` | one_head_filter_pi_star | 309 | 25.2672 | 0.9619 | 0.5340 | -0.2902 | -0.0008 | 0.1359 | ok | RAN |
| ETHUSDT | 4 | `sma5500_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9757 | 0.5575 | -0.1968 | -0.0008 | 0.1298 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5500_above_at_h` | one_head_filter_pi_star | 39 | 11.7689 | 0.7373 | 0.4872 | -1.4803 | -0.0146 | 0.1795 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5500_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.6177 | 0.4412 | -2.1060 | -0.0221 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5500_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5500_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5500_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5500_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5500_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
