# Autonomy public-indicator hunt gen 1540

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T063312Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema978_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.8275 | 0.6623 | 3.9091 | 0.0198 | 0.3596 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema978_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.7979 | 0.6596 | 3.7810 | 0.0188 | 0.3489 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema978_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.7775 | 0.6446 | 3.7754 | 0.0120 | 0.3058 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema978_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.2985 | 0.6042 | 1.3018 | 0.0112 | 0.2361 | ok | RAN |
| SOLUSDT | 4 | `ema978_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.6814 | 0.6389 | 3.4543 | 0.0109 | 0.2976 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema978_above_at_h` | one_head_filter_pi_star | 111 | 9.2255 | 1.6455 | 0.6486 | 2.2669 | 0.0095 | 0.3153 | ok | RAN |
| SOLUSDT | 8 | `ema978_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.6155 | 0.6198 | 2.2343 | 0.0091 | 0.3058 | ok | RAN |
| ETHUSDT | 4 | `ema978_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 1.1866 | 0.5887 | 0.8013 | 0.0071 | 0.2097 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema978_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema978_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema978_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema978_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema978_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema978_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
