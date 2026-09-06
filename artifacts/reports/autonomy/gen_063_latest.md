# Autonomy public-indicator hunt gen 063

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T134111Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `cob_cross_up_0` | one_head_filter_pi_star | 27 | 2.2217 | 1.4000 | 0.6296 | 0.7656 | 0.0237 | 0.2963 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cob_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8020 | 0.6816 | 3.8746 | 0.0205 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `cob_cross_up_0` | one_head_filter_pi_star | 37 | 3.0446 | 1.5139 | 0.6486 | 1.0936 | 0.0205 | 0.2973 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cob_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7846 | 0.6787 | 3.7601 | 0.0203 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `cob_cross_up_0` | one_head_filter_pi_star | 30 | 2.5567 | 1.8378 | 0.6000 | 1.3975 | 0.0189 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `cob_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1645 | 0.6890 | 4.0077 | 0.0177 | 0.4146 | EBR>35% | RAN |
| SOLUSDT | 4 | `cob_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1323 | 0.6871 | 3.9123 | 0.0172 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `cob_cross_down_0` | one_head_filter_pi_star | 18 | 1.4866 | 1.6397 | 0.5556 | 0.8748 | 0.0146 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `cob_cross_down_0` | one_head_filter_pi_star | 37 | 3.0559 | 1.2333 | 0.5676 | 0.5415 | 0.0099 | 0.1622 | TPM<MIN | RAN |
| SOLUSDT | 8 | `cob_cross_down_0` | one_head_filter_pi_star | 29 | 2.3857 | 1.6331 | 0.5862 | 1.0668 | 0.0095 | 0.1379 | TPM<MIN | RAN |
| ETHUSDT | 8 | `cob_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2567 | 0.5938 | 1.2074 | 0.0080 | 0.1875 | ok | RAN |
| SOLUSDT | 4 | `cob_cross_down_0` | one_head_filter_pi_star | 19 | 1.6244 | 1.4222 | 0.5263 | 0.6778 | 0.0077 | 0.2105 | TPM<MIN | RAN |
| ETHUSDT | 4 | `cob_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2172 | 0.5926 | 0.9965 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `cob_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4085 | 0.6066 | 2.1557 | 0.0060 | 0.2417 | ok | RAN |
| SOLUSDT | 8 | `cob_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3754 | 0.5896 | 2.0360 | 0.0056 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `cob_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `cob_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| SOLUSDT | 4 | `cob_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cob_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `cob_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `cob_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cob_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `cob_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `cob_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
