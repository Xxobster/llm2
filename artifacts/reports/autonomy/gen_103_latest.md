# Autonomy public-indicator hunt gen 103

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T161629Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `rr_cross_down_06` | one_head_filter_pi_star | 70 | 5.8766 | 2.1446 | 0.7429 | 2.8788 | 0.0281 | 0.4143 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `rr_cross_up_15` | one_head_filter_pi_star | 271 | 22.1922 | 1.4753 | 0.6236 | 2.7314 | 0.0138 | 0.2878 | ok | RAN |
| BTCUSDT | 8 | `rr_cross_up_15` | one_head_filter_pi_star | 16 | 1.6657 | 1.1969 | 0.4375 | 0.3274 | 0.0128 | 0.0625 | TPM<MIN | RAN |
| SOLUSDT | 8 | `rr_cross_up_15` | one_head_filter_pi_star | 227 | 18.5097 | 1.7954 | 0.6520 | 3.6596 | 0.0100 | 0.2511 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `rr_cross_down_06` | one_head_filter_pi_star | 36 | 3.1770 | 1.3491 | 0.5833 | 0.8265 | 0.0063 | 0.4722 | EBR>35% | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `rr_cross_up_15` | one_head_filter_pi_star | 27 | 2.3146 | 0.9333 | 0.5556 | -0.1452 | -0.0013 | 0.1481 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `rr_cross_up_15` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `rr_cross_down_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `rr_cross_down_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rr_cross_up_15` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rr_cross_down_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rr_wide_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rr_tight_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rr_cross_down_06` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
