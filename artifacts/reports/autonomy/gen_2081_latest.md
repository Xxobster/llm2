# Autonomy public-indicator hunt gen 2081

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T193221Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4760_above_at_h` | one_head_filter_pi_star | 27 | 2.3468 | 2.6616 | 0.7407 | 1.7584 | 0.0174 | 0.0741 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema4760_above_at_h` | one_head_filter_pi_star | 69 | 5.6722 | 1.8079 | 0.6667 | 1.8915 | 0.0111 | 0.1014 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema4760_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 1.0303 | 0.5588 | 0.1392 | 0.0014 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4760_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9870 | 0.5368 | -0.1006 | -0.0003 | 0.1288 | ok | RAN |
| SOLUSDT | 8 | `ema4760_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9871 | 0.5329 | -0.0967 | -0.0003 | 0.1382 | ok | RAN |
| ETHUSDT | 4 | `ema4760_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9698 | 0.5562 | -0.2395 | -0.0010 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4760_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9496 | 0.5552 | -0.4162 | -0.0017 | 0.1366 | ok | RAN |
| ETHUSDT | 8 | `ema4760_above_at_h` | one_head_filter_pi_star | 38 | 4.4654 | 0.7838 | 0.5000 | -0.7981 | -0.0116 | 0.1579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6281 | 0.3158 | -0.8186 | -0.0428 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4760_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
