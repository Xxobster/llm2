# Autonomy public-indicator hunt gen 416

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T055758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma640_below_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.9503 | 0.6699 | 4.3772 | 0.0225 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma640_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9585 | 0.6757 | 4.1652 | 0.0225 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma640_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8276 | 0.6750 | 3.5916 | 0.0129 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma640_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.7830 | 0.6588 | 3.4975 | 0.0120 | 0.3270 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma640_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.5246 | 0.6026 | 2.2083 | 0.0082 | 0.3179 | ok | RAN |
| SOLUSDT | 8 | `sma640_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.4782 | 0.6071 | 1.9833 | 0.0079 | 0.3286 | ok | RAN |
| ETHUSDT | 8 | `sma640_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1927 | 0.6037 | 0.9538 | 0.0072 | 0.2256 | ok | RAN |
| ETHUSDT | 4 | `sma640_above_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.1542 | 0.5882 | 0.7600 | 0.0058 | 0.2092 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma640_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma640_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
