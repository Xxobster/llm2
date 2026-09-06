# Autonomy public-indicator hunt gen 1323

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T222922Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma647_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.1121 | 0.6935 | 4.4955 | 0.0251 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma647_below_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.9076 | 0.6796 | 4.1656 | 0.0216 | 0.3738 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma647_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 1.7970 | 0.6600 | 3.4892 | 0.0120 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma647_below_at_h` | one_head_filter_pi_star | 199 | 16.1890 | 1.7042 | 0.6583 | 3.1773 | 0.0112 | 0.3266 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma647_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.5798 | 0.6172 | 2.2722 | 0.0088 | 0.3203 | ok | RAN |
| SOLUSDT | 4 | `sma647_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.5328 | 0.6071 | 2.1263 | 0.0084 | 0.3286 | ok | RAN |
| ETHUSDT | 8 | `sma647_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.1924 | 0.5941 | 0.9922 | 0.0070 | 0.2235 | ok | RAN |
| ETHUSDT | 4 | `sma647_above_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.1462 | 0.5897 | 0.7326 | 0.0056 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma647_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma647_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma647_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma647_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma647_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma647_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
