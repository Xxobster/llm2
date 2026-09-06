# Autonomy public-indicator hunt gen 897

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T010741Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1800_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1800_below_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.6363 | 0.6474 | 3.6861 | 0.0166 | 0.3100 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1800_below_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.5729 | 0.6413 | 3.4460 | 0.0153 | 0.3070 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1800_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.8817 | 0.6507 | 4.3485 | 0.0140 | 0.3382 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1800_below_at_h` | one_head_filter_pi_star | 278 | 22.7323 | 1.8964 | 0.6547 | 4.4322 | 0.0135 | 0.3273 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1800_above_at_h` | one_head_filter_pi_star | 90 | 7.3399 | 1.7371 | 0.6667 | 2.1597 | 0.0095 | 0.2778 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1800_above_at_h` | one_head_filter_pi_star | 98 | 7.9923 | 1.6916 | 0.6429 | 2.1036 | 0.0093 | 0.2347 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1800_above_at_h` | one_head_filter_pi_star | 56 | 4.9247 | 1.1791 | 0.5893 | 0.5317 | 0.0073 | 0.2321 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1800_above_at_h` | one_head_filter_pi_star | 38 | 3.3417 | 0.9815 | 0.5526 | -0.0500 | -0.0009 | 0.2632 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1800_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0463 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1800_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4980 | 0.2667 | -1.0243 | -0.0545 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
