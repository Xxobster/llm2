# Autonomy public-indicator hunt gen 1429

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T135609Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret247_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.2278 | 0.7066 | 4.6527 | 0.0277 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret247_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0984 | 0.7006 | 4.4499 | 0.0249 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret247_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.9440 | 0.6631 | 3.8495 | 0.0135 | 0.3476 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret247_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.8874 | 0.6561 | 3.6657 | 0.0130 | 0.3598 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret247_pos_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2374 | 0.5989 | 1.2200 | 0.0084 | 0.2198 | ok | RAN |
| SOLUSDT | 4 | `ret247_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5252 | 0.6207 | 2.3220 | 0.0081 | 0.2701 | ok | RAN |
| SOLUSDT | 8 | `ret247_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.5239 | 0.6243 | 2.3150 | 0.0079 | 0.2948 | ok | RAN |
| ETHUSDT | 4 | `ret247_pos_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1733 | 0.5976 | 0.8482 | 0.0063 | 0.2378 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret247_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret247_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret247_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret247_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret247_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret247_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
