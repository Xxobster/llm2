# Autonomy public-indicator hunt gen 1745

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T092106Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3920_above_at_h` | one_head_filter_pi_star | 88 | 7.2177 | 1.6201 | 0.6364 | 1.7382 | 0.0082 | 0.1136 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3920_above_at_h` | one_head_filter_pi_star | 100 | 8.2019 | 1.3241 | 0.6000 | 1.0985 | 0.0049 | 0.0900 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3920_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.0238 | 0.5409 | 0.1680 | 0.0005 | 0.1388 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema3920_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 0.9820 | 0.5267 | -0.1334 | -0.0004 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `ema3920_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9872 | 0.5587 | -0.1046 | -0.0004 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema3920_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9611 | 0.5539 | -0.3174 | -0.0013 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3920_above_at_h` | one_head_filter_pi_star | 33 | 9.9583 | 0.9239 | 0.5152 | -0.3453 | -0.0034 | 0.1818 | ok | RAN |
| ETHUSDT | 4 | `ema3920_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.8813 | 0.5185 | -0.4890 | -0.0056 | 0.1481 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3920_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3920_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
