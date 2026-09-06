# Autonomy public-indicator hunt gen 1332

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T231854Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema948_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8947 | 0.6726 | 4.0656 | 0.0203 | 0.3453 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema948_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.8359 | 0.6652 | 3.9844 | 0.0194 | 0.3391 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema948_above_at_h` | one_head_filter_pi_star | 136 | 11.2239 | 1.3661 | 0.6176 | 1.5875 | 0.0128 | 0.2206 | ok | RAN |
| SOLUSDT | 4 | `ema948_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7689 | 0.6471 | 3.7864 | 0.0120 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema948_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7170 | 0.6434 | 3.5627 | 0.0115 | 0.2992 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema948_above_at_h` | one_head_filter_pi_star | 116 | 9.5126 | 1.7545 | 0.6466 | 2.4498 | 0.0108 | 0.3276 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema948_above_at_h` | one_head_filter_pi_star | 140 | 11.5540 | 1.2404 | 0.6000 | 1.0987 | 0.0091 | 0.2214 | ok | RAN |
| SOLUSDT | 8 | `ema948_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.5228 | 0.6167 | 1.9252 | 0.0079 | 0.3083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema948_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema948_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema948_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema948_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema948_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema948_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
