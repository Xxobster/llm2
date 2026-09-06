# Autonomy public-indicator hunt gen 1642

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T220135Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1496_pos_at_h` | one_head_filter_pi_star | 19 | 1.6155 | 2.9828 | 0.7368 | 1.9531 | 0.0206 | 0.2105 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1496_pos_at_h` | one_head_filter_pi_star | 12 | 1.3629 | 1.9009 | 0.6667 | 1.0935 | 0.0136 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1496_neg_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.0161 | 0.5498 | 0.1239 | 0.0003 | 0.1360 | ok | RAN |
| SOLUSDT | 8 | `ret1496_neg_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.0047 | 0.5426 | 0.0353 | 0.0001 | 0.1262 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1496_neg_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 0.9306 | 0.5503 | -0.5612 | -0.0023 | 0.1384 | ok | RAN |
| ETHUSDT | 8 | `ret1496_neg_at_h` | one_head_filter_pi_star | 319 | 25.9513 | 0.9179 | 0.5455 | -0.6675 | -0.0027 | 0.1411 | ok | RAN |
| ETHUSDT | 8 | `ret1496_pos_at_h` | one_head_filter_pi_star | 12 | 1.4101 | 0.8631 | 0.5833 | -0.2654 | -0.0055 | 0.0833 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1496_pos_at_h` | one_head_filter_pi_star | 13 | 1.3052 | 0.6425 | 0.4615 | -0.7727 | -0.0168 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1496_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5104 | 0.2500 | -1.1382 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1496_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5085 | 0.2500 | -1.0265 | -0.0561 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1496_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1496_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1496_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1496_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
