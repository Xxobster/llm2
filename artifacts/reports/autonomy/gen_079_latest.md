# Autonomy public-indicator hunt gen 079

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T144333Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `kijun_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8380 | 0.6818 | 3.9857 | 0.0212 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 8 | `kijun_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8151 | 0.6773 | 3.9115 | 0.0207 | 0.3727 | EBR>35% | RAN |
| ETHUSDT | 8 | `kijun_cross_down` | one_head_filter_pi_star | 22 | 2.0315 | 1.7631 | 0.6818 | 1.1321 | 0.0206 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 8 | `kijun_cross_down` | one_head_filter_pi_star | 27 | 2.3744 | 2.6635 | 0.7407 | 2.0417 | 0.0184 | 0.2222 | TPM<MIN | RAN |
| SOLUSDT | 8 | `kijun_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1787 | 0.6890 | 4.0325 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `kijun_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1749 | 0.6905 | 4.0629 | 0.0178 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `kijun_cross_up` | one_head_filter_pi_star | 27 | 2.3504 | 1.3973 | 0.5926 | 0.7865 | 0.0159 | 0.2593 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `kijun_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2207 | 0.5901 | 1.0119 | 0.0072 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `kijun_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.1886 | 0.5915 | 0.8865 | 0.0062 | 0.2012 | ok | RAN |
| SOLUSDT | 4 | `kijun_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3560 | 0.5935 | 1.9346 | 0.0053 | 0.2430 | ok | RAN |
| SOLUSDT | 8 | `kijun_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3449 | 0.5915 | 1.8864 | 0.0052 | 0.2441 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `kijun_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `kijun_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `kijun_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `kijun_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `kijun_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `kijun_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `kijun_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `kijun_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `kijun_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `kijun_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kijun_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `kijun_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kijun_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
