# Autonomy public-indicator hunt gen 2481

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T230759Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5760_above_at_h` | one_head_filter_pi_star | 52 | 4.3777 | 1.7056 | 0.6346 | 1.4625 | 0.0095 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5760_above_at_h` | one_head_filter_pi_star | 43 | 3.9869 | 1.7268 | 0.6047 | 1.3918 | 0.0094 | 0.0930 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5760_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 1.0032 | 0.5411 | 0.0240 | 0.0001 | 0.1297 | ok | RAN |
| ETHUSDT | 4 | `ema5760_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9874 | 0.5585 | -0.1028 | -0.0004 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `ema5760_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9742 | 0.5394 | -0.2020 | -0.0005 | 0.1303 | ok | RAN |
| ETHUSDT | 8 | `ema5760_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9517 | 0.5552 | -0.3989 | -0.0016 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5760_above_at_h` | one_head_filter_pi_star | 42 | 11.3728 | 0.7551 | 0.4762 | -1.2782 | -0.0130 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `ema5760_above_at_h` | one_head_filter_pi_star | 43 | 7.3242 | 0.7148 | 0.4884 | -1.2829 | -0.0156 | 0.1628 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5760_above_at_h` | one_head_filter_pi_star | 22 | 1.8721 | 0.6170 | 0.3182 | -0.9116 | -0.0467 | 0.0455 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5760_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5440 | 0.3000 | -1.0991 | -0.0574 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
