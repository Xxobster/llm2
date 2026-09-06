# Autonomy public-indicator hunt gen 794

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T150744Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret648_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.9624 | 0.6832 | 4.2678 | 0.0214 | 0.3465 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret648_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.8995 | 0.6776 | 3.7908 | 0.0197 | 0.3497 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret648_neg_at_h` | one_head_filter_pi_star | 224 | 18.3167 | 1.8999 | 0.6696 | 4.0552 | 0.0151 | 0.3348 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret648_neg_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 1.8526 | 0.6651 | 3.7880 | 0.0143 | 0.3488 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret648_pos_at_h` | one_head_filter_pi_star | 110 | 9.1424 | 1.9082 | 0.6909 | 2.8598 | 0.0113 | 0.2909 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret648_pos_at_h` | one_head_filter_pi_star | 104 | 8.6437 | 1.7289 | 0.6538 | 2.3713 | 0.0096 | 0.2500 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret648_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.1559 | 0.5611 | 0.8067 | 0.0064 | 0.2333 | ok | RAN |
| ETHUSDT | 8 | `ret648_pos_at_h` | one_head_filter_pi_star | 159 | 13.1220 | 1.1362 | 0.5535 | 0.6530 | 0.0056 | 0.2327 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret648_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5010 | 0.2941 | -1.0496 | -0.0537 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret648_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4695 | 0.2941 | -1.1808 | -0.0597 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret648_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret648_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret648_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret648_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
