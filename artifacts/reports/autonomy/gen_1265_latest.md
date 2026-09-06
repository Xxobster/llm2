# Autonomy public-indicator hunt gen 1265

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T164726Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2720_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.6123 | 0.6437 | 3.6294 | 0.0162 | 0.3114 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2720_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5667 | 0.6382 | 3.4736 | 0.0153 | 0.3059 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2720_below_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.9540 | 0.6642 | 4.5334 | 0.0140 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2720_below_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.8165 | 0.6493 | 4.0644 | 0.0124 | 0.3321 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2720_above_at_h` | one_head_filter_pi_star | 87 | 7.1511 | 1.8312 | 0.6667 | 2.2840 | 0.0110 | 0.2414 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2720_above_at_h` | one_head_filter_pi_star | 103 | 8.4658 | 1.4920 | 0.6311 | 1.6540 | 0.0079 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2720_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.8354 | 0.4815 | -0.7347 | -0.0065 | 0.1481 | ok | RAN |
| BTCUSDT | 8 | `ema2720_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.7376 | 0.3684 | -0.5246 | -0.0260 | 0.1053 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
