# Autonomy public-indicator hunt gen 096

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T154903Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `vr_low_at_h` | one_head_filter_pi_star | 12 | 1.5172 | 2.5419 | 0.7500 | 1.6257 | 0.1768 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `vr_low_at_h` | one_head_filter_pi_star | 76 | 6.2184 | 2.4211 | 0.7500 | 3.1661 | 0.0325 | 0.4474 | EBR>35% | RAN |
| ETHUSDT | 4 | `vr_cross_down_07` | one_head_filter_pi_star | 61 | 5.3409 | 2.5145 | 0.7049 | 2.7859 | 0.0301 | 0.3279 | GATE_CAND | RAN |
| ETHUSDT | 8 | `vr_cross_down_07` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `vr_low_at_h` | one_head_filter_pi_star | 78 | 6.5335 | 1.6173 | 0.6282 | 1.9672 | 0.0129 | 0.5513 | EBR>35% | RAN |
| SOLUSDT | 8 | `vr_cross_down_07` | one_head_filter_pi_star | 367 | 29.8562 | 1.7001 | 0.6431 | 4.2954 | 0.0104 | 0.3188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `vr_cross_up_15` | one_head_filter_pi_star | 20 | 1.6993 | 1.5427 | 0.6000 | 0.8506 | 0.0086 | 0.1500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `vr_cross_down_07` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| SOLUSDT | 8 | `vr_cross_up_15` | one_head_filter_pi_star | 214 | 17.4496 | 1.3547 | 0.6075 | 1.9115 | 0.0055 | 0.2009 | ok | RAN |
| ETHUSDT | 8 | `vr_cross_up_15` | one_head_filter_pi_star | 218 | 17.9269 | 1.1151 | 0.5780 | 0.7133 | 0.0038 | 0.2156 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `vr_cross_down_07` | one_head_filter_pi_star | 19 | 1.6776 | 0.7968 | 0.5263 | -0.4671 | -0.0060 | 0.4737 | EBR>35% | RAN |
| ETHUSDT | 4 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `vr_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `vr_cross_up_15` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `vr_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vr_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vr_cross_up_15` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `vr_cross_down_07` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `vr_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `vr_cross_up_15` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
