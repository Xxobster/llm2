# Autonomy public-indicator hunt gen 916

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T031157Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema905_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1310 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema905_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8596 | 0.6712 | 3.8904 | 0.0200 | 0.3559 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema905_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.7570 | 0.6608 | 3.6703 | 0.0190 | 0.3612 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema905_below_at_h` | one_head_filter_pi_star | 229 | 18.7255 | 1.8025 | 0.6550 | 3.7308 | 0.0121 | 0.3100 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema905_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.7228 | 0.6443 | 3.6492 | 0.0114 | 0.3083 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema905_above_at_h` | one_head_filter_pi_star | 140 | 11.5078 | 1.2560 | 0.6071 | 1.1968 | 0.0096 | 0.2286 | ok | RAN |
| SOLUSDT | 8 | `ema905_above_at_h` | one_head_filter_pi_star | 128 | 10.4372 | 1.6239 | 0.6172 | 2.3427 | 0.0091 | 0.3125 | ok | RAN |
| SOLUSDT | 4 | `ema905_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.5476 | 0.6165 | 2.1443 | 0.0086 | 0.3158 | ok | RAN |
| ETHUSDT | 8 | `ema905_above_at_h` | one_head_filter_pi_star | 138 | 11.3880 | 1.1562 | 0.5797 | 0.7385 | 0.0063 | 0.2246 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema905_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema905_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema905_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema905_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema905_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
