# Autonomy public-indicator hunt gen 2265

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T202843Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5220_above_at_h` | one_head_filter_pi_star | 61 | 5.2407 | 1.6318 | 0.6557 | 1.5468 | 0.0098 | 0.1148 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5220_above_at_h` | one_head_filter_pi_star | 50 | 4.6359 | 1.5994 | 0.6200 | 1.3058 | 0.0094 | 0.1200 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5220_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9777 | 0.5394 | -0.1751 | -0.0005 | 0.1273 | ok | RAN |
| ETHUSDT | 8 | `ema5220_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9784 | 0.5591 | -0.1783 | -0.0007 | 0.1354 | ok | RAN |
| SOLUSDT | 8 | `ema5220_below_at_h` | one_head_filter_pi_star | 323 | 26.4120 | 0.9646 | 0.5325 | -0.2769 | -0.0007 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5220_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9059 | 0.5468 | -0.8193 | -0.0032 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `ema5220_above_at_h` | one_head_filter_pi_star | 39 | 11.7689 | 0.7571 | 0.4872 | -1.4723 | -0.0124 | 0.1282 | ok | RAN |
| ETHUSDT | 8 | `ema5220_above_at_h` | one_head_filter_pi_star | 50 | 14.5939 | 0.7279 | 0.4800 | -1.8269 | -0.0160 | 0.1800 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5220_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0496 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5220_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
