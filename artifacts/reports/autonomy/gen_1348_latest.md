# Autonomy public-indicator hunt gen 1348

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T004913Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema950_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema950_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 1.9229 | 0.6724 | 4.2165 | 0.0213 | 0.3534 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema950_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7837 | 0.6513 | 3.8101 | 0.0185 | 0.3403 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema950_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.4580 | 0.6232 | 1.8785 | 0.0152 | 0.2391 | ok | RAN |
| SOLUSDT | 8 | `ema950_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.9248 | 0.6573 | 4.3170 | 0.0137 | 0.3105 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema950_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 1.7252 | 0.6434 | 3.6532 | 0.0115 | 0.3062 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema950_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 1.3172 | 0.6200 | 1.4726 | 0.0112 | 0.2267 | ok | RAN |
| SOLUSDT | 8 | `ema950_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.7706 | 0.6667 | 2.5447 | 0.0111 | 0.3158 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema950_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.7156 | 0.6529 | 2.4003 | 0.0107 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema950_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema950_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema950_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema950_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema950_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
