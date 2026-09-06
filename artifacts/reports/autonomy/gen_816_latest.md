# Autonomy public-indicator hunt gen 816

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T171038Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma1640_above_at_h` | one_head_filter_pi_star | 56 | 4.6551 | 2.6026 | 0.7679 | 2.8742 | 0.0181 | 0.3214 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1640_below_at_h` | one_head_filter_pi_star | 286 | 23.3636 | 1.6813 | 0.6503 | 3.8588 | 0.0168 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1640_above_at_h` | one_head_filter_pi_star | 40 | 3.4768 | 2.3825 | 0.7250 | 2.4388 | 0.0166 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1640_below_at_h` | one_head_filter_pi_star | 273 | 22.3016 | 1.6438 | 0.6484 | 3.5587 | 0.0163 | 0.3187 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1640_below_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 1.7359 | 0.6352 | 3.9925 | 0.0109 | 0.3145 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1640_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.6907 | 0.6297 | 3.8000 | 0.0105 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma1640_above_at_h` | one_head_filter_pi_star | 69 | 5.9898 | 1.1151 | 0.5797 | 0.3889 | 0.0051 | 0.2319 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1640_above_at_h` | one_head_filter_pi_star | 67 | 5.5294 | 1.0032 | 0.5672 | 0.0116 | 0.0002 | 0.2537 | ok | RAN |
| BTCUSDT | 4 | `sma1640_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0522 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1640_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
