# Autonomy public-indicator hunt gen 1492

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T020338Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema971_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema971_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 1.6853 | 0.6463 | 3.5637 | 0.0173 | 0.3415 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema971_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 1.6799 | 0.6463 | 3.3667 | 0.0171 | 0.3406 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema971_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8365 | 0.6540 | 4.1440 | 0.0129 | 0.3042 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema971_above_at_h` | one_head_filter_pi_star | 125 | 10.2746 | 1.8144 | 0.6640 | 2.7285 | 0.0117 | 0.3280 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema971_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 1.7017 | 0.6453 | 3.6291 | 0.0111 | 0.3094 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema971_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 1.2808 | 0.6029 | 1.2218 | 0.0105 | 0.2426 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema971_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.5778 | 0.6281 | 2.0903 | 0.0089 | 0.3223 | ok | RAN |
| ETHUSDT | 4 | `ema971_above_at_h` | one_head_filter_pi_star | 135 | 11.1413 | 1.1790 | 0.5852 | 0.8230 | 0.0073 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema971_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema971_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema971_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema971_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema971_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
