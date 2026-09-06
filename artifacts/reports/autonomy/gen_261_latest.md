# Autonomy public-indicator hunt gen 261

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T024409Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret19_cross_down_0` | one_head_filter_pi_star | 13 | 1.2093 | 2.0621 | 0.6923 | 1.0724 | 0.0268 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret19_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8404 | 0.6773 | 4.1082 | 0.0213 | 0.3727 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret19_neg_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8161 | 0.6786 | 3.9334 | 0.0210 | 0.3705 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret19_cross_up_0` | one_head_filter_pi_star | 20 | 1.9109 | 2.2698 | 0.6500 | 1.5656 | 0.0205 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret19_cross_down_0` | one_head_filter_pi_star | 47 | 4.0994 | 2.3585 | 0.6809 | 2.3053 | 0.0204 | 0.2128 | ok | RAN |
| SOLUSDT | 4 | `ret19_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.3038 | 0.7059 | 4.4161 | 0.0192 | 0.4176 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret19_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2125 | 0.6933 | 4.0518 | 0.0179 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret19_cross_up_0` | one_head_filter_pi_star | 24 | 2.0465 | 1.4137 | 0.5417 | 0.7247 | 0.0152 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret19_cross_down_0` | one_head_filter_pi_star | 47 | 3.8947 | 1.2881 | 0.5745 | 0.7264 | 0.0107 | 0.1915 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret19_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2105 | 0.5987 | 0.9589 | 0.0068 | 0.2102 | ok | RAN |
| SOLUSDT | 8 | `ret19_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3798 | 0.6000 | 2.0348 | 0.0056 | 0.2476 | ok | RAN |
| SOLUSDT | 4 | `ret19_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3146 | 0.5849 | 1.7291 | 0.0047 | 0.2453 | ok | RAN |
| ETHUSDT | 4 | `ret19_pos_at_h` | one_head_filter_pi_star | 166 | 13.6986 | 1.0970 | 0.5783 | 0.5021 | 0.0033 | 0.1988 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret19_cross_up_0` | one_head_filter_pi_star | 13 | 1.2155 | 0.5766 | 0.3846 | -0.9246 | -0.0277 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret19_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret19_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret19_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret19_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret19_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret19_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret19_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret19_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret19_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret19_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
