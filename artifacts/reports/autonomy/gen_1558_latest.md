# Autonomy public-indicator hunt gen 1558

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T081346Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma421_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0081 | 0.6952 | 4.3772 | 0.0237 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma421_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9554 | 0.6961 | 4.2271 | 0.0228 | 0.3978 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma421_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2341 | 0.6936 | 4.3706 | 0.0169 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma421_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1862 | 0.6927 | 4.2839 | 0.0164 | 0.3799 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma421_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2995 | 0.6075 | 1.5263 | 0.0101 | 0.2151 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma421_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2193 | 0.5914 | 1.1601 | 0.0076 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `wma421_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3929 | 0.6011 | 1.8941 | 0.0060 | 0.2568 | ok | RAN |
| SOLUSDT | 4 | `wma421_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3320 | 0.5909 | 1.7354 | 0.0054 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma421_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma421_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma421_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma421_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma421_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma421_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
