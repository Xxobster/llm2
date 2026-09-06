# Autonomy public-indicator hunt gen 369

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T185923Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema480_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1092 | 0.7049 | 4.5806 | 0.0244 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema480_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.9978 | 0.6810 | 4.4981 | 0.0232 | 0.3619 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema480_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.9326 | 0.6700 | 3.9251 | 0.0138 | 0.3550 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema480_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8178 | 0.6537 | 3.5660 | 0.0123 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema480_above_at_h` | one_head_filter_pi_star | 174 | 14.2689 | 1.6749 | 0.6264 | 2.9096 | 0.0102 | 0.2931 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema480_above_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.6614 | 0.6257 | 2.7700 | 0.0099 | 0.2807 | ok | RAN |
| ETHUSDT | 8 | `ema480_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2259 | 0.6051 | 1.0828 | 0.0080 | 0.2166 | ok | RAN |
| ETHUSDT | 4 | `ema480_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.1107 | 0.5871 | 0.5616 | 0.0041 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema480_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
