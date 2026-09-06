# Autonomy public-indicator hunt gen 1299

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T201526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma644_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0461 | 0.6825 | 4.3020 | 0.0244 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma644_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0234 | 0.6848 | 4.2835 | 0.0232 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma644_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.8146 | 0.6650 | 3.5246 | 0.0126 | 0.3204 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma644_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.7414 | 0.6569 | 3.3716 | 0.0118 | 0.3235 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma644_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.6643 | 0.6275 | 2.6925 | 0.0104 | 0.3203 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma644_above_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.6021 | 0.6234 | 2.4627 | 0.0094 | 0.3052 | ok | RAN |
| ETHUSDT | 4 | `sma644_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.1945 | 0.5948 | 0.9386 | 0.0073 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `sma644_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 1.1863 | 0.6081 | 0.8751 | 0.0069 | 0.2297 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma644_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma644_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma644_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma644_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma644_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma644_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
