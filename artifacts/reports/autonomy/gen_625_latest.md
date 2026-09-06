# Autonomy public-indicator hunt gen 625

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T020654Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1120_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| BTCUSDT | 8 | `ema1120_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1120_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7585 | 0.6555 | 3.6914 | 0.0178 | 0.3277 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1120_below_at_h` | one_head_filter_pi_star | 252 | 20.5861 | 1.6795 | 0.6468 | 3.5897 | 0.0173 | 0.3373 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1120_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.6725 | 0.6377 | 3.5446 | 0.0111 | 0.3132 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1120_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.6514 | 0.6455 | 2.2526 | 0.0096 | 0.3182 | ok | RAN |
| SOLUSDT | 8 | `ema1120_above_at_h` | one_head_filter_pi_star | 109 | 8.9385 | 1.6134 | 0.6330 | 2.1282 | 0.0093 | 0.3028 | ok | RAN |
| ETHUSDT | 4 | `ema1120_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 1.2356 | 0.5984 | 0.9906 | 0.0093 | 0.2295 | ok | RAN |
| SOLUSDT | 4 | `ema1120_below_at_h` | one_head_filter_pi_star | 280 | 22.8958 | 1.5232 | 0.6179 | 3.0030 | 0.0090 | 0.3036 | ok | RAN |
| ETHUSDT | 8 | `ema1120_above_at_h` | one_head_filter_pi_star | 119 | 9.8200 | 1.1569 | 0.5798 | 0.6666 | 0.0062 | 0.2017 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1120_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1120_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
