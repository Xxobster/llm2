# Autonomy public-indicator hunt gen 819

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T172816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma522_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.1023 | 0.6939 | 4.7400 | 0.0243 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma522_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0429 | 0.6848 | 4.4015 | 0.0241 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma522_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.8726 | 0.6751 | 3.7590 | 0.0131 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma522_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.7792 | 0.6684 | 3.4036 | 0.0122 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma522_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.7258 | 0.6236 | 3.0489 | 0.0107 | 0.2809 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma522_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2805 | 0.6049 | 1.3314 | 0.0096 | 0.2160 | ok | RAN |
| SOLUSDT | 4 | `sma522_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.6287 | 0.6193 | 2.6813 | 0.0094 | 0.2898 | ok | RAN |
| ETHUSDT | 4 | `sma522_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.1922 | 0.5956 | 1.0208 | 0.0068 | 0.2295 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma522_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma522_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma522_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma522_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma522_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma522_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
