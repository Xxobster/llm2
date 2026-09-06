# Autonomy public-indicator hunt gen 956

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T074122Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema955_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 2.0179 | 0.6767 | 4.4838 | 0.0224 | 0.3534 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema955_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 1.7450 | 0.6569 | 3.7614 | 0.0184 | 0.3431 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema955_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7831 | 0.6454 | 3.8754 | 0.0123 | 0.3068 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema955_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7113 | 0.6420 | 3.5053 | 0.0113 | 0.3045 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema955_above_at_h` | one_head_filter_pi_star | 134 | 11.0146 | 1.3006 | 0.6119 | 1.2908 | 0.0111 | 0.2239 | ok | RAN |
| SOLUSDT | 4 | `ema955_above_at_h` | one_head_filter_pi_star | 112 | 9.3086 | 1.7327 | 0.6518 | 2.4374 | 0.0109 | 0.3304 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema955_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.6376 | 0.6341 | 2.2874 | 0.0092 | 0.3089 | ok | RAN |
| ETHUSDT | 4 | `ema955_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 1.1471 | 0.5802 | 0.6638 | 0.0057 | 0.2214 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema955_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema955_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema955_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema955_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema955_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema955_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
