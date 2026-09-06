# Autonomy public-indicator hunt gen 368

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T184335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma520_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.1017 | 0.6966 | 4.5347 | 0.0257 | 0.4045 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma520_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.9080 | 0.6818 | 3.9635 | 0.0217 | 0.3920 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma520_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.9077 | 0.6811 | 3.6810 | 0.0133 | 0.3459 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma520_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.8616 | 0.6791 | 3.6501 | 0.0132 | 0.3422 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma520_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.6708 | 0.6216 | 2.9134 | 0.0101 | 0.2811 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma520_above_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.2505 | 0.5935 | 1.1846 | 0.0089 | 0.2129 | ok | RAN |
| SOLUSDT | 4 | `sma520_above_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.5105 | 0.6023 | 2.2562 | 0.0080 | 0.2982 | ok | RAN |
| ETHUSDT | 4 | `sma520_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2012 | 0.5969 | 1.0906 | 0.0071 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma520_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma520_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
