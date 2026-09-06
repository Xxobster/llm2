# Autonomy public-indicator hunt gen 042

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T121607Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `adl_neg_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.9144 | 0.6981 | 4.1591 | 0.0229 | 0.3868 | EBR>35% | RAN |
| ETHUSDT | 8 | `adl_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9346 | 0.6989 | 3.8303 | 0.0226 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 8 | `adl_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.6327 | 0.7244 | 4.6801 | 0.0208 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `adl_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.3575 | 0.7083 | 4.4748 | 0.0195 | 0.4107 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `adl_cross_up_0` | one_head_filter_pi_star | 63 | 5.1816 | 1.3323 | 0.6190 | 0.9686 | 0.0110 | 0.3016 | ok | RAN |
| SOLUSDT | 4 | `adl_cross_down_0` | one_head_filter_pi_star | 13 | 1.1441 | 2.2161 | 0.6154 | 1.2349 | 0.0102 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `adl_pos_at_h` | one_head_filter_pi_star | 175 | 14.3376 | 1.2323 | 0.5943 | 1.1248 | 0.0081 | 0.2171 | ok | RAN |
| SOLUSDT | 8 | `adl_cross_down_0` | one_head_filter_pi_star | 40 | 3.3881 | 1.5445 | 0.6250 | 1.1781 | 0.0073 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adl_pos_at_h` | one_head_filter_pi_star | 169 | 13.8460 | 1.1870 | 0.5799 | 0.8832 | 0.0062 | 0.1893 | ok | RAN |
| SOLUSDT | 8 | `adl_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3555 | 0.5896 | 1.9302 | 0.0059 | 0.2406 | ok | RAN |
| SOLUSDT | 4 | `adl_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3527 | 0.5943 | 1.9230 | 0.0053 | 0.2358 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `adl_cross_up_0` | one_head_filter_pi_star | 36 | 2.9670 | 0.9613 | 0.5833 | -0.1065 | -0.0009 | 0.3056 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adl_cross_down_0` | one_head_filter_pi_star | 46 | 3.8182 | 0.8689 | 0.4565 | -0.3748 | -0.0039 | 0.0870 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adl_cross_up_0` | one_head_filter_pi_star | 16 | 1.3644 | 0.8300 | 0.5000 | -0.3575 | -0.0074 | 0.3125 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adl_cross_down_0` | one_head_filter_pi_star | 19 | 2.1441 | 0.3663 | 0.4211 | -1.8158 | -0.0240 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `adl_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7040 | 0.3500 | -0.6085 | -0.0291 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `adl_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6980 | 0.3158 | -0.6210 | -0.0303 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 4 | `adl_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `adl_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `adl_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `adl_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adl_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `adl_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adl_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
