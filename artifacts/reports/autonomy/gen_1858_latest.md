# Autonomy public-indicator hunt gen 1858

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T193651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1712_pos_at_h` | one_head_filter_pi_star | 13 | 4.1142 | 1.2506 | 0.6154 | 0.7375 | 0.0101 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret1712_pos_at_h` | one_head_filter_pi_star | 20 | 1.9470 | 1.4600 | 0.6500 | 0.7428 | 0.0095 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1712_pos_at_h` | one_head_filter_pi_star | 20 | 1.7005 | 1.5970 | 0.6500 | 0.9427 | 0.0086 | 0.1500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1712_neg_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 0.9665 | 0.5348 | -0.2560 | -0.0007 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `ret1712_neg_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 0.9646 | 0.5399 | -0.2669 | -0.0007 | 0.1246 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1712_neg_at_h` | one_head_filter_pi_star | 361 | 29.3681 | 0.9402 | 0.5568 | -0.5096 | -0.0020 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `ret1712_neg_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 0.9162 | 0.5506 | -0.7395 | -0.0028 | 0.1320 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1712_pos_at_h` | one_head_filter_pi_star | 17 | 5.2980 | 0.6296 | 0.4118 | -1.4511 | -0.0238 | 0.1765 | ok | RAN |
| BTCUSDT | 8 | `ret1712_pos_at_h` | one_head_filter_pi_star | 12 | 2.2038 | 0.3560 | 0.2500 | -1.9427 | -0.0883 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1712_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1712_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1712_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1712_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1712_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
