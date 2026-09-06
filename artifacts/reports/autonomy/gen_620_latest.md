# Autonomy public-indicator hunt gen 620

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T014808Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema535_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 2.1004 | 0.6950 | 4.7099 | 0.0244 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema535_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9356 | 0.6900 | 4.0636 | 0.0223 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema535_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8281 | 0.6615 | 3.5121 | 0.0124 | 0.3487 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema535_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7597 | 0.6485 | 3.3945 | 0.0113 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema535_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.6392 | 0.6257 | 2.8046 | 0.0096 | 0.2849 | ok | RAN |
| SOLUSDT | 8 | `ema535_above_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.5191 | 0.6024 | 2.2650 | 0.0081 | 0.2892 | ok | RAN |
| ETHUSDT | 8 | `ema535_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1680 | 0.6012 | 0.8173 | 0.0062 | 0.2025 | ok | RAN |
| ETHUSDT | 4 | `ema535_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.0747 | 0.5848 | 0.3921 | 0.0029 | 0.2105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema535_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema535_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema535_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema535_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema535_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema535_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
