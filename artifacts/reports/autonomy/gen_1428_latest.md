# Autonomy public-indicator hunt gen 1428

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T132731Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema962_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.9352 | 0.6636 | 4.2128 | 0.0208 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema962_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.7672 | 0.6540 | 3.7005 | 0.0182 | 0.3418 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema962_below_at_h` | one_head_filter_pi_star | 226 | 18.4802 | 1.8187 | 0.6549 | 3.7959 | 0.0127 | 0.3142 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema962_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.3352 | 0.6144 | 1.5242 | 0.0118 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `ema962_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.6939 | 0.6349 | 3.4895 | 0.0110 | 0.2937 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema962_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 1.2867 | 0.5984 | 1.2093 | 0.0105 | 0.2295 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema962_above_at_h` | one_head_filter_pi_star | 126 | 10.4722 | 1.5953 | 0.6349 | 2.2473 | 0.0093 | 0.3254 | ok | RAN |
| SOLUSDT | 8 | `ema962_above_at_h` | one_head_filter_pi_star | 119 | 9.7586 | 1.5241 | 0.6218 | 1.9501 | 0.0080 | 0.3025 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema962_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema962_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema962_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema962_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema962_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema962_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
