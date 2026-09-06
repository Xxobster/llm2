# Autonomy public-indicator hunt gen 502

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T180242Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma220_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0459 | 0.6931 | 4.6032 | 0.0241 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma220_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9936 | 0.6911 | 4.4335 | 0.0230 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma220_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2487 | 0.7011 | 4.3596 | 0.0179 | 0.3793 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma220_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2124 | 0.6946 | 4.1671 | 0.0173 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma220_above_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.3406 | 0.6158 | 1.5977 | 0.0112 | 0.2316 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma220_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3419 | 0.5922 | 1.8075 | 0.0054 | 0.2670 | ok | RAN |
| SOLUSDT | 4 | `wma220_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.2681 | 0.5871 | 1.4275 | 0.0043 | 0.2637 | ok | RAN |
| ETHUSDT | 4 | `wma220_above_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1107 | 0.5885 | 0.5893 | 0.0041 | 0.2188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma220_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
