# Autonomy public-indicator hunt gen 995

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T092619Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma672_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0495 | 0.6898 | 4.3375 | 0.0238 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma672_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0463 | 0.6910 | 4.2648 | 0.0232 | 0.3876 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma672_above_at_h` | one_head_filter_pi_star | 108 | 8.8565 | 1.8913 | 0.6481 | 2.8363 | 0.0126 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma672_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.3296 | 0.6242 | 1.5197 | 0.0116 | 0.2293 | ok | RAN |
| SOLUSDT | 8 | `sma672_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.7335 | 0.6538 | 3.3420 | 0.0114 | 0.3269 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma672_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.6789 | 0.6526 | 3.1420 | 0.0108 | 0.3146 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma672_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 1.2400 | 0.6027 | 1.1322 | 0.0086 | 0.2192 | ok | RAN |
| SOLUSDT | 4 | `sma672_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.4788 | 0.6031 | 1.8867 | 0.0077 | 0.3130 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma672_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma672_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma672_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma672_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma672_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma672_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
