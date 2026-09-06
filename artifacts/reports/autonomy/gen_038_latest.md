# Autonomy public-indicator hunt gen 038

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T120132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `kst_cross_up_0` | one_head_filter_pi_star | 32 | 3.0366 | 3.1652 | 0.7500 | 2.7354 | 0.0234 | 0.2188 | TPM<MIN | RAN |
| ETHUSDT | 8 | `kst_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8480 | 0.6771 | 4.0973 | 0.0218 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `kst_neg_at_h` | one_head_filter_pi_star | 206 | 16.8283 | 1.8716 | 0.6748 | 3.9625 | 0.0217 | 0.3592 | EBR>35% | RAN |
| ETHUSDT | 8 | `kst_cross_down_0` | one_head_filter_pi_star | 67 | 5.5368 | 1.5721 | 0.6269 | 1.4655 | 0.0196 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 8 | `kst_cross_down_0` | one_head_filter_pi_star | 34 | 2.7942 | 1.9123 | 0.6471 | 1.5251 | 0.0183 | 0.4412 | EBR>35% | RAN |
| SOLUSDT | 8 | `kst_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2037 | 0.6890 | 4.1148 | 0.0183 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `kst_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9627 | 0.6743 | 3.7428 | 0.0159 | 0.3771 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `kst_cross_up_0` | one_head_filter_pi_star | 37 | 3.4414 | 1.4104 | 0.5676 | 0.9426 | 0.0123 | 0.1892 | TPM<MIN | RAN |
| ETHUSDT | 4 | `kst_cross_down_0` | one_head_filter_pi_star | 39 | 3.5276 | 1.2796 | 0.5897 | 0.6239 | 0.0110 | 0.3077 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `kst_cross_up_0` | one_head_filter_pi_star | 47 | 4.3947 | 1.6071 | 0.6170 | 1.4590 | 0.0093 | 0.1702 | ok | RAN |
| SOLUSDT | 4 | `kst_cross_down_0` | one_head_filter_pi_star | 26 | 2.1571 | 1.2850 | 0.6154 | 0.5545 | 0.0081 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `kst_pos_at_h` | one_head_filter_pi_star | 209 | 17.0419 | 1.5496 | 0.6172 | 2.6645 | 0.0076 | 0.2679 | ok | RAN |
| ETHUSDT | 4 | `kst_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2167 | 0.6066 | 1.1097 | 0.0071 | 0.2295 | ok | RAN |
| ETHUSDT | 8 | `kst_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1672 | 0.5963 | 0.8121 | 0.0053 | 0.2050 | ok | RAN |
| SOLUSDT | 8 | `kst_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3204 | 0.5896 | 1.7535 | 0.0048 | 0.2406 | ok | RAN |
| ETHUSDT | 4 | `kst_cross_up_0` | one_head_filter_pi_star | 24 | 2.2653 | 1.0525 | 0.5417 | 0.1107 | 0.0020 | 0.2083 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `kst_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `kst_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `kst_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `kst_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `kst_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kst_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `kst_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kst_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
