# Autonomy public-indicator hunt gen 824

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T175530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1660_below_at_h` | one_head_filter_pi_star | 269 | 21.9748 | 1.7150 | 0.6468 | 3.8057 | 0.0174 | 0.3234 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1660_below_at_h` | one_head_filter_pi_star | 283 | 23.1185 | 1.6776 | 0.6466 | 3.8070 | 0.0169 | 0.3145 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1660_above_at_h` | one_head_filter_pi_star | 58 | 4.8214 | 1.9023 | 0.7069 | 2.0625 | 0.0132 | 0.3276 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1660_above_at_h` | one_head_filter_pi_star | 46 | 3.9983 | 2.0435 | 0.7174 | 2.0532 | 0.0126 | 0.3261 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma1660_below_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.7336 | 0.6341 | 4.0019 | 0.0110 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1660_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7160 | 0.6343 | 3.8794 | 0.0107 | 0.3172 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1660_above_at_h` | one_head_filter_pi_star | 65 | 5.5310 | 1.1392 | 0.5692 | 0.4543 | 0.0059 | 0.2154 | ok | RAN |
| ETHUSDT | 4 | `sma1660_above_at_h` | one_head_filter_pi_star | 64 | 5.4531 | 1.0453 | 0.5781 | 0.1598 | 0.0020 | 0.2344 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1660_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1660_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3351 | 0.2143 | -1.4392 | -0.0770 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1660_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1660_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1660_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
