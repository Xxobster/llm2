# Autonomy public-indicator hunt gen 628

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T021843Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema545_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0877 | 0.6957 | 4.4390 | 0.0236 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema545_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9433 | 0.6834 | 4.1683 | 0.0218 | 0.3769 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema545_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8337 | 0.6616 | 3.5697 | 0.0127 | 0.3434 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema545_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.7875 | 0.6507 | 3.5028 | 0.0120 | 0.3206 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema545_above_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.6375 | 0.6294 | 2.6993 | 0.0096 | 0.2882 | ok | RAN |
| SOLUSDT | 8 | `ema545_above_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.5507 | 0.6164 | 2.2592 | 0.0087 | 0.3151 | ok | RAN |
| ETHUSDT | 4 | `ema545_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1399 | 0.5864 | 0.6808 | 0.0051 | 0.1852 | ok | RAN |
| ETHUSDT | 8 | `ema545_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.0610 | 0.5864 | 0.3142 | 0.0023 | 0.2037 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema545_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema545_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema545_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema545_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema545_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema545_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
