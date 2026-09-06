# Autonomy public-indicator hunt gen 1555

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T075650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma682_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1437 | 0.6940 | 4.5637 | 0.0250 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma682_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0509 | 0.6757 | 4.4269 | 0.0232 | 0.3730 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma682_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.7474 | 0.6603 | 3.3459 | 0.0117 | 0.3206 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma682_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.7679 | 0.6553 | 3.4425 | 0.0117 | 0.3204 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma682_above_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.6686 | 0.6311 | 2.4522 | 0.0094 | 0.3115 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma682_above_at_h` | one_head_filter_pi_star | 153 | 12.5468 | 1.5480 | 0.6144 | 2.2671 | 0.0089 | 0.3137 | ok | RAN |
| ETHUSDT | 4 | `sma682_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.2222 | 0.5903 | 1.0222 | 0.0078 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `sma682_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.1838 | 0.6042 | 0.8611 | 0.0068 | 0.2153 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma682_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma682_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma682_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma682_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma682_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma682_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
