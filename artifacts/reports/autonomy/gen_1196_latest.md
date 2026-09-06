# Autonomy public-indicator hunt gen 1196

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T095426Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema928_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.8566 | 0.6580 | 3.9525 | 0.0198 | 0.3420 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema928_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.7634 | 0.6620 | 3.5388 | 0.0187 | 0.3657 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema928_below_at_h` | one_head_filter_pi_star | 240 | 19.6250 | 1.7393 | 0.6417 | 3.5925 | 0.0116 | 0.3042 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema928_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.7171 | 0.6473 | 3.5500 | 0.0114 | 0.3071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema928_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6435 | 0.6400 | 2.3213 | 0.0094 | 0.2960 | ok | RAN |
| SOLUSDT | 4 | `ema928_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.5657 | 0.6218 | 2.0560 | 0.0087 | 0.3025 | ok | RAN |
| ETHUSDT | 8 | `ema928_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.1868 | 0.5971 | 0.8768 | 0.0072 | 0.2230 | ok | RAN |
| ETHUSDT | 4 | `ema928_above_at_h` | one_head_filter_pi_star | 135 | 11.0968 | 1.1238 | 0.5852 | 0.5910 | 0.0048 | 0.2074 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema928_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema928_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema928_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema928_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema928_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema928_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
