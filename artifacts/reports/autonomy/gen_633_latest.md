# Autonomy public-indicator hunt gen 633

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T023741Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1140_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1424 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema1140_below_at_h` | one_head_filter_pi_star | 268 | 21.8931 | 1.6671 | 0.6493 | 3.6786 | 0.0171 | 0.3358 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1140_below_at_h` | one_head_filter_pi_star | 259 | 21.1579 | 1.6570 | 0.6448 | 3.4964 | 0.0166 | 0.3320 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1140_below_at_h` | one_head_filter_pi_star | 280 | 22.8958 | 1.6351 | 0.6286 | 3.4645 | 0.0106 | 0.3143 | ok | RAN |
| SOLUSDT | 4 | `ema1140_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 1.6062 | 0.6259 | 3.2957 | 0.0101 | 0.3037 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1140_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.5653 | 0.6446 | 2.0833 | 0.0089 | 0.2893 | ok | RAN |
| SOLUSDT | 8 | `ema1140_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.4264 | 0.6321 | 1.5826 | 0.0069 | 0.2925 | ok | RAN |
| ETHUSDT | 4 | `ema1140_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 1.0934 | 0.5688 | 0.4012 | 0.0038 | 0.2202 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1140_above_at_h` | one_head_filter_pi_star | 107 | 8.8305 | 1.0259 | 0.5607 | 0.1119 | 0.0011 | 0.2056 | ok | RAN |
| BTCUSDT | 8 | `ema1140_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1140_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0592 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
