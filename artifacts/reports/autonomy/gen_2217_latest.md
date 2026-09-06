# Autonomy public-indicator hunt gen 2217

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T144418Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5100_above_at_h` | one_head_filter_pi_star | 47 | 3.8637 | 1.8730 | 0.6383 | 1.6038 | 0.0129 | 0.1277 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5100_above_at_h` | one_head_filter_pi_star | 60 | 4.9323 | 1.6626 | 0.6500 | 1.5272 | 0.0097 | 0.0833 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema5100_above_at_h` | one_head_filter_pi_star | 40 | 4.7004 | 1.1013 | 0.5750 | 0.3265 | 0.0046 | 0.1500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5100_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9802 | 0.5354 | -0.1541 | -0.0004 | 0.1292 | ok | RAN |
| SOLUSDT | 8 | `ema5100_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9774 | 0.5394 | -0.1777 | -0.0005 | 0.1303 | ok | RAN |
| ETHUSDT | 8 | `ema5100_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9558 | 0.5543 | -0.3618 | -0.0015 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `ema5100_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9507 | 0.5549 | -0.4083 | -0.0017 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5100_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.8107 | 0.5000 | -1.1081 | -0.0090 | 0.1500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5100_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5100_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
