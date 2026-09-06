# Autonomy public-indicator hunt gen 1092

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T220040Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema912_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.8387 | 0.6696 | 3.9383 | 0.0201 | 0.3565 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema912_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8086 | 0.6597 | 3.8302 | 0.0194 | 0.3487 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema912_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.8340 | 0.6516 | 3.9372 | 0.0125 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema912_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.8065 | 0.6638 | 3.7630 | 0.0123 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema912_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.7523 | 0.6160 | 2.5812 | 0.0107 | 0.3040 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema912_above_at_h` | one_head_filter_pi_star | 128 | 10.5214 | 1.2524 | 0.6016 | 1.0713 | 0.0091 | 0.2266 | ok | RAN |
| SOLUSDT | 4 | `ema912_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.6001 | 0.6299 | 2.2609 | 0.0088 | 0.3150 | ok | RAN |
| ETHUSDT | 4 | `ema912_above_at_h` | one_head_filter_pi_star | 132 | 10.8928 | 1.1208 | 0.5833 | 0.5710 | 0.0048 | 0.2197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema912_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema912_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema912_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema912_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema912_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema912_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
