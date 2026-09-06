# Autonomy public-indicator hunt gen 988

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T175027Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema995_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.8318 | 0.6681 | 3.8404 | 0.0197 | 0.3540 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema995_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 1.6983 | 0.6500 | 3.5547 | 0.0175 | 0.3292 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema995_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7813 | 0.6535 | 3.9088 | 0.0126 | 0.3031 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema995_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.6379 | 0.6367 | 3.4374 | 0.0106 | 0.3109 | ok | RAN |
| SOLUSDT | 4 | `ema995_above_at_h` | one_head_filter_pi_star | 126 | 10.2741 | 1.7119 | 0.6429 | 2.5338 | 0.0103 | 0.3095 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema995_above_at_h` | one_head_filter_pi_star | 144 | 11.8841 | 1.2773 | 0.5972 | 1.2332 | 0.0101 | 0.2361 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema995_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.5423 | 0.6271 | 1.9687 | 0.0081 | 0.2881 | ok | RAN |
| ETHUSDT | 4 | `ema995_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 1.1427 | 0.5938 | 0.6481 | 0.0057 | 0.2344 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema995_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema995_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema995_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema995_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema995_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema995_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
