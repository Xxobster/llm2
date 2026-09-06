# Autonomy public-indicator hunt gen 109

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T163937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema5_above_at_h` | one_head_filter_pi_star | 46 | 3.8900 | 2.5165 | 0.6957 | 2.5068 | 0.0467 | 0.5652 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema5_above_at_h` | one_head_filter_pi_star | 12 | 1.2830 | 3.2032 | 0.8333 | 2.1468 | 0.0371 | 0.5833 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema5_below_at_h` | one_head_filter_pi_star | 50 | 4.5109 | 2.0480 | 0.7200 | 2.1098 | 0.0317 | 0.4200 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema5_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.7448 | 0.6807 | 3.0682 | 0.0216 | 0.4036 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema5_below_at_h` | one_head_filter_pi_star | 155 | 12.6745 | 2.2196 | 0.6839 | 4.0554 | 0.0188 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema5_cross_up` | one_head_filter_pi_star | 345 | 28.0664 | 1.5549 | 0.6377 | 3.5189 | 0.0153 | 0.2986 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema5_cross_down` | one_head_filter_pi_star | 383 | 31.1578 | 1.5394 | 0.6423 | 3.5700 | 0.0151 | 0.3003 | ok | RAN |
| ETHUSDT | 4 | `ema5_above_at_h` | one_head_filter_pi_star | 138 | 11.3880 | 1.4496 | 0.6159 | 1.7114 | 0.0151 | 0.2319 | ok | RAN |
| ETHUSDT | 4 | `ema5_cross_up` | one_head_filter_pi_star | 88 | 7.2412 | 1.4836 | 0.6250 | 1.5918 | 0.0138 | 0.2841 | ok | RAN |
| SOLUSDT | 8 | `ema5_cross_up` | one_head_filter_pi_star | 346 | 28.1478 | 1.7922 | 0.6503 | 4.7097 | 0.0111 | 0.3006 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5_cross_down` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema5_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4139 | 0.6010 | 2.1291 | 0.0066 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `ema5_cross_down` | one_head_filter_pi_star | 89 | 7.3038 | 1.2835 | 0.6292 | 1.0598 | 0.0037 | 0.1348 | ok | RAN |
| SOLUSDT | 4 | `ema5_cross_up` | one_head_filter_pi_star | 38 | 3.1292 | 1.1738 | 0.6053 | 0.4216 | 0.0030 | 0.2895 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5_cross_down` | one_head_filter_pi_star | 24 | 2.0423 | 1.0210 | 0.4167 | 0.0411 | 0.0017 | 0.1250 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5_cross_down` | one_head_filter_pi_star | 49 | 4.4132 | 0.9923 | 0.5306 | -0.0221 | -0.0002 | 0.0816 | ok | RAN |
| BTCUSDT | 4 | `ema5_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.9014 | 0.4211 | -0.1767 | -0.0105 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5_cross_up` | one_head_filter_pi_star | 22 | 2.5139 | 0.8648 | 0.4545 | -0.3312 | -0.0135 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema5_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
