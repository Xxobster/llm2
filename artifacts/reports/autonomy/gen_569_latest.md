# Autonomy public-indicator hunt gen 569

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T222902Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema980_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema980_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.9315 | 0.6754 | 4.1566 | 0.0210 | 0.3509 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema980_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 1.7478 | 0.6542 | 3.7169 | 0.0188 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema980_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.8155 | 0.6482 | 3.9967 | 0.0124 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema980_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.7341 | 0.6480 | 3.6571 | 0.0114 | 0.3000 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema980_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.6998 | 0.6446 | 2.3780 | 0.0106 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema980_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.6371 | 0.6378 | 2.3442 | 0.0093 | 0.3150 | ok | RAN |
| ETHUSDT | 4 | `ema980_above_at_h` | one_head_filter_pi_star | 121 | 9.9851 | 1.2085 | 0.5950 | 0.8670 | 0.0078 | 0.1983 | ok | RAN |
| ETHUSDT | 8 | `ema980_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 1.0784 | 0.5726 | 0.3521 | 0.0030 | 0.2137 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema980_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema980_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
