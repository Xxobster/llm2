# Autonomy public-indicator hunt gen 180

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T211700Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema22_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema22_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema22_cross_down` | one_head_filter_pi_star | 24 | 2.0321 | 2.6829 | 0.7083 | 1.9518 | 0.0182 | 0.1667 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema22_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1950 | 0.6909 | 4.0869 | 0.0181 | 0.4242 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema22_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema22_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2338 | 0.5963 | 1.0653 | 0.0074 | 0.2050 | ok | RAN |
| ETHUSDT | 8 | `ema22_cross_up` | one_head_filter_pi_star | 16 | 1.4130 | 1.1723 | 0.6250 | 0.2776 | 0.0068 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema22_above_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1983 | 0.5949 | 0.9099 | 0.0064 | 0.2089 | ok | RAN |
| SOLUSDT | 4 | `ema22_above_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3846 | 0.6009 | 2.0796 | 0.0056 | 0.2431 | ok | RAN |
| SOLUSDT | 8 | `ema22_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3628 | 0.5953 | 1.9682 | 0.0054 | 0.2419 | ok | RAN |
| ETHUSDT | 8 | `ema22_cross_down` | one_head_filter_pi_star | 14 | 1.6878 | 1.0984 | 0.4286 | 0.1699 | 0.0032 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema22_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema22_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ema22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema22_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema22_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema22_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
