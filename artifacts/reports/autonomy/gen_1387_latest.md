# Autonomy public-indicator hunt gen 1387

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T042946Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma657_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0758 | 0.6878 | 4.5243 | 0.0251 | 0.3915 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma657_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9683 | 0.6685 | 4.0024 | 0.0225 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma657_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.6972 | 0.6552 | 3.1615 | 0.0113 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma657_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.6611 | 0.6535 | 3.0940 | 0.0109 | 0.3218 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma657_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.6490 | 0.6290 | 2.4201 | 0.0095 | 0.3387 | ok | RAN |
| SOLUSDT | 4 | `sma657_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.6032 | 0.6200 | 2.4234 | 0.0093 | 0.3200 | ok | RAN |
| ETHUSDT | 8 | `sma657_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2255 | 0.6144 | 1.0842 | 0.0083 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `sma657_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1179 | 0.5855 | 0.5866 | 0.0044 | 0.2105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma657_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma657_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma657_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma657_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma657_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma657_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
