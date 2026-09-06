# Autonomy public-indicator hunt gen 513

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T184559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema840_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 2.0764 | 0.6919 | 4.2860 | 0.0236 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema840_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.7513 | 0.6604 | 3.4375 | 0.0185 | 0.3726 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema840_below_at_h` | one_head_filter_pi_star | 230 | 18.8073 | 1.8581 | 0.6609 | 3.9422 | 0.0128 | 0.3174 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema840_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7935 | 0.6516 | 3.8010 | 0.0123 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema840_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.7052 | 0.6529 | 2.4899 | 0.0103 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema840_above_at_h` | one_head_filter_pi_star | 140 | 11.4157 | 1.5144 | 0.6143 | 2.0412 | 0.0082 | 0.3071 | ok | RAN |
| ETHUSDT | 4 | `ema840_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 1.1706 | 0.5935 | 0.8618 | 0.0064 | 0.2065 | ok | RAN |
| ETHUSDT | 8 | `ema840_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1633 | 0.5844 | 0.8352 | 0.0062 | 0.2208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema840_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0571 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema840_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
