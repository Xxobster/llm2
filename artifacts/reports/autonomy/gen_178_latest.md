# Autonomy public-indicator hunt gen 178

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T210908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret56_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.7528 | 0.6735 | 3.7325 | 0.0203 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret56_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.7228 | 0.6684 | 3.6615 | 0.0193 | 0.3627 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret56_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1551 | 0.6946 | 4.0961 | 0.0170 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret56_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0639 | 0.6845 | 3.8923 | 0.0165 | 0.3988 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret56_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.4062 | 0.6211 | 1.9010 | 0.0122 | 0.2474 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret56_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.3171 | 0.6022 | 1.5419 | 0.0097 | 0.2366 | ok | RAN |
| SOLUSDT | 8 | `ret56_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.4428 | 0.6020 | 2.2724 | 0.0064 | 0.2587 | ok | RAN |
| SOLUSDT | 4 | `ret56_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.4159 | 0.6029 | 2.1440 | 0.0061 | 0.2598 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret56_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret56_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret56_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret56_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret56_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret56_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
