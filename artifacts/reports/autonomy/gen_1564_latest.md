# Autonomy public-indicator hunt gen 1564

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T165939Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema982_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.8826 | 0.6652 | 4.0496 | 0.0204 | 0.3565 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema982_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8586 | 0.6610 | 3.9947 | 0.0198 | 0.3390 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema982_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7812 | 0.6431 | 3.8831 | 0.0122 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema982_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 1.7309 | 0.6412 | 3.7864 | 0.0117 | 0.3015 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema982_above_at_h` | one_head_filter_pi_star | 129 | 10.6453 | 1.2554 | 0.6047 | 1.0880 | 0.0095 | 0.2093 | ok | RAN |
| SOLUSDT | 8 | `ema982_above_at_h` | one_head_filter_pi_star | 125 | 10.2746 | 1.6004 | 0.6320 | 2.2037 | 0.0090 | 0.3200 | ok | RAN |
| SOLUSDT | 4 | `ema982_above_at_h` | one_head_filter_pi_star | 130 | 10.6003 | 1.5587 | 0.6308 | 2.1238 | 0.0084 | 0.3077 | ok | RAN |
| ETHUSDT | 4 | `ema982_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 1.1273 | 0.5804 | 0.5470 | 0.0051 | 0.2143 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema982_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema982_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema982_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema982_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema982_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema982_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
