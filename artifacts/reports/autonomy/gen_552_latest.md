# Autonomy public-indicator hunt gen 552

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T212244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma980_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1446 | 0.6995 | 4.5052 | 0.0239 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma980_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8678 | 0.6859 | 3.7332 | 0.0198 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma980_below_at_h` | one_head_filter_pi_star | 237 | 19.3797 | 1.8623 | 0.6540 | 3.9779 | 0.0131 | 0.3207 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma980_below_at_h` | one_head_filter_pi_star | 222 | 18.1531 | 1.7868 | 0.6577 | 3.5911 | 0.0124 | 0.3423 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma980_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.7275 | 0.6504 | 2.4649 | 0.0101 | 0.3008 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma980_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.6424 | 0.6372 | 2.1070 | 0.0089 | 0.3097 | ok | RAN |
| ETHUSDT | 4 | `sma980_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2112 | 0.5833 | 1.0072 | 0.0077 | 0.2024 | ok | RAN |
| ETHUSDT | 8 | `sma980_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.0418 | 0.5473 | 0.2027 | 0.0016 | 0.1959 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma980_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5901 | 0.2353 | -0.8024 | -0.0339 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma980_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
