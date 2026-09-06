# Autonomy public-indicator hunt gen 601

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T003550Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1060_below_at_h` | one_head_filter_pi_star | 10 | 1.7037 | 3.8400 | 0.8000 | 2.3848 | 0.1444 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1060_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 1.6889 | 0.6461 | 3.5106 | 0.0174 | 0.3292 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1060_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 1.6318 | 0.6449 | 3.2438 | 0.0162 | 0.3347 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1060_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 1.7911 | 0.6437 | 3.9443 | 0.0122 | 0.3103 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1060_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.8763 | 0.6696 | 2.8466 | 0.0120 | 0.2946 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1060_below_at_h` | one_head_filter_pi_star | 267 | 21.7210 | 1.6417 | 0.6292 | 3.3946 | 0.0105 | 0.3034 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1060_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.5541 | 0.6325 | 2.0152 | 0.0083 | 0.2906 | ok | RAN |
| ETHUSDT | 4 | `ema1060_above_at_h` | one_head_filter_pi_star | 108 | 8.9131 | 1.1035 | 0.5741 | 0.4329 | 0.0042 | 0.2130 | ok | RAN |
| ETHUSDT | 8 | `ema1060_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 1.0408 | 0.5556 | 0.1784 | 0.0017 | 0.1966 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1060_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1060_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
