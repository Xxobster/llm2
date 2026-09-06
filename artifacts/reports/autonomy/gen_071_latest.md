# Autonomy public-indicator hunt gen 071

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T141253Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `rw_wide_at_h` | one_head_filter_pi_star | 12 | 1.1569 | 2.7406 | 0.7500 | 1.6161 | 0.1678 | 0.3333 | TPM<MIN | RAN |
| BTCUSDT | 8 | `rw_wide_at_h` | one_head_filter_pi_star | 13 | 1.2533 | 2.4761 | 0.6923 | 1.5099 | 0.1406 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rw_wide_at_h` | one_head_filter_pi_star | 247 | 20.2002 | 2.1231 | 0.7085 | 4.9114 | 0.0295 | 0.3887 | EBR>35% | RAN |
| ETHUSDT | 8 | `rw_wide_at_h` | one_head_filter_pi_star | 259 | 21.0702 | 2.0222 | 0.6950 | 4.7422 | 0.0283 | 0.4015 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `rw_wide_at_h` | one_head_filter_pi_star | 292 | 23.8771 | 1.8401 | 0.6644 | 4.3089 | 0.0138 | 0.3870 | EBR>35% | RAN |
| SOLUSDT | 8 | `rw_wide_at_h` | one_head_filter_pi_star | 293 | 23.9589 | 1.8242 | 0.6553 | 4.3073 | 0.0135 | 0.3891 | EBR>35% | RAN |
| SOLUSDT | 8 | `rw_cross_up_02` | one_head_filter_pi_star | 63 | 5.2882 | 1.5888 | 0.6190 | 1.6167 | 0.0128 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `rw_cross_up_02` | one_head_filter_pi_star | 42 | 3.5110 | 1.4453 | 0.6190 | 1.0482 | 0.0098 | 0.2143 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rw_cross_up_02` | one_head_filter_pi_star | 81 | 6.6331 | 1.1699 | 0.5802 | 0.5945 | 0.0071 | 0.2469 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rw_cross_up_02` | one_head_filter_pi_star | 40 | 3.2946 | 1.0158 | 0.5500 | 0.0441 | 0.0008 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rw_tight_at_h` | one_head_filter_pi_star | 20 | 2.0032 | 0.9009 | 0.5500 | -0.2072 | -0.0012 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rw_tight_at_h` | one_head_filter_pi_star | 21 | 2.1034 | 0.5945 | 0.5238 | -0.9164 | -0.0058 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `rw_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `rw_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rw_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `rw_cross_up_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rw_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `rw_cross_up_02` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
