# Autonomy public-indicator hunt gen 931

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T045311Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma618_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9612 | 0.6786 | 4.1788 | 0.0226 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma618_below_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8593 | 0.6587 | 3.9818 | 0.0206 | 0.3558 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma618_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7495 | 0.6633 | 3.3821 | 0.0116 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma618_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 1.7214 | 0.6618 | 3.3603 | 0.0116 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma618_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.6653 | 0.6211 | 2.6611 | 0.0102 | 0.3230 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma618_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5888 | 0.6259 | 2.2927 | 0.0088 | 0.3165 | ok | RAN |
| ETHUSDT | 4 | `sma618_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.2287 | 0.6127 | 1.1272 | 0.0083 | 0.2139 | ok | RAN |
| ETHUSDT | 8 | `sma618_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 1.2156 | 0.6061 | 1.0667 | 0.0077 | 0.2242 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma618_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma618_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma618_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma618_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma618_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma618_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
