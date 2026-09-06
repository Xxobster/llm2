# Autonomy public-indicator hunt gen 2241

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T173651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5160_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 1.7620 | 0.6613 | 1.7322 | 0.0113 | 0.0968 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5160_above_at_h` | one_head_filter_pi_star | 47 | 4.0853 | 1.5193 | 0.6170 | 1.1010 | 0.0086 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5160_below_at_h` | one_head_filter_pi_star | 307 | 25.1037 | 0.9555 | 0.5277 | -0.3424 | -0.0010 | 0.1336 | ok | RAN |
| SOLUSDT | 8 | `ema5160_below_at_h` | one_head_filter_pi_star | 315 | 25.7578 | 0.9484 | 0.5302 | -0.4007 | -0.0011 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5160_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.9623 | 0.5312 | -0.1740 | -0.0017 | 0.0938 | ok | RAN |
| ETHUSDT | 4 | `ema5160_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9431 | 0.5533 | -0.4856 | -0.0019 | 0.1326 | ok | RAN |
| ETHUSDT | 8 | `ema5160_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9416 | 0.5526 | -0.4872 | -0.0020 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema5160_above_at_h` | one_head_filter_pi_star | 38 | 11.0914 | 0.8907 | 0.5263 | -0.5963 | -0.0055 | 0.1579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5160_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5160_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
