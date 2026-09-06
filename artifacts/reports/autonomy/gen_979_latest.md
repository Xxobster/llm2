# Autonomy public-indicator hunt gen 979

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T100150Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma654_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9863 | 0.6848 | 4.1966 | 0.0239 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma654_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 1.8100 | 0.6698 | 3.9121 | 0.0204 | 0.3581 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma654_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 1.7707 | 0.6635 | 3.4337 | 0.0118 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma654_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.6374 | 0.6485 | 2.9938 | 0.0104 | 0.3168 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma654_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.5818 | 0.6190 | 2.3461 | 0.0094 | 0.3265 | ok | RAN |
| SOLUSDT | 4 | `sma654_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.4794 | 0.5957 | 1.9057 | 0.0080 | 0.3191 | ok | RAN |
| ETHUSDT | 4 | `sma654_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.1680 | 0.5959 | 0.7955 | 0.0061 | 0.2260 | ok | RAN |
| ETHUSDT | 8 | `sma654_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1525 | 0.6039 | 0.7392 | 0.0056 | 0.2208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma654_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma654_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma654_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma654_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma654_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma654_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
