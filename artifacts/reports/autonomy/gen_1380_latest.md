# Autonomy public-indicator hunt gen 1380

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T034711Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema954_below_at_h` | one_head_filter_pi_star | 10 | 1.5712 | 1.8910 | 0.7000 | 1.2388 | 0.0913 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema954_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7764 | 0.6639 | 3.7573 | 0.0183 | 0.3445 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema954_below_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 1.6970 | 0.6475 | 3.5822 | 0.0177 | 0.3361 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema954_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.4135 | 0.6214 | 1.7432 | 0.0149 | 0.2286 | ok | RAN |
| SOLUSDT | 8 | `ema954_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 1.7022 | 0.6394 | 3.6840 | 0.0114 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema954_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.7643 | 0.6612 | 2.6869 | 0.0113 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema954_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.6845 | 0.6437 | 3.4427 | 0.0110 | 0.2996 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema954_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.6982 | 0.6609 | 2.3901 | 0.0102 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema954_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.2415 | 0.6084 | 1.0814 | 0.0093 | 0.2168 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema954_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema954_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema954_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema954_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema954_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
