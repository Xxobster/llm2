# Autonomy public-indicator hunt gen 892

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T003727Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema875_below_at_h` | one_head_filter_pi_star | 210 | 17.1551 | 1.9829 | 0.6810 | 4.1072 | 0.0225 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema875_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 1.8437 | 0.6653 | 3.9954 | 0.0197 | 0.3475 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema875_above_at_h` | one_head_filter_pi_star | 141 | 11.5900 | 1.3451 | 0.6170 | 1.5599 | 0.0126 | 0.2411 | ok | RAN |
| SOLUSDT | 4 | `ema875_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 1.7040 | 0.6411 | 3.4971 | 0.0113 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema875_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 1.7027 | 0.6409 | 3.6753 | 0.0110 | 0.2973 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema875_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.7077 | 0.6452 | 2.4656 | 0.0105 | 0.3306 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema875_above_at_h` | one_head_filter_pi_star | 129 | 10.5187 | 1.6540 | 0.6279 | 2.4200 | 0.0095 | 0.3178 | ok | RAN |
| ETHUSDT | 8 | `ema875_above_at_h` | one_head_filter_pi_star | 138 | 11.3880 | 1.1546 | 0.5870 | 0.7403 | 0.0063 | 0.2101 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema875_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0408 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema875_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema875_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema875_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema875_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema875_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
