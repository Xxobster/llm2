# Autonomy public-indicator hunt gen 868

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T221215Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema845_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.8801 | 0.6767 | 3.9884 | 0.0208 | 0.3578 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema845_below_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.8271 | 0.6651 | 3.7432 | 0.0197 | 0.3578 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema845_below_at_h` | one_head_filter_pi_star | 241 | 19.7068 | 1.8131 | 0.6515 | 3.8593 | 0.0123 | 0.3029 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema845_below_at_h` | one_head_filter_pi_star | 222 | 18.1531 | 1.7957 | 0.6577 | 3.5774 | 0.0123 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema845_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.6994 | 0.6299 | 2.5591 | 0.0100 | 0.3071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema845_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.6862 | 0.6434 | 2.4740 | 0.0099 | 0.3178 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema845_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.1660 | 0.5909 | 0.7295 | 0.0064 | 0.2121 | ok | RAN |
| ETHUSDT | 4 | `ema845_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1026 | 0.5897 | 0.5071 | 0.0039 | 0.2051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema845_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema845_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema845_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema845_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema845_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema845_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
