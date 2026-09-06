# Autonomy public-indicator hunt gen 1198

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T100537Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma655_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1802 | 0.7104 | 4.7439 | 0.0254 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma655_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.1123 | 0.6944 | 4.6226 | 0.0247 | 0.3833 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma655_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.9920 | 0.6717 | 4.0897 | 0.0144 | 0.3535 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma655_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8153 | 0.6602 | 3.5949 | 0.0127 | 0.3398 | GATE_CAND | RAN |
| ETHUSDT | 8 | `wma655_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.3323 | 0.6196 | 1.5684 | 0.0111 | 0.2086 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma655_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2672 | 0.6082 | 1.3332 | 0.0093 | 0.2164 | ok | RAN |
| SOLUSDT | 4 | `wma655_above_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5590 | 0.6092 | 2.4768 | 0.0086 | 0.2874 | ok | RAN |
| SOLUSDT | 8 | `wma655_above_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.4842 | 0.6163 | 2.2085 | 0.0078 | 0.2791 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma655_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma655_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
