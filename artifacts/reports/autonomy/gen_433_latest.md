# Autonomy public-indicator hunt gen 433

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T101244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema640_below_at_h` | one_head_filter_pi_star | 204 | 16.6649 | 1.9564 | 0.6765 | 4.1902 | 0.0222 | 0.3775 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema640_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.8899 | 0.6698 | 4.1089 | 0.0211 | 0.3632 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema640_below_at_h` | one_head_filter_pi_star | 218 | 17.8260 | 1.8288 | 0.6560 | 3.7318 | 0.0128 | 0.3211 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema640_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.8255 | 0.6635 | 3.6453 | 0.0127 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema640_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.6504 | 0.6267 | 2.5940 | 0.0098 | 0.3133 | ok | RAN |
| SOLUSDT | 4 | `ema640_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.5964 | 0.6260 | 2.2546 | 0.0092 | 0.3359 | ok | RAN |
| ETHUSDT | 4 | `ema640_above_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 1.1853 | 0.5890 | 0.8639 | 0.0068 | 0.2055 | ok | RAN |
| ETHUSDT | 8 | `ema640_above_at_h` | one_head_filter_pi_star | 154 | 12.7083 | 1.1704 | 0.5909 | 0.8160 | 0.0063 | 0.2013 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema640_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema640_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
