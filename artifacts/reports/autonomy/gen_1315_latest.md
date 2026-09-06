# Autonomy public-indicator hunt gen 1315

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T214618Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma646_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0600 | 0.6898 | 4.4686 | 0.0246 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma646_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9932 | 0.6737 | 4.2756 | 0.0227 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma646_below_at_h` | one_head_filter_pi_star | 199 | 16.1890 | 1.8831 | 0.6784 | 3.7951 | 0.0133 | 0.3216 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma646_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.7388 | 0.6553 | 3.3659 | 0.0114 | 0.3155 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma646_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.5630 | 0.6087 | 2.3348 | 0.0087 | 0.3106 | ok | RAN |
| SOLUSDT | 8 | `sma646_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5221 | 0.6081 | 2.1756 | 0.0084 | 0.3176 | ok | RAN |
| ETHUSDT | 8 | `sma646_above_at_h` | one_head_filter_pi_star | 156 | 12.8230 | 1.1800 | 0.6090 | 0.9006 | 0.0066 | 0.2244 | ok | RAN |
| ETHUSDT | 4 | `sma646_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1706 | 0.5965 | 0.8796 | 0.0064 | 0.2281 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma646_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma646_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma646_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma646_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma646_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma646_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
