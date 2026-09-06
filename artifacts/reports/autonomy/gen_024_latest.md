# Autonomy public-indicator hunt gen 024

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T101503Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `eom_cross_up_0` | one_head_filter_pi_star | 37 | 3.0446 | 2.0849 | 0.5946 | 1.8220 | 0.0334 | 0.2703 | TPM<MIN | RAN |
| ETHUSDT | 4 | `eom_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8033 | 0.6787 | 3.8706 | 0.0207 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `eom_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7962 | 0.6757 | 3.8460 | 0.0206 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 4 | `eom_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2276 | 0.6951 | 4.1590 | 0.0182 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `eom_cross_down_0` | one_head_filter_pi_star | 36 | 3.0803 | 1.5016 | 0.6667 | 1.0843 | 0.0176 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 8 | `eom_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1912 | 0.6909 | 4.0367 | 0.0175 | 0.4182 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `eom_cross_down_0` | one_head_filter_pi_star | 23 | 1.8921 | 1.7085 | 0.6087 | 1.0552 | 0.0143 | 0.3043 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `eom_cross_down_0` | one_head_filter_pi_star | 35 | 2.8793 | 1.6336 | 0.6571 | 1.0296 | 0.0084 | 0.2286 | TPM<MIN | RAN |
| ETHUSDT | 8 | `eom_cross_down_0` | one_head_filter_pi_star | 47 | 3.8947 | 1.2140 | 0.5957 | 0.5652 | 0.0081 | 0.2128 | TPM<MIN | RAN |
| ETHUSDT | 8 | `eom_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2413 | 0.5938 | 1.0983 | 0.0076 | 0.2000 | ok | RAN |
| SOLUSDT | 4 | `eom_cross_up_0` | one_head_filter_pi_star | 22 | 1.8618 | 1.3535 | 0.5455 | 0.5986 | 0.0072 | 0.1818 | TPM<MIN | RAN |
| SOLUSDT | 4 | `eom_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.4955 | 0.6132 | 2.5190 | 0.0070 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `eom_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2017 | 0.5963 | 0.9312 | 0.0065 | 0.1988 | ok | RAN |
| SOLUSDT | 8 | `eom_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3896 | 0.5991 | 2.1379 | 0.0058 | 0.2442 | ok | RAN |
| ETHUSDT | 4 | `eom_cross_up_0` | one_head_filter_pi_star | 25 | 2.0648 | 1.0847 | 0.4800 | 0.1631 | 0.0037 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `eom_cross_up_0` | one_head_filter_pi_star | 24 | 2.0311 | 1.1546 | 0.5417 | 0.3018 | 0.0035 | 0.2500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `eom_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `eom_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `eom_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `eom_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `eom_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `eom_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `eom_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `eom_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
