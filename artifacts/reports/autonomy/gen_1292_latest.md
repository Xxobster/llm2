# Autonomy public-indicator hunt gen 1292

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T192426Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema942_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.8028 | 0.6569 | 3.8338 | 0.0192 | 0.3389 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema942_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.7441 | 0.6622 | 3.5943 | 0.0184 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema942_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.7025 | 0.6411 | 3.5016 | 0.0112 | 0.3105 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema942_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.6952 | 0.6429 | 3.5217 | 0.0111 | 0.3016 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema942_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.5778 | 0.6281 | 2.1106 | 0.0088 | 0.3223 | ok | RAN |
| SOLUSDT | 8 | `ema942_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.5459 | 0.6179 | 2.0582 | 0.0084 | 0.3089 | ok | RAN |
| ETHUSDT | 4 | `ema942_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.1770 | 0.5870 | 0.8246 | 0.0068 | 0.2246 | ok | RAN |
| ETHUSDT | 8 | `ema942_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 1.1694 | 0.5794 | 0.7582 | 0.0068 | 0.2381 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema942_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema942_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0521 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema942_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema942_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema942_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema942_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
