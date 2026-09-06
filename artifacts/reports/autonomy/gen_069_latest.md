# Autonomy public-indicator hunt gen 069

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T140507Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `dc_low_closer` | one_head_filter_pi_star | 213 | 17.4002 | 1.8278 | 0.6854 | 3.8659 | 0.0211 | 0.3803 | EBR>35% | RAN |
| ETHUSDT | 4 | `dc_low_closer` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0205 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 4 | `dc_low_closer` | one_head_filter_pi_star | 163 | 13.3287 | 2.2428 | 0.6933 | 4.1554 | 0.0184 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 8 | `dc_low_closer` | one_head_filter_pi_star | 147 | 12.0203 | 2.0750 | 0.6735 | 3.6562 | 0.0169 | 0.4218 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `dc_high_closer` | one_head_filter_pi_star | 150 | 12.3782 | 1.3324 | 0.6000 | 1.3989 | 0.0110 | 0.1933 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `dc_high_closer` | one_head_filter_pi_star | 161 | 13.2859 | 1.2226 | 0.5901 | 1.0068 | 0.0070 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `dc_high_closer` | one_head_filter_pi_star | 217 | 17.6943 | 1.4003 | 0.6037 | 2.1802 | 0.0060 | 0.2442 | ok | RAN |
| SOLUSDT | 4 | `dc_high_closer` | one_head_filter_pi_star | 217 | 17.6943 | 1.3891 | 0.5991 | 2.1002 | 0.0057 | 0.2442 | ok | RAN |
| ETHUSDT | 4 | `dc_near_low_at_h` | one_head_filter_pi_star | 181 | 14.8842 | 1.1011 | 0.5801 | 0.5593 | 0.0030 | 0.1823 | ok | RAN |
| SOLUSDT | 4 | `dc_near_high_at_h` | one_head_filter_pi_star | 161 | 13.4439 | 1.2115 | 0.5714 | 1.0822 | 0.0030 | 0.1304 | ok | RAN |
| SOLUSDT | 8 | `dc_near_high_at_h` | one_head_filter_pi_star | 165 | 13.7779 | 1.1658 | 0.5636 | 0.8272 | 0.0023 | 0.1212 | ok | RAN |
| SOLUSDT | 8 | `dc_near_low_at_h` | one_head_filter_pi_star | 113 | 9.2533 | 1.1319 | 0.5664 | 0.5287 | 0.0018 | 0.0885 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `dc_near_low_at_h` | one_head_filter_pi_star | 96 | 7.8489 | 1.0572 | 0.5729 | 0.2136 | 0.0008 | 0.1146 | ok | RAN |
| ETHUSDT | 8 | `dc_near_low_at_h` | one_head_filter_pi_star | 162 | 13.3282 | 1.0019 | 0.5617 | 0.0103 | 0.0001 | 0.1296 | ok | RAN |
| ETHUSDT | 8 | `dc_near_high_at_h` | one_head_filter_pi_star | 152 | 12.4532 | 0.7804 | 0.5197 | -1.2454 | -0.0073 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `dc_near_high_at_h` | one_head_filter_pi_star | 140 | 11.4701 | 0.6952 | 0.4786 | -1.7138 | -0.0105 | 0.1143 | ok | RAN |
| BTCUSDT | 8 | `dc_high_closer` | one_head_filter_pi_star | 18 | 1.5318 | 0.6971 | 0.3889 | -0.5701 | -0.0306 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `dc_high_closer` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `dc_near_high_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4838 | 0.2632 | -1.1440 | -0.0498 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `dc_near_high_at_h` | one_head_filter_pi_star | 16 | 1.4683 | 0.3831 | 0.2500 | -1.3889 | -0.0534 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `dc_near_low_at_h` | one_head_filter_pi_star | 12 | 1.6328 | 0.2330 | 0.2500 | -2.2470 | -0.0588 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `dc_near_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `dc_low_closer` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `dc_low_closer` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
