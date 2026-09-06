# Autonomy public-indicator hunt gen 1252

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T153229Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema936_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 1.9666 | 0.6797 | 4.3787 | 0.0219 | 0.3506 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema936_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.7882 | 0.6582 | 3.7629 | 0.0190 | 0.3418 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema936_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.8548 | 0.6576 | 4.1340 | 0.0132 | 0.3152 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema936_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.7421 | 0.6457 | 3.7189 | 0.0117 | 0.3031 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema936_above_at_h` | one_head_filter_pi_star | 129 | 10.7216 | 1.6310 | 0.6279 | 2.3227 | 0.0095 | 0.3178 | ok | RAN |
| SOLUSDT | 8 | `ema936_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.5786 | 0.6270 | 2.1251 | 0.0088 | 0.3333 | ok | RAN |
| ETHUSDT | 8 | `ema936_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 1.2334 | 0.6000 | 1.0352 | 0.0085 | 0.2231 | ok | RAN |
| ETHUSDT | 4 | `ema936_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 1.1394 | 0.5902 | 0.6195 | 0.0057 | 0.2295 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema936_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema936_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema936_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema936_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema936_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema936_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
