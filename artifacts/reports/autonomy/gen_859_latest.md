# Autonomy public-indicator hunt gen 859

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T211930Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma558_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.1805 | 0.6971 | 4.6479 | 0.0257 | 0.4114 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma558_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 2.0412 | 0.6943 | 4.5179 | 0.0240 | 0.3834 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma558_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.9254 | 0.6731 | 4.0312 | 0.0136 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma558_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8710 | 0.6634 | 3.7777 | 0.0128 | 0.3267 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma558_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.5658 | 0.6182 | 2.4298 | 0.0088 | 0.3030 | ok | RAN |
| SOLUSDT | 8 | `sma558_above_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.5159 | 0.6048 | 2.2879 | 0.0080 | 0.2754 | ok | RAN |
| ETHUSDT | 4 | `sma558_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.1656 | 0.5967 | 0.8620 | 0.0061 | 0.2210 | ok | RAN |
| ETHUSDT | 8 | `sma558_above_at_h` | one_head_filter_pi_star | 172 | 14.1937 | 1.1000 | 0.5814 | 0.5324 | 0.0038 | 0.2209 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma558_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma558_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma558_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma558_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma558_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma558_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
