# Autonomy public-indicator hunt gen 1997

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T085143Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret329_neg_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2822 | 0.6049 | 1.4468 | 0.0082 | 0.2037 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret329_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2213 | 0.5896 | 1.2141 | 0.0066 | 0.1908 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret329_pos_at_h` | one_head_filter_pi_star | 177 | 14.5149 | 1.2462 | 0.5650 | 1.2273 | 0.0042 | 0.1073 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret329_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.1427 | 0.5549 | 0.7266 | 0.0025 | 0.1037 | ok | RAN |
| SOLUSDT | 8 | `ret329_neg_at_h` | one_head_filter_pi_star | 192 | 15.6196 | 1.0084 | 0.5729 | 0.0512 | 0.0002 | 0.1458 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret329_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.8984 | 0.5487 | -0.6589 | -0.0023 | 0.1436 | ok | RAN |
| ETHUSDT | 4 | `ret329_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 0.9346 | 0.5680 | -0.3703 | -0.0025 | 0.1006 | ok | RAN |
| ETHUSDT | 8 | `ret329_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 0.7666 | 0.5319 | -1.4951 | -0.0102 | 0.1011 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret329_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4385 | 0.2222 | -1.2856 | -0.0664 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret329_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4309 | 0.2632 | -1.3328 | -0.0671 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret329_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret329_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret329_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret329_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
