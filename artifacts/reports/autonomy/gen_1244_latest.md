# Autonomy public-indicator hunt gen 1244

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T144859Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema934_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 2.0512 | 0.6726 | 4.5049 | 0.0226 | 0.3540 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema934_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.8489 | 0.6639 | 4.0070 | 0.0200 | 0.3445 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema934_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 1.8444 | 0.6546 | 4.0421 | 0.0124 | 0.3052 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema934_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.7892 | 0.6488 | 3.7461 | 0.0122 | 0.3017 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema934_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.7213 | 0.6417 | 2.4907 | 0.0105 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema934_above_at_h` | one_head_filter_pi_star | 110 | 9.1424 | 1.6016 | 0.6455 | 2.1312 | 0.0092 | 0.3273 | ok | RAN |
| ETHUSDT | 8 | `ema934_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.1798 | 0.5920 | 0.8173 | 0.0070 | 0.2160 | ok | RAN |
| ETHUSDT | 4 | `ema934_above_at_h` | one_head_filter_pi_star | 114 | 9.3707 | 1.1541 | 0.5965 | 0.6491 | 0.0060 | 0.2193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema934_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema934_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema934_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema934_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema934_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema934_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
