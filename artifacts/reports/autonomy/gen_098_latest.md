# Autonomy public-indicator hunt gen 098

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T155717Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `kcw_cross_up_03` | one_head_filter_pi_star | 14 | 1.4312 | 20.3237 | 0.9286 | 3.6328 | 0.0976 | 0.8571 | EBR>35% | RAN |
| ETHUSDT | 8 | `kcw_wide_at_h` | one_head_filter_pi_star | 53 | 4.8543 | 5.0768 | 0.8679 | 4.4561 | 0.0649 | 0.7547 | EBR>35% | RAN |
| ETHUSDT | 4 | `kcw_wide_at_h` | one_head_filter_pi_star | 47 | 4.7845 | 7.0825 | 0.8936 | 4.8147 | 0.0647 | 0.7660 | EBR>35% | RAN |
| SOLUSDT | 4 | `kcw_cross_up_03` | one_head_filter_pi_star | 15 | 1.3834 | 5.2065 | 0.8667 | 2.5866 | 0.0326 | 0.8000 | EBR>35% | RAN |
| SOLUSDT | 4 | `kcw_wide_at_h` | one_head_filter_pi_star | 60 | 5.1747 | 3.9164 | 0.8167 | 4.1553 | 0.0300 | 0.7500 | EBR>35% | RAN |
| SOLUSDT | 8 | `kcw_wide_at_h` | one_head_filter_pi_star | 56 | 5.1647 | 4.2009 | 0.8214 | 4.0092 | 0.0286 | 0.7500 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `kcw_tight_at_h` | one_head_filter_pi_star | 18 | 1.8513 | 0.6840 | 0.6667 | -0.5398 | -0.0022 | 0.0000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `kcw_tight_at_h` | one_head_filter_pi_star | 20 | 2.0545 | 0.6775 | 0.7000 | -0.6013 | -0.0024 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `kcw_tight_at_h` | one_head_filter_pi_star | 21 | 2.1128 | 0.5011 | 0.4762 | -1.1630 | -0.0061 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `kcw_tight_at_h` | one_head_filter_pi_star | 24 | 2.4146 | 0.4974 | 0.5000 | -1.2682 | -0.0069 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `kcw_tight_at_h` | one_head_filter_pi_star | 12 | 2.7056 | 0.1550 | 0.2500 | -3.2207 | -0.0775 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `kcw_tight_at_h` | one_head_filter_pi_star | 13 | 2.9171 | 0.1479 | 0.2308 | -3.3606 | -0.0818 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `kcw_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `kcw_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `kcw_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `kcw_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kcw_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kcw_cross_up_03` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kcw_cross_down_01` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
