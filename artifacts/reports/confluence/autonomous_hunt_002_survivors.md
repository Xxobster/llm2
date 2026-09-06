# Hunt 002 diagnostic flags

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. **Promoted: none.**
Test window only (last 30% before lockbox). n>=50, entry-bar exit <=35%, intent expectancy beats same-bracket control, Profit Factor >= 85% of control.
Beating a losing control (Profit Factor < 1) is a weak flag, not a promote.

Arms in grid: 1092. Flags: 67.

| Symbol | TF | H | Event | Mode | TP | SL | n | /mo | PF | PFctrl | WR | Sharpe | exp_i | exp_ctrl | ebr |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT | 1h | 4 | `structure_break_hold` | one_head_standalone_pi_star | 0.02 | 0.01 | 70 | 4.3 | 1.274 | 0.865 | 0.471 | 0.77 | 0.0530 | -0.0110 | 0.171 |
| BTCUSDT | 15m | 4 | `structure_break_hold` | one_head_standalone_pi_star | 0.01 | 0.015 | 55 | 4.6 | 1.667 | 1.187 | 0.564 | 1.57 | 0.0718 | 0.0150 | 0.073 |
| ETHUSDT | 15m | 8 | `structure_break_hold` | one_head_filter_pi_star | 0.02 | 0.01 | 74 | 6.1 | 1.702 | 0.986 | 0.622 | 1.66 | 0.0226 | -0.0005 | 0.095 |
| BTCUSDT | 1h | 4 | `macd_hist_flip_down` | one_head_standalone_pi_star | 0.01 | 0.01 | 182 | 11.4 | 1.533 | 1.159 | 0.632 | 2.12 | 0.0339 | 0.0109 | 0.319 |
| SOLUSDT | 15m | 8 | `pulse_extend` | one_head_filter_pi_star | 0.02 | 0.01 | 54 | 5.0 | 1.839 | 0.982 | 0.574 | 1.87 | 0.0218 | -0.0004 | 0.056 |
| SOLUSDT | 15m | 4 | `pulse_extend` | one_head_filter_pi_star | 0.02 | 0.01 | 53 | 5.1 | 1.803 | 0.982 | 0.566 | 1.81 | 0.0208 | -0.0004 | 0.057 |
| SOLUSDT | 15m | 16 | `pulse_extend` | one_head_filter_pi_star | 0.02 | 0.01 | 53 | 5.1 | 1.779 | 0.982 | 0.566 | 1.78 | 0.0202 | -0.0004 | 0.038 |
| ETHUSDT | 15m | 4 | `range_break_up` | one_head_filter_pi_star | 0.02 | 0.01 | 52 | 4.6 | 1.358 | 0.986 | 0.558 | 0.81 | 0.0178 | -0.0005 | 0.038 |
| ETHUSDT | 15m | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.015 | 0.01 | 82 | 6.8 | 1.738 | 1.053 | 0.622 | 2.08 | 0.0199 | 0.0018 | 0.159 |
| BTCUSDT | 1h | 4 | `adx_fade` | one_head_standalone_pi_star | 0.02 | 0.01 | 394 | 23.9 | 1.111 | 0.865 | 0.487 | 0.74 | 0.0060 | -0.0110 | 0.140 |
| BTCUSDT | 1h | 4 | `macd_hist_flip_up` | one_head_standalone_pi_star | 0.02 | 0.01 | 323 | 19.7 | 1.070 | 0.865 | 0.495 | 0.44 | 0.0047 | -0.0110 | 0.099 |
| BTCUSDT | 1h | 4 | `failed_swing_ll` | one_head_standalone_pi_star | 0.02 | 0.01 | 391 | 23.8 | 1.060 | 0.865 | 0.486 | 0.43 | 0.0040 | -0.0110 | 0.110 |
| BTCUSDT | 1h | 4 | `macd_hist_flip_up` | one_head_standalone_pi_star | 0.01 | 0.01 | 280 | 17.0 | 1.446 | 1.159 | 0.604 | 2.44 | 0.0260 | 0.0109 | 0.279 |
| BTCUSDT | 1h | 4 | `stoch_cross_up_20` | one_head_standalone_pi_star | 0.02 | 0.01 | 429 | 26.1 | 1.048 | 0.865 | 0.478 | 0.36 | 0.0032 | -0.0110 | 0.140 |
| BTCUSDT | 1h | 4 | `adx_fade` | one_head_standalone_pi_star | 0.01 | 0.01 | 319 | 19.4 | 1.459 | 1.159 | 0.621 | 2.43 | 0.0240 | 0.0109 | 0.313 |
| ETHUSDT | 15m | 16 | `structure_break_hold` | one_head_standalone_pi_star | 0.02 | 0.01 | 59 | 4.8 | 1.223 | 0.986 | 0.508 | 0.57 | 0.0109 | -0.0005 | 0.068 |
| BTCUSDT | 15m | 4 | `structure_break_hold` | one_head_standalone_pi_star | 0.01 | 0.01 | 121 | 10.0 | 1.090 | 1.015 | 0.537 | 0.40 | 0.0111 | 0.0014 | 0.066 |
| BTCUSDT | 1h | 4 | `range_hold` | one_head_standalone_pi_star | 0.02 | 0.01 | 783 | 47.6 | 0.964 | 0.865 | 0.457 | -0.37 | -0.0020 | -0.0110 | 0.112 |
| SOLUSDT | 15m | 16 | `failed_swing_ll` | one_head_filter_pi_star | 0.01 | 0.01 | 72 | 5.9 | 2.188 | 1.666 | 0.667 | 2.68 | 0.0183 | 0.0100 | 0.347 |
| ETHUSDT | 15m | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.02 | 0.01 | 97 | 7.9 | 1.220 | 0.986 | 0.526 | 0.83 | 0.0076 | -0.0005 | 0.113 |
| SOLUSDT | 15m | 8 | `failed_swing_ll` | one_head_filter_pi_star | 0.01 | 0.01 | 50 | 4.1 | 2.062 | 1.666 | 0.640 | 2.21 | 0.0181 | 0.0100 | 0.320 |
| BTCUSDT | 1h | 4 | `range_hold` | one_head_standalone_pi_star | 0.01 | 0.01 | 571 | 34.7 | 1.349 | 1.159 | 0.594 | 2.65 | 0.0185 | 0.0109 | 0.291 |
| ETHUSDT | 15m | 8 | `range_break_up` | one_head_filter_pi_star | 0.02 | 0.01 | 102 | 8.4 | 1.174 | 0.986 | 0.520 | 0.61 | 0.0067 | -0.0005 | 0.049 |
| BTCUSDT | 1h | 4 | `failed_swing_hh` | one_head_standalone_pi_star | 0.02 | 0.01 | 357 | 21.8 | 0.917 | 0.865 | 0.440 | -0.56 | -0.0043 | -0.0110 | 0.076 |
| BTCUSDT | 1h | 4 | `macd_hist_flip_down` | one_head_standalone_pi_star | 0.02 | 0.01 | 250 | 15.3 | 0.938 | 0.865 | 0.448 | -0.37 | -0.0044 | -0.0110 | 0.072 |
| ETHUSDT | 15m | 16 | `range_break_up` | one_head_filter_pi_star | 0.02 | 0.01 | 139 | 11.5 | 1.131 | 0.986 | 0.525 | 0.54 | 0.0049 | -0.0005 | 0.072 |
| ETHUSDT | 15m | 4 | `structure_break_hold` | one_head_filter_pi_star | 0.02 | 0.01 | 115 | 9.4 | 1.133 | 0.986 | 0.565 | 0.50 | 0.0049 | -0.0005 | 0.078 |
| ETHUSDT | 15m | 4 | `failed_swing_hh` | one_head_filter_pi_star | 0.02 | 0.01 | 54 | 4.5 | 1.135 | 0.986 | 0.519 | 0.35 | 0.0045 | -0.0005 | 0.056 |
| SOLUSDT | 15m | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 0.015 | 0.01 | 149 | 12.2 | 1.343 | 1.139 | 0.544 | 1.41 | 0.0076 | 0.0027 | 0.188 |
| ETHUSDT | 15m | 16 | `macd_hist_flip_down` | one_head_filter_pi_star | 0.02 | 0.01 | 189 | 15.5 | 1.110 | 0.986 | 0.519 | 0.55 | 0.0040 | -0.0005 | 0.069 |
| SOLUSDT | 15m | 4 | `range_break_down` | one_head_filter_pi_star | 0.015 | 0.01 | 64 | 5.2 | 1.306 | 1.139 | 0.594 | 0.88 | 0.0072 | 0.0027 | 0.109 |
| SOLUSDT | 15m | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.015 | 0.01 | 70 | 5.8 | 1.291 | 1.139 | 0.514 | 0.89 | 0.0070 | 0.0027 | 0.143 |
| BTCUSDT | 1h | 4 | `stoch_cross_down_80` | one_head_standalone_pi_star | 0.02 | 0.01 | 382 | 23.2 | 0.876 | 0.865 | 0.427 | -0.89 | -0.0069 | -0.0110 | 0.113 |
| SOLUSDT | 15m | 16 | `failed_swing_ll` | one_head_filter_pi_star | 0.02 | 0.01 | 117 | 9.6 | 1.164 | 0.982 | 0.538 | 0.63 | 0.0036 | -0.0004 | 0.060 |
| SOLUSDT | 15m | 16 | `vsa_dryup_expand` | one_head_filter_pi_star | 0.02 | 0.01 | 117 | 9.6 | 1.183 | 0.982 | 0.530 | 0.72 | 0.0034 | -0.0004 | 0.043 |
| SOLUSDT | 15m | 8 | `failed_swing_ll` | one_head_filter_pi_star | 0.02 | 0.01 | 75 | 6.1 | 1.122 | 0.982 | 0.507 | 0.37 | 0.0030 | -0.0004 | 0.053 |
| ETHUSDT | 15m | 8 | `macd_hist_flip_up` | one_head_filter_pi_star | 0.02 | 0.01 | 72 | 5.9 | 1.082 | 0.986 | 0.556 | 0.29 | 0.0028 | -0.0005 | 0.139 |
| ETHUSDT | 15m | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 0.01 | 0.015 | 205 | 16.7 | 1.673 | 1.557 | 0.693 | 3.06 | 0.0182 | 0.0155 | 0.346 |
| ETHUSDT | 15m | 4 | `stoch_cross_down_80` | one_head_filter_pi_star | 0.02 | 0.01 | 154 | 12.7 | 1.056 | 0.986 | 0.519 | 0.25 | 0.0021 | -0.0005 | 0.058 |
| SOLUSDT | 15m | 4 | `range_break_down` | one_head_filter_pi_star | 0.02 | 0.01 | 109 | 8.9 | 1.083 | 0.982 | 0.514 | 0.32 | 0.0020 | -0.0004 | 0.083 |
| ETHUSDT | 15m | 16 | `rsi_cross_down_70` | one_head_filter_pi_star | 0.02 | 0.01 | 107 | 8.8 | 1.046 | 0.986 | 0.533 | 0.19 | 0.0017 | -0.0005 | 0.065 |
| ETHUSDT | 15m | 4 | `structure_break_hold` | one_head_filter_pi_star | 0.015 | 0.01 | 103 | 8.4 | 1.105 | 1.053 | 0.583 | 0.40 | 0.0040 | 0.0018 | 0.087 |
| ETHUSDT | 15m | 8 | `stoch_cross_down_80` | one_head_filter_pi_star | 0.02 | 0.01 | 158 | 13.0 | 1.045 | 0.986 | 0.519 | 0.21 | 0.0016 | -0.0005 | 0.063 |
| ETHUSDT | 15m | 8 | `failed_swing_hh` | one_head_filter_pi_star | 0.02 | 0.01 | 100 | 8.3 | 1.040 | 0.986 | 0.520 | 0.15 | 0.0015 | -0.0005 | 0.060 |
| SOLUSDT | 15m | 4 | `stoch_cross_up_20` | one_head_filter_pi_star | 0.02 | 0.01 | 152 | 12.4 | 1.060 | 0.982 | 0.493 | 0.28 | 0.0015 | -0.0004 | 0.099 |
| BTCUSDT | 1h | 4 | `pulse_extend` | one_head_standalone_pi_star | 0.01 | 0.01 | 69 | 4.4 | 1.029 | 1.159 | 0.536 | 0.10 | 0.0127 | 0.0109 | 0.319 |
| ETHUSDT | 1h | 4 | `structure_break_hold` | one_head_standalone_pi_star | 0.02 | 0.01 | 94 | 5.9 | 1.903 | 1.704 | 0.511 | 2.40 | 0.0427 | 0.0411 | 0.287 |
| SOLUSDT | 15m | 8 | `rsi_cross_down_70` | one_head_filter_pi_star | 0.02 | 0.01 | 112 | 9.1 | 1.053 | 0.982 | 0.536 | 0.22 | 0.0011 | -0.0004 | 0.080 |
| SOLUSDT | 15m | 8 | `macd_hist_flip_up` | one_head_filter_pi_star | 0.02 | 0.01 | 99 | 8.1 | 1.044 | 0.982 | 0.525 | 0.16 | 0.0010 | -0.0004 | 0.111 |
| SOLUSDT | 15m | 8 | `stoch_cross_up_20` | one_head_filter_pi_star | 0.02 | 0.01 | 157 | 12.8 | 1.040 | 0.982 | 0.497 | 0.19 | 0.0010 | -0.0004 | 0.102 |
| SOLUSDT | 15m | 4 | `rsi_cross_down_70` | one_head_standalone_pi_star | 0.02 | 0.01 | 297 | 24.2 | 1.076 | 0.982 | 0.519 | 0.49 | 0.0008 | -0.0004 | 0.057 |
| ETHUSDT | 15m | 8 | `range_break_down` | one_head_filter_pi_star | 0.02 | 0.01 | 164 | 13.4 | 1.016 | 0.986 | 0.543 | 0.08 | 0.0006 | -0.0005 | 0.079 |
| ETHUSDT | 15m | 8 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.02 | 0.01 | 123 | 10.0 | 1.015 | 0.986 | 0.520 | 0.07 | 0.0005 | -0.0005 | 0.106 |
| SOLUSDT | 15m | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.02 | 0.01 | 74 | 6.2 | 1.024 | 0.982 | 0.459 | 0.09 | 0.0006 | -0.0004 | 0.095 |
| SOLUSDT | 15m | 16 | `macd_hist_flip_up` | one_head_filter_pi_star | 0.02 | 0.01 | 198 | 16.2 | 1.022 | 0.982 | 0.505 | 0.12 | 0.0005 | -0.0004 | 0.086 |
| SOLUSDT | 15m | 4 | `structure_break_hold` | one_head_filter_pi_star | 0.015 | 0.01 | 64 | 6.0 | 1.130 | 1.139 | 0.469 | 0.47 | 0.0036 | 0.0027 | 0.250 |
| ETHUSDT | 15m | 8 | `macd_hist_flip_down` | one_head_filter_pi_star | 0.02 | 0.01 | 83 | 6.9 | 1.007 | 0.986 | 0.494 | 0.03 | 0.0003 | -0.0005 | 0.072 |
| SOLUSDT | 15m | 8 | `rsi_cross_down_70` | one_head_standalone_pi_star | 0.02 | 0.01 | 343 | 27.9 | 1.025 | 0.982 | 0.490 | 0.17 | 0.0003 | -0.0004 | 0.076 |
| SOLUSDT | 15m | 4 | `rsi_cross_up_30` | one_head_standalone_pi_star | 0.02 | 0.01 | 259 | 21.2 | 1.014 | 0.982 | 0.475 | 0.11 | 0.0002 | -0.0004 | 0.112 |
| SOLUSDT | 15m | 8 | `vsa_dryup_expand` | one_head_standalone_pi_star | 0.02 | 0.01 | 325 | 26.4 | 1.018 | 0.982 | 0.511 | 0.11 | 0.0001 | -0.0004 | 0.006 |
| SOLUSDT | 15m | 8 | `rsi_cross_up_30` | one_head_standalone_pi_star | 0.02 | 0.01 | 405 | 32.9 | 0.999 | 0.982 | 0.501 | -0.01 | -0.0000 | -0.0004 | 0.114 |
| SOLUSDT | 15m | 16 | `range_break_down` | one_head_filter_pi_star | 0.02 | 0.01 | 141 | 11.5 | 0.993 | 0.982 | 0.482 | -0.03 | -0.0002 | -0.0004 | 0.085 |
| SOLUSDT | 15m | 16 | `stoch_cross_down_80` | one_head_standalone_pi_star | 0.02 | 0.01 | 3582 | 290.5 | 0.961 | 0.982 | 0.480 | -0.87 | -0.0002 | -0.0004 | 0.025 |
| SOLUSDT | 15m | 16 | `rsi_cross_up_30` | one_head_filter_pi_star | 0.02 | 0.01 | 121 | 9.9 | 0.992 | 0.982 | 0.488 | -0.04 | -0.0002 | -0.0004 | 0.116 |
| SOLUSDT | 15m | 16 | `adx_fade` | one_head_standalone_pi_star | 0.02 | 0.01 | 1873 | 151.9 | 0.955 | 0.982 | 0.497 | -0.83 | -0.0003 | -0.0004 | 0.051 |
| SOLUSDT | 15m | 16 | `stoch_cross_down_80` | one_head_filter_pi_star | 0.02 | 0.01 | 329 | 26.8 | 0.984 | 0.982 | 0.498 | -0.11 | -0.0003 | -0.0004 | 0.079 |
| ETHUSDT | 15m | 16 | `stoch_cross_down_80` | one_head_standalone_pi_star | 0.02 | 0.01 | 3458 | 280.5 | 0.948 | 0.986 | 0.470 | -1.07 | -0.0004 | -0.0005 | 0.030 |
