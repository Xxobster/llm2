# Autonomy public-indicator hunt gen 705

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T073209Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1320_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1320_below_at_h` | one_head_filter_pi_star | 272 | 22.2199 | 1.8620 | 0.6654 | 4.2553 | 0.0197 | 0.3309 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1320_below_at_h` | one_head_filter_pi_star | 282 | 23.0368 | 1.7739 | 0.6596 | 4.1281 | 0.0185 | 0.3298 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1320_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.7017 | 0.6324 | 3.6834 | 0.0116 | 0.3199 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1320_below_at_h` | one_head_filter_pi_star | 277 | 22.6505 | 1.6601 | 0.6318 | 3.5673 | 0.0108 | 0.3141 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1320_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.6742 | 0.6522 | 2.2581 | 0.0095 | 0.2783 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1320_above_at_h` | one_head_filter_pi_star | 98 | 8.0878 | 1.2275 | 0.5918 | 0.8523 | 0.0092 | 0.2143 | ok | RAN |
| SOLUSDT | 4 | `ema1320_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.4240 | 0.6381 | 1.5052 | 0.0063 | 0.2667 | ok | RAN |
| ETHUSDT | 8 | `ema1320_above_at_h` | one_head_filter_pi_star | 85 | 7.0149 | 1.0832 | 0.5765 | 0.3263 | 0.0036 | 0.2235 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1320_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1320_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
