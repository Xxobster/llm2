# Autonomy public-indicator hunt gen 593

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T000456Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1040_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema1040_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.7954 | 0.6638 | 3.7814 | 0.0188 | 0.3362 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1040_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.7665 | 0.6581 | 3.6618 | 0.0184 | 0.3419 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1040_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.7413 | 0.6415 | 3.8523 | 0.0118 | 0.3094 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1040_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 1.6719 | 0.6374 | 3.5054 | 0.0107 | 0.3053 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1040_above_at_h` | one_head_filter_pi_star | 110 | 9.0416 | 1.5758 | 0.6364 | 2.0141 | 0.0088 | 0.3091 | ok | RAN |
| SOLUSDT | 8 | `ema1040_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.5708 | 0.6545 | 1.9717 | 0.0086 | 0.2909 | ok | RAN |
| ETHUSDT | 4 | `ema1040_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 1.2030 | 0.5840 | 0.8777 | 0.0077 | 0.2240 | ok | RAN |
| ETHUSDT | 8 | `ema1040_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 1.0851 | 0.5603 | 0.3705 | 0.0034 | 0.1983 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1040_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1040_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
