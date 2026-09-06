# Autonomy public-indicator hunt gen 138

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T183224Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema144_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0930 | 0.7016 | 4.7614 | 0.0244 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema144_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0531 | 0.6959 | 4.6704 | 0.0239 | 0.3763 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema144_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.2180 | 0.6927 | 4.3673 | 0.0177 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema144_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1060 | 0.6867 | 3.9261 | 0.0167 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema144_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2369 | 0.5957 | 1.1857 | 0.0081 | 0.2340 | ok | RAN |
| SOLUSDT | 8 | `ema144_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3313 | 0.5891 | 1.7206 | 0.0051 | 0.2723 | ok | RAN |
| ETHUSDT | 4 | `ema144_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1393 | 0.5938 | 0.7418 | 0.0050 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `ema144_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2928 | 0.5871 | 1.5397 | 0.0045 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema144_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema144_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema144_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema144_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema144_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema144_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
