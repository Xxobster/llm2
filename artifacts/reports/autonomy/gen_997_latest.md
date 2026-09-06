# Autonomy public-indicator hunt gen 997

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T094438Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret197_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1340 | 0.7006 | 4.6380 | 0.0257 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret197_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.9845 | 0.6886 | 4.1611 | 0.0232 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret197_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 1.9902 | 0.6848 | 3.7145 | 0.0151 | 0.3758 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret197_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.0175 | 0.6708 | 3.5561 | 0.0151 | 0.3727 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret197_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.5434 | 0.6237 | 2.4424 | 0.0083 | 0.2688 | ok | RAN |
| ETHUSDT | 8 | `ret197_pos_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2256 | 0.6050 | 1.1766 | 0.0080 | 0.2200 | ok | RAN |
| SOLUSDT | 4 | `ret197_pos_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.4108 | 0.6167 | 1.9499 | 0.0065 | 0.2722 | ok | RAN |
| ETHUSDT | 4 | `ret197_pos_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.1555 | 0.5850 | 0.8356 | 0.0056 | 0.2250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret197_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6903 | 0.3333 | -0.6386 | -0.0328 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret197_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0448 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret197_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret197_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret197_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret197_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
