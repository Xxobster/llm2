# Autonomy public-indicator hunt gen 915

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T030522Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma606_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0144 | 0.6878 | 4.3149 | 0.0238 | 0.3968 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma606_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9416 | 0.6800 | 4.2182 | 0.0219 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma606_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8448 | 0.6667 | 3.6826 | 0.0127 | 0.3283 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma606_below_at_h` | one_head_filter_pi_star | 216 | 17.6625 | 1.8212 | 0.6574 | 3.7354 | 0.0122 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma606_above_at_h` | one_head_filter_pi_star | 163 | 13.3668 | 1.6490 | 0.6196 | 2.7331 | 0.0101 | 0.3190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma606_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.5334 | 0.6194 | 2.2638 | 0.0084 | 0.3032 | ok | RAN |
| ETHUSDT | 8 | `sma606_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1489 | 0.5976 | 0.7677 | 0.0056 | 0.2317 | ok | RAN |
| ETHUSDT | 4 | `sma606_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.1433 | 0.6023 | 0.7584 | 0.0052 | 0.1989 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma606_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma606_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma606_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma606_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma606_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma606_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
