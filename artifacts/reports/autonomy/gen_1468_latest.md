# Autonomy public-indicator hunt gen 1468

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T234936Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema968_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8723 | 0.6622 | 3.9837 | 0.0203 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema968_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 1.6583 | 0.6461 | 3.4418 | 0.0164 | 0.3416 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema968_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.3263 | 0.6207 | 1.4510 | 0.0120 | 0.2345 | ok | RAN |
| SOLUSDT | 8 | `ema968_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 1.7473 | 0.6398 | 3.8025 | 0.0118 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema968_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.7464 | 0.6440 | 3.6978 | 0.0118 | 0.2960 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema968_above_at_h` | one_head_filter_pi_star | 121 | 9.9452 | 1.8169 | 0.6777 | 2.6481 | 0.0115 | 0.3306 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema968_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.5313 | 0.6121 | 1.9237 | 0.0078 | 0.3103 | ok | RAN |
| ETHUSDT | 4 | `ema968_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.1539 | 0.5906 | 0.6818 | 0.0058 | 0.2205 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema968_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema968_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema968_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema968_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema968_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema968_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
