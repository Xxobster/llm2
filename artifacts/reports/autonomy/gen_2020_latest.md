# Autonomy public-indicator hunt gen 2020

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T112810Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1045_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1045_above_at_h` | one_head_filter_pi_star | 121 | 9.9452 | 1.2672 | 0.6198 | 1.1065 | 0.0046 | 0.1488 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1045_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.1063 | 0.5963 | 0.4563 | 0.0019 | 0.1376 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1045_above_at_h` | one_head_filter_pi_star | 129 | 10.6462 | 0.9983 | 0.5736 | -0.0077 | -0.0001 | 0.1240 | ok | RAN |
| SOLUSDT | 8 | `ema1045_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9636 | 0.5430 | -0.2530 | -0.0008 | 0.1289 | ok | RAN |
| SOLUSDT | 4 | `ema1045_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9587 | 0.5444 | -0.2899 | -0.0009 | 0.1313 | ok | RAN |
| ETHUSDT | 8 | `ema1045_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.9653 | 0.5535 | -0.2319 | -0.0011 | 0.1628 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1045_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 0.8906 | 0.5236 | -0.7987 | -0.0036 | 0.1502 | ok | RAN |
| ETHUSDT | 8 | `ema1045_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.8145 | 0.5214 | -0.8810 | -0.0082 | 0.1197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1045_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1045_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1045_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1045_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1045_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
