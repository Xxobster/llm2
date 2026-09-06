# Autonomy public-indicator hunt gen 592

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T000059Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1080_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.3789 | 0.7158 | 4.6715 | 0.0264 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma1080_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8645 | 0.6650 | 3.7065 | 0.0199 | 0.3695 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1080_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 1.7479 | 0.6441 | 3.5931 | 0.0117 | 0.3178 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1080_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.7060 | 0.6375 | 3.5133 | 0.0111 | 0.3147 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1080_above_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.7698 | 0.6452 | 2.5715 | 0.0106 | 0.2984 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1080_above_at_h` | one_head_filter_pi_star | 120 | 9.8406 | 1.5992 | 0.6333 | 2.0676 | 0.0090 | 0.3333 | ok | RAN |
| ETHUSDT | 8 | `sma1080_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 1.1580 | 0.5766 | 0.7299 | 0.0062 | 0.2044 | ok | RAN |
| ETHUSDT | 4 | `sma1080_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1065 | 0.5724 | 0.5105 | 0.0042 | 0.2105 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1080_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1080_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
