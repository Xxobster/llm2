# Autonomy public-indicator hunt gen 624

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T020310Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1160_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 2.0333 | 0.6763 | 4.2874 | 0.0234 | 0.3671 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1160_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.9306 | 0.6784 | 4.2263 | 0.0217 | 0.3524 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1160_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.8564 | 0.6520 | 4.0916 | 0.0130 | 0.3160 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1160_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.7481 | 0.6473 | 3.7612 | 0.0117 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1160_above_at_h` | one_head_filter_pi_star | 95 | 7.7905 | 1.5644 | 0.6526 | 1.8581 | 0.0084 | 0.2842 | ok | RAN |
| SOLUSDT | 4 | `sma1160_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.5593 | 0.6415 | 1.9262 | 0.0080 | 0.2642 | ok | RAN |
| ETHUSDT | 4 | `sma1160_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.0729 | 0.5625 | 0.3448 | 0.0030 | 0.2014 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1160_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.9865 | 0.5473 | -0.0726 | -0.0006 | 0.2230 | ok | RAN |
| BTCUSDT | 4 | `sma1160_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1160_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
