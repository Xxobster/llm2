# Autonomy public-indicator hunt gen 972

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T211856Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema975_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 2.0345 | 0.6812 | 4.4540 | 0.0227 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema975_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.7521 | 0.6537 | 3.5912 | 0.0180 | 0.3420 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema975_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7681 | 0.6494 | 3.8280 | 0.0123 | 0.3028 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema975_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.7632 | 0.6461 | 3.7125 | 0.0117 | 0.3045 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema975_above_at_h` | one_head_filter_pi_star | 113 | 9.3918 | 1.6936 | 0.6726 | 2.2746 | 0.0108 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema975_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.2474 | 0.5940 | 1.0683 | 0.0089 | 0.2256 | ok | RAN |
| SOLUSDT | 8 | `ema975_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.5842 | 0.6371 | 2.1960 | 0.0088 | 0.3065 | ok | RAN |
| ETHUSDT | 4 | `ema975_above_at_h` | one_head_filter_pi_star | 130 | 10.7278 | 1.1489 | 0.5846 | 0.6710 | 0.0059 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema975_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema975_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema975_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema975_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema975_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema975_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
