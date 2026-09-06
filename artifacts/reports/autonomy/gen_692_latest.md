# Autonomy public-indicator hunt gen 692

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T063625Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema625_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0486 | 0.6786 | 4.2488 | 0.0233 | 0.3878 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema625_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8937 | 0.6748 | 3.9895 | 0.0206 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema625_below_at_h` | one_head_filter_pi_star | 227 | 18.5620 | 1.8340 | 0.6608 | 3.8166 | 0.0126 | 0.3216 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema625_below_at_h` | one_head_filter_pi_star | 217 | 17.7443 | 1.8092 | 0.6544 | 3.6208 | 0.0124 | 0.3180 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema625_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5617 | 0.6170 | 2.2463 | 0.0086 | 0.3333 | ok | RAN |
| SOLUSDT | 8 | `ema625_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5301 | 0.6170 | 2.1175 | 0.0083 | 0.3191 | ok | RAN |
| ETHUSDT | 8 | `ema625_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.1841 | 0.6125 | 0.8927 | 0.0066 | 0.1938 | ok | RAN |
| ETHUSDT | 4 | `ema625_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1721 | 0.5987 | 0.8376 | 0.0063 | 0.1974 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema625_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema625_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema625_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema625_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
