# Autonomy public-indicator hunt gen 1404

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T061531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema958_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.8456 | 0.6709 | 3.9863 | 0.0202 | 0.3502 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema958_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.7243 | 0.6525 | 3.6400 | 0.0178 | 0.3432 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema958_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.8929 | 0.6549 | 4.2460 | 0.0133 | 0.3098 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema958_above_at_h` | one_head_filter_pi_star | 110 | 9.1424 | 1.8258 | 0.6727 | 2.6448 | 0.0117 | 0.3364 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema958_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.6999 | 0.6429 | 3.5230 | 0.0113 | 0.3056 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema958_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.2786 | 0.6061 | 1.1866 | 0.0106 | 0.2197 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema958_above_at_h` | one_head_filter_pi_star | 127 | 10.3556 | 1.5276 | 0.6220 | 2.0086 | 0.0080 | 0.2992 | ok | RAN |
| ETHUSDT | 8 | `ema958_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 1.1865 | 0.5940 | 0.8288 | 0.0070 | 0.2331 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema958_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema958_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema958_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema958_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema958_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema958_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
