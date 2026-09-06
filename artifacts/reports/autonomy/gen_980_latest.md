# Autonomy public-indicator hunt gen 980

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T101001Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema985_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema985_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.8882 | 0.6681 | 4.0257 | 0.0202 | 0.3493 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema985_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.7713 | 0.6580 | 3.6731 | 0.0189 | 0.3463 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema985_above_at_h` | one_head_filter_pi_star | 124 | 10.2327 | 1.3330 | 0.6048 | 1.3508 | 0.0117 | 0.2258 | ok | RAN |
| SOLUSDT | 8 | `ema985_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.7168 | 0.6408 | 3.5567 | 0.0114 | 0.3143 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema985_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.7160 | 0.6404 | 3.7156 | 0.0113 | 0.3034 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema985_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.6754 | 0.6557 | 2.3875 | 0.0099 | 0.3197 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema985_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 1.2341 | 0.6063 | 0.9995 | 0.0086 | 0.2126 | ok | RAN |
| SOLUSDT | 8 | `ema985_above_at_h` | one_head_filter_pi_star | 121 | 9.9458 | 1.4897 | 0.6281 | 1.8548 | 0.0076 | 0.2893 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema985_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema985_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema985_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema985_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema985_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
