# Autonomy public-indicator hunt gen 097

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T155302Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `bbw_high_at_h` | one_head_filter_pi_star | 13 | 1.2533 | 2.4761 | 0.6923 | 1.5099 | 0.1458 | 0.3077 | TPM<MIN | RAN |
| BTCUSDT | 8 | `bbw_high_at_h` | one_head_filter_pi_star | 14 | 1.3497 | 2.3168 | 0.6429 | 1.4360 | 0.1211 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `bbw_high_at_h` | one_head_filter_pi_star | 212 | 17.5361 | 2.0451 | 0.7123 | 4.3332 | 0.0275 | 0.4104 | EBR>35% | RAN |
| ETHUSDT | 8 | `bbw_high_at_h` | one_head_filter_pi_star | 238 | 19.3618 | 1.9355 | 0.6849 | 4.2219 | 0.0260 | 0.4034 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `bbw_high_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 1.8353 | 0.6615 | 4.2349 | 0.0138 | 0.4038 | EBR>35% | RAN |
| SOLUSDT | 8 | `bbw_high_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.7195 | 0.6452 | 3.9158 | 0.0123 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `bbw_cross_up_p02` | one_head_filter_pi_star | 136 | 11.1370 | 1.2487 | 0.5956 | 1.0987 | 0.0098 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `bbw_cross_up_p02` | one_head_filter_pi_star | 124 | 10.3092 | 1.2405 | 0.5645 | 1.0625 | 0.0054 | 0.2016 | ok | RAN |
| SOLUSDT | 4 | `bbw_cross_up_p02` | one_head_filter_pi_star | 99 | 8.3140 | 1.1447 | 0.5556 | 0.5890 | 0.0035 | 0.1919 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `bbw_cross_up_p02` | one_head_filter_pi_star | 85 | 6.9607 | 1.0325 | 0.5529 | 0.1247 | 0.0014 | 0.2353 | ok | RAN |
| ETHUSDT | 8 | `bbw_low_at_h` | one_head_filter_pi_star | 18 | 1.8029 | 0.6984 | 0.5000 | -0.6569 | -0.0038 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `bbw_low_at_h` | one_head_filter_pi_star | 19 | 1.9031 | 0.6425 | 0.5263 | -0.7440 | -0.0049 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `bbw_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `bbw_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bbw_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bbw_cross_up_p02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bbw_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bbw_cross_up_p02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `bbw_cross_down_p008` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
