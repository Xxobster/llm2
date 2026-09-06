# Autonomy public-indicator hunt gen 2409

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T145352Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5580_above_at_h` | one_head_filter_pi_star | 51 | 4.3816 | 1.7039 | 0.6275 | 1.4572 | 0.0098 | 0.1373 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5580_above_at_h` | one_head_filter_pi_star | 53 | 4.9140 | 1.5000 | 0.6038 | 1.1714 | 0.0077 | 0.0943 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5580_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9802 | 0.5355 | -0.1520 | -0.0004 | 0.1290 | ok | RAN |
| SOLUSDT | 4 | `ema5580_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9435 | 0.5307 | -0.4495 | -0.0012 | 0.1288 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5580_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9456 | 0.5522 | -0.4463 | -0.0018 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `ema5580_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9382 | 0.5513 | -0.5214 | -0.0021 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `ema5580_above_at_h` | one_head_filter_pi_star | 41 | 12.3724 | 0.7190 | 0.4878 | -1.6978 | -0.0142 | 0.1220 | ok | RAN |
| ETHUSDT | 8 | `ema5580_above_at_h` | one_head_filter_pi_star | 39 | 11.5074 | 0.7102 | 0.4615 | -1.5779 | -0.0153 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5580_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.6195 | 0.3333 | -0.9018 | -0.0470 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5580_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0628 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
