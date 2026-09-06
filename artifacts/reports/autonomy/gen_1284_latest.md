# Autonomy public-indicator hunt gen 1284

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T184038Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema941_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.9541 | 0.6712 | 4.2529 | 0.0213 | 0.3514 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema941_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8899 | 0.6697 | 4.0297 | 0.0198 | 0.3484 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema941_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.8126 | 0.6488 | 3.8884 | 0.0124 | 0.3099 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema941_above_at_h` | one_head_filter_pi_star | 124 | 10.1926 | 1.3146 | 0.6048 | 1.2883 | 0.0117 | 0.2339 | ok | RAN |
| SOLUSDT | 4 | `ema941_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7158 | 0.6431 | 3.5859 | 0.0113 | 0.3020 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema941_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.2924 | 0.6081 | 1.3520 | 0.0110 | 0.2230 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema941_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.6273 | 0.6452 | 2.2801 | 0.0093 | 0.3145 | ok | RAN |
| SOLUSDT | 4 | `ema941_above_at_h` | one_head_filter_pi_star | 118 | 9.6986 | 1.4984 | 0.6356 | 1.8896 | 0.0079 | 0.3051 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema941_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema941_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema941_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema941_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema941_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema941_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
