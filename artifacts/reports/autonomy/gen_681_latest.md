# Autonomy public-indicator hunt gen 681

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T054942Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1260_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1488 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1260_below_at_h` | one_head_filter_pi_star | 259 | 21.1579 | 1.8301 | 0.6564 | 4.0863 | 0.0193 | 0.3359 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1260_below_at_h` | one_head_filter_pi_star | 269 | 21.9748 | 1.7614 | 0.6543 | 3.9674 | 0.0187 | 0.3383 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1260_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.7160 | 0.6445 | 3.6793 | 0.0117 | 0.3164 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1260_below_at_h` | one_head_filter_pi_star | 286 | 23.3865 | 1.6298 | 0.6329 | 3.5160 | 0.0104 | 0.3112 | ok | RAN |
| SOLUSDT | 4 | `ema1260_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.7303 | 0.6389 | 2.3587 | 0.0102 | 0.2870 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1260_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.6635 | 0.6514 | 2.1959 | 0.0093 | 0.2661 | ok | RAN |
| ETHUSDT | 8 | `ema1260_above_at_h` | one_head_filter_pi_star | 81 | 6.6848 | 1.2341 | 0.6049 | 0.8529 | 0.0093 | 0.2469 | ok | RAN |
| ETHUSDT | 4 | `ema1260_above_at_h` | one_head_filter_pi_star | 97 | 8.0053 | 1.1731 | 0.5876 | 0.6518 | 0.0069 | 0.2062 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1260_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1260_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1260_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1260_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1260_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
