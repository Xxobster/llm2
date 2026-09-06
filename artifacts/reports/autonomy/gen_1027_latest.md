# Autonomy public-indicator hunt gen 1027

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T135517Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma601_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0106 | 0.6834 | 4.4104 | 0.0231 | 0.3668 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma601_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0139 | 0.6811 | 4.2091 | 0.0229 | 0.3946 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma601_below_at_h` | one_head_filter_pi_star | 214 | 17.4093 | 1.9337 | 0.6729 | 4.0061 | 0.0133 | 0.3131 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma601_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8315 | 0.6719 | 3.5994 | 0.0125 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma601_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.5972 | 0.6135 | 2.4926 | 0.0093 | 0.3190 | ok | RAN |
| SOLUSDT | 8 | `sma601_above_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.5591 | 0.6169 | 2.3387 | 0.0088 | 0.2987 | ok | RAN |
| ETHUSDT | 8 | `sma601_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1766 | 0.5988 | 0.9238 | 0.0065 | 0.2335 | ok | RAN |
| ETHUSDT | 4 | `sma601_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.0997 | 0.5955 | 0.5316 | 0.0037 | 0.1966 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma601_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma601_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma601_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma601_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma601_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma601_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
