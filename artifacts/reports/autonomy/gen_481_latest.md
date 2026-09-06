# Autonomy public-indicator hunt gen 481

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T164021Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema760_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 2.0409 | 0.6860 | 4.3634 | 0.0232 | 0.3768 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema760_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8755 | 0.6782 | 3.8081 | 0.0209 | 0.3861 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema760_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8349 | 0.6559 | 4.0220 | 0.0127 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema760_below_at_h` | one_head_filter_pi_star | 223 | 18.2349 | 1.8221 | 0.6592 | 3.7415 | 0.0124 | 0.3274 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema760_above_at_h` | one_head_filter_pi_star | 115 | 9.5580 | 1.6711 | 0.6522 | 2.3611 | 0.0101 | 0.3391 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema760_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.3020 | 0.6111 | 1.3887 | 0.0100 | 0.2099 | ok | RAN |
| ETHUSDT | 8 | `ema760_above_at_h` | one_head_filter_pi_star | 139 | 11.4705 | 1.2695 | 0.6115 | 1.1749 | 0.0095 | 0.2086 | ok | RAN |
| SOLUSDT | 4 | `ema760_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.5802 | 0.6370 | 2.2788 | 0.0088 | 0.3333 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0393 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
