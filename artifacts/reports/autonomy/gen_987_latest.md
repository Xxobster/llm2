# Autonomy public-indicator hunt gen 987

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T172742Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma666_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9331 | 0.6802 | 4.0851 | 0.0222 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma666_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9726 | 0.6739 | 4.1113 | 0.0221 | 0.3913 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma666_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8565 | 0.6717 | 3.5679 | 0.0128 | 0.3283 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma666_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.6976 | 0.6602 | 3.2516 | 0.0110 | 0.3350 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma666_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2989 | 0.6196 | 1.4350 | 0.0101 | 0.2270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma666_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.5269 | 0.6028 | 2.1041 | 0.0083 | 0.3191 | ok | RAN |
| SOLUSDT | 8 | `sma666_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.5015 | 0.6119 | 2.0625 | 0.0081 | 0.3284 | ok | RAN |
| ETHUSDT | 4 | `sma666_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1112 | 0.5875 | 0.5731 | 0.0042 | 0.2125 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma666_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma666_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma666_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma666_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma666_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma666_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
