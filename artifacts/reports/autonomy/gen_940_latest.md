# Autonomy public-indicator hunt gen 940

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T055330Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema935_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 2.0413 | 0.6748 | 4.3642 | 0.0220 | 0.3592 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema935_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.8395 | 0.6667 | 3.9871 | 0.0199 | 0.3593 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema935_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.7334 | 0.6471 | 3.6910 | 0.0116 | 0.2980 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema935_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.7079 | 0.6475 | 3.5293 | 0.0113 | 0.3074 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema935_above_at_h` | one_head_filter_pi_star | 124 | 10.3060 | 1.6780 | 0.6452 | 2.4396 | 0.0103 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema935_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.2652 | 0.6138 | 1.2296 | 0.0097 | 0.2138 | ok | RAN |
| SOLUSDT | 8 | `ema935_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.6596 | 0.6434 | 2.4046 | 0.0096 | 0.3101 | ok | RAN |
| ETHUSDT | 4 | `ema935_above_at_h` | one_head_filter_pi_star | 139 | 11.4256 | 1.1853 | 0.5899 | 0.8771 | 0.0071 | 0.2302 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema935_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema935_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0549 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema935_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema935_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema935_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema935_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
