# Autonomy public-indicator hunt gen 1371

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T025808Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma655_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0643 | 0.6923 | 4.3861 | 0.0247 | 0.4011 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma655_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8534 | 0.6755 | 3.7547 | 0.0208 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma655_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.7778 | 0.6615 | 3.3325 | 0.0123 | 0.3179 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma655_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.6656 | 0.6517 | 3.0629 | 0.0109 | 0.3234 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma655_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5776 | 0.6081 | 2.3100 | 0.0088 | 0.3108 | ok | RAN |
| SOLUSDT | 8 | `sma655_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.5200 | 0.6179 | 1.9413 | 0.0080 | 0.3496 | ok | RAN |
| ETHUSDT | 8 | `sma655_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.2020 | 0.6090 | 0.9800 | 0.0074 | 0.2179 | ok | RAN |
| ETHUSDT | 4 | `sma655_above_at_h` | one_head_filter_pi_star | 137 | 11.3054 | 1.1277 | 0.5839 | 0.6037 | 0.0048 | 0.2190 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma655_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma655_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma655_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma655_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma655_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
