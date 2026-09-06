# Autonomy public-indicator hunt gen 1516

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T041559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema974_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 2.0330 | 0.6714 | 4.3506 | 0.0225 | 0.3662 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema974_below_at_h` | one_head_filter_pi_star | 249 | 20.3410 | 1.6305 | 0.6426 | 3.3488 | 0.0164 | 0.3414 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema974_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.7812 | 0.6490 | 3.7580 | 0.0120 | 0.3020 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema974_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.8063 | 0.6538 | 2.7307 | 0.0114 | 0.3154 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema974_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.6828 | 0.6371 | 3.5345 | 0.0111 | 0.3089 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema974_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 1.2688 | 0.5952 | 1.1211 | 0.0098 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `ema974_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.6366 | 0.6356 | 2.2271 | 0.0094 | 0.3220 | ok | RAN |
| ETHUSDT | 8 | `ema974_above_at_h` | one_head_filter_pi_star | 135 | 11.1404 | 1.2461 | 0.6000 | 1.0730 | 0.0090 | 0.2148 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema974_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema974_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema974_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema974_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema974_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema974_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
