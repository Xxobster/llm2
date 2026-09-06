# Autonomy public-indicator hunt gen 852

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T203828Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema825_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.8968 | 0.6729 | 3.8672 | 0.0205 | 0.3692 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema825_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8342 | 0.6711 | 3.7946 | 0.0205 | 0.3644 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema825_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8446 | 0.6599 | 4.0187 | 0.0127 | 0.3117 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema825_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 1.7951 | 0.6567 | 3.6885 | 0.0120 | 0.3090 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema825_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.8046 | 0.6641 | 2.7859 | 0.0117 | 0.3359 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema825_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.6625 | 0.6412 | 2.4537 | 0.0094 | 0.3206 | ok | RAN |
| ETHUSDT | 8 | `ema825_above_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 1.1236 | 0.5878 | 0.5642 | 0.0048 | 0.2137 | ok | RAN |
| ETHUSDT | 4 | `ema825_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.1300 | 0.5890 | 0.6386 | 0.0048 | 0.2192 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema825_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema825_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema825_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema825_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema825_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema825_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
