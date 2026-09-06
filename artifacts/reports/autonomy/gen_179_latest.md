# Autonomy public-indicator hunt gen 179

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T211301Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma22_cross_down` | one_head_filter_pi_star | 13 | 1.2029 | 3.5064 | 0.7692 | 1.8460 | 0.0212 | 0.2308 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma22_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma22_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma22_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1841 | 0.6909 | 4.0513 | 0.0180 | 0.4182 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma22_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1836 | 0.6909 | 4.0495 | 0.0180 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma22_cross_up` | one_head_filter_pi_star | 16 | 1.3166 | 1.4404 | 0.6875 | 0.6405 | 0.0154 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma22_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| ETHUSDT | 8 | `sma22_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2057 | 0.5886 | 0.9484 | 0.0067 | 0.2089 | ok | RAN |
| SOLUSDT | 8 | `sma22_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3815 | 0.5915 | 2.0590 | 0.0056 | 0.2488 | ok | RAN |
| SOLUSDT | 4 | `sma22_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3673 | 0.5953 | 1.9903 | 0.0054 | 0.2465 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma22_cross_down` | one_head_filter_pi_star | 12 | 1.3245 | 0.8212 | 0.5000 | -0.3058 | -0.0061 | 0.0833 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma22_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma22_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `sma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `sma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
