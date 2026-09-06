# Autonomy public-indicator hunt gen 1729

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T075236Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3880_above_at_h` | one_head_filter_pi_star | 82 | 6.7255 | 1.9131 | 0.6707 | 2.2259 | 0.0108 | 0.1098 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3880_above_at_h` | one_head_filter_pi_star | 74 | 6.0694 | 1.8181 | 0.6622 | 1.8933 | 0.0106 | 0.0946 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3880_below_at_h` | one_head_filter_pi_star | 295 | 24.1224 | 1.0169 | 0.5322 | 0.1231 | 0.0003 | 0.1322 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema3880_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.0021 | 0.5338 | 0.0154 | 0.0000 | 0.1423 | ok | RAN |
| ETHUSDT | 4 | `ema3880_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9783 | 0.5587 | -0.1798 | -0.0007 | 0.1347 | ok | RAN |
| ETHUSDT | 8 | `ema3880_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9532 | 0.5546 | -0.3807 | -0.0015 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3880_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.8853 | 0.5143 | -0.5526 | -0.0055 | 0.1714 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
