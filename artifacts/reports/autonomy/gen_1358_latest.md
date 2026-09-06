# Autonomy public-indicator hunt gen 1358

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T014519Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma755_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1590 | 0.7037 | 4.8392 | 0.0254 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma755_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0769 | 0.6898 | 4.5151 | 0.0243 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma755_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.7876 | 0.6683 | 3.5120 | 0.0120 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma755_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7631 | 0.6598 | 3.3188 | 0.0116 | 0.3351 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma755_above_at_h` | one_head_filter_pi_star | 179 | 14.6789 | 1.5729 | 0.6089 | 2.5924 | 0.0092 | 0.3017 | ok | RAN |
| SOLUSDT | 8 | `wma755_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5482 | 0.6105 | 2.4422 | 0.0085 | 0.2849 | ok | RAN |
| ETHUSDT | 8 | `wma755_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.2434 | 0.5988 | 1.2102 | 0.0083 | 0.2275 | ok | RAN |
| ETHUSDT | 4 | `wma755_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.1951 | 0.5954 | 1.0141 | 0.0070 | 0.2197 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma755_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma755_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma755_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma755_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma755_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
