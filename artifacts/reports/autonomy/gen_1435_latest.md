# Autonomy public-indicator hunt gen 1435

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T165308Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma664_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1063 | 0.6906 | 4.4897 | 0.0244 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma664_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0114 | 0.6811 | 4.2912 | 0.0231 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma664_below_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.8094 | 0.6587 | 3.6003 | 0.0120 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma664_below_at_h` | one_head_filter_pi_star | 204 | 16.5958 | 1.6494 | 0.6520 | 3.0415 | 0.0108 | 0.3235 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma664_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.6008 | 0.6154 | 2.3998 | 0.0093 | 0.3154 | ok | RAN |
| SOLUSDT | 4 | `sma664_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5512 | 0.6187 | 2.1731 | 0.0086 | 0.3165 | ok | RAN |
| ETHUSDT | 4 | `sma664_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.2015 | 0.5986 | 0.9357 | 0.0072 | 0.2245 | ok | RAN |
| ETHUSDT | 8 | `sma664_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1317 | 0.5963 | 0.6654 | 0.0048 | 0.2112 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma664_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma664_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0432 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma664_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma664_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma664_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma664_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
