# Autonomy public-indicator hunt gen 2201

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T124010Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5060_above_at_h` | one_head_filter_pi_star | 74 | 6.0832 | 1.7225 | 0.6351 | 1.8217 | 0.0109 | 0.0946 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema5060_above_at_h` | one_head_filter_pi_star | 52 | 4.4675 | 1.5489 | 0.5962 | 1.1749 | 0.0088 | 0.0962 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema5060_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9837 | 0.5594 | -0.1334 | -0.0005 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `ema5060_below_at_h` | one_head_filter_pi_star | 305 | 24.9401 | 0.9687 | 0.5311 | -0.2364 | -0.0006 | 0.1410 | ok | RAN |
| SOLUSDT | 4 | `ema5060_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9368 | 0.5285 | -0.5025 | -0.0013 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5060_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9443 | 0.5536 | -0.4695 | -0.0019 | 0.1362 | ok | RAN |
| ETHUSDT | 4 | `ema5060_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.9480 | 0.5250 | -0.2828 | -0.0023 | 0.1500 | ok | RAN |
| ETHUSDT | 8 | `ema5060_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.8837 | 0.5250 | -0.6964 | -0.0058 | 0.1500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5060_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5060_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
