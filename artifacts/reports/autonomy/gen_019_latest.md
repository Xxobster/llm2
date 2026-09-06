# Autonomy public-indicator hunt gen 019

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T090349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `uo_cross_up_30` | one_head_filter_pi_star | 30 | 3.0462 | 3.6797 | 0.8000 | 3.0918 | 0.0567 | 0.4667 | EBR>35% | RAN |
| ETHUSDT | 8 | `uo_cross_up_30` | one_head_filter_pi_star | 33 | 3.3508 | 3.7014 | 0.7879 | 3.2187 | 0.0547 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 4 | `uo_cross_up_30` | one_head_filter_pi_star | 27 | 2.3603 | 2.4946 | 0.7778 | 2.4419 | 0.0286 | 0.5556 | EBR>35% | RAN |
| SOLUSDT | 8 | `uo_cross_up_30` | one_head_filter_pi_star | 31 | 2.6907 | 2.0938 | 0.7419 | 2.1310 | 0.0225 | 0.4839 | EBR>35% | RAN |
| ETHUSDT | 8 | `uo_cross_down_70` | one_head_filter_pi_star | 21 | 1.9453 | 1.6796 | 0.5714 | 0.8862 | 0.0187 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `uo_cross_down_70` | one_head_filter_pi_star | 22 | 2.0380 | 1.4734 | 0.5909 | 0.7068 | 0.0145 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 8 | `uo_cross_down_70` | one_head_filter_pi_star | 27 | 2.7637 | 1.6115 | 0.6296 | 1.1976 | 0.0125 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `uo_cross_down_70` | one_head_filter_pi_star | 27 | 2.7637 | 1.5198 | 0.6296 | 1.0417 | 0.0103 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `uo_cross_down_70` | one_head_filter_pi_star | 12 | 1.3634 | 0.9958 | 0.5000 | -0.0069 | -0.0004 | 0.0833 | TPM<MIN | RAN |
| BTCUSDT | 8 | `uo_cross_down_70` | one_head_filter_pi_star | 12 | 1.3634 | 0.9958 | 0.5000 | -0.0069 | -0.0005 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 4 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `uo_cross_up_30` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `uo_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `uo_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `uo_cross_up_30` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
