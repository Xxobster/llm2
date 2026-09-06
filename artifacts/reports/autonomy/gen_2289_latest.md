# Autonomy public-indicator hunt gen 2289

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T232210Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5280_above_at_h` | one_head_filter_pi_star | 47 | 4.3577 | 1.9570 | 0.6596 | 1.7174 | 0.0128 | 0.1277 | ok | RAN |
| SOLUSDT | 8 | `ema5280_above_at_h` | one_head_filter_pi_star | 58 | 4.7679 | 1.6215 | 0.6379 | 1.3449 | 0.0087 | 0.0862 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema5280_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9767 | 0.5591 | -0.1897 | -0.0008 | 0.1354 | ok | RAN |
| SOLUSDT | 4 | `ema5280_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9407 | 0.5263 | -0.4546 | -0.0013 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `ema5280_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9610 | 0.5562 | -0.3239 | -0.0013 | 0.1383 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema5280_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9156 | 0.5197 | -0.6602 | -0.0018 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema5280_above_at_h` | one_head_filter_pi_star | 40 | 4.7004 | 0.7905 | 0.5000 | -0.6842 | -0.0099 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema5280_above_at_h` | one_head_filter_pi_star | 45 | 5.2879 | 0.7324 | 0.4889 | -1.0711 | -0.0147 | 0.1333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5280_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5564 | 0.2778 | -0.9546 | -0.0512 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5280_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
