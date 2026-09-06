# Autonomy public-indicator hunt gen 051

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T125429Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `er_high_at_h` | one_head_filter_pi_star | 21 | 1.8074 | 6.8826 | 0.8095 | 3.3149 | 0.0599 | 0.5238 | EBR>35% | RAN |
| SOLUSDT | 4 | `er_high_at_h` | one_head_filter_pi_star | 25 | 2.3701 | 4.7746 | 0.8400 | 3.5059 | 0.0472 | 0.6400 | EBR>35% | RAN |
| ETHUSDT | 4 | `er_cross_up_06` | one_head_filter_pi_star | 59 | 4.8729 | 1.5796 | 0.6780 | 1.6013 | 0.0200 | 0.3390 | GATE_CAND | RAN |
| ETHUSDT | 8 | `er_low_at_h` | one_head_filter_pi_star | 190 | 15.6345 | 1.6086 | 0.6421 | 2.8271 | 0.0162 | 0.2632 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `er_low_at_h` | one_head_filter_pi_star | 85 | 7.0056 | 1.9798 | 0.6706 | 2.6314 | 0.0137 | 0.2588 | GATE_CAND | RAN |
| ETHUSDT | 8 | `er_cross_down_03` | one_head_filter_pi_star | 274 | 22.3833 | 1.4756 | 0.6387 | 2.8293 | 0.0133 | 0.2591 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `er_cross_down_03` | one_head_filter_pi_star | 270 | 22.0159 | 1.6224 | 0.6370 | 3.4721 | 0.0087 | 0.2889 | ok | RAN |
| ETHUSDT | 4 | `er_low_at_h` | one_head_filter_pi_star | 95 | 7.8159 | 1.2328 | 0.5579 | 0.8494 | 0.0085 | 0.2842 | ok | RAN |
| SOLUSDT | 8 | `er_low_at_h` | one_head_filter_pi_star | 146 | 11.9821 | 1.4349 | 0.6164 | 1.9282 | 0.0069 | 0.2671 | ok | RAN |
| ETHUSDT | 8 | `er_cross_up_06` | one_head_filter_pi_star | 54 | 4.5258 | 1.1582 | 0.5370 | 0.5212 | 0.0069 | 0.2407 | ok | RAN |
| SOLUSDT | 8 | `er_cross_up_06` | one_head_filter_pi_star | 80 | 6.6653 | 1.2207 | 0.5625 | 0.7600 | 0.0050 | 0.2625 | ok | RAN |
| SOLUSDT | 4 | `er_cross_down_03` | one_head_filter_pi_star | 78 | 6.4378 | 1.2581 | 0.6026 | 0.8626 | 0.0043 | 0.2179 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `er_cross_down_03` | one_head_filter_pi_star | 88 | 7.2926 | 1.0121 | 0.5682 | 0.0453 | 0.0004 | 0.2045 | ok | RAN |
| SOLUSDT | 4 | `er_cross_up_06` | one_head_filter_pi_star | 61 | 5.1484 | 1.0051 | 0.5410 | 0.0175 | 0.0001 | 0.2951 | ok | RAN |
| BTCUSDT | 8 | `er_cross_down_03` | one_head_filter_pi_star | 16 | 1.4683 | 0.4561 | 0.3125 | -1.2249 | -0.0410 | 0.1250 | TPM<MIN | RAN |
| BTCUSDT | 8 | `er_low_at_h` | one_head_filter_pi_star | 11 | 1.3837 | 0.4035 | 0.3636 | -1.3525 | -0.0457 | 0.0909 | TPM<MIN | RAN |
| ETHUSDT | 8 | `er_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `er_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `er_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `er_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `er_cross_up_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `er_cross_down_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `er_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `er_cross_up_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
