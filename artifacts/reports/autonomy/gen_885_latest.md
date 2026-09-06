# Autonomy public-indicator hunt gen 885

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T235531Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret169_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.1053 | 0.6951 | 4.4222 | 0.0265 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret169_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0599 | 0.6966 | 4.4523 | 0.0256 | 0.3876 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret169_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1207 | 0.6707 | 4.0080 | 0.0158 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret169_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.0676 | 0.6727 | 3.8382 | 0.0156 | 0.3758 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret169_pos_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.2565 | 0.6103 | 1.3214 | 0.0083 | 0.2256 | ok | RAN |
| SOLUSDT | 8 | `ret169_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4404 | 0.6020 | 2.1580 | 0.0069 | 0.2602 | ok | RAN |
| ETHUSDT | 4 | `ret169_pos_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1945 | 0.5938 | 1.0478 | 0.0065 | 0.2135 | ok | RAN |
| SOLUSDT | 4 | `ret169_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3746 | 0.6020 | 1.8825 | 0.0059 | 0.2551 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret169_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret169_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret169_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret169_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret169_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret169_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
