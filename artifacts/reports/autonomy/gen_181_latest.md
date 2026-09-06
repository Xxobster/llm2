# Autonomy public-indicator hunt gen 181

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T212037Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret14_cross_up_0` | one_head_filter_pi_star | 23 | 1.9612 | 1.5927 | 0.6957 | 0.9750 | 0.0309 | 0.3043 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret14_cross_up_0` | one_head_filter_pi_star | 38 | 3.1269 | 1.8165 | 0.6842 | 1.5904 | 0.0307 | 0.3158 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret14_cross_up_0` | one_head_filter_pi_star | 22 | 1.8749 | 3.1696 | 0.6818 | 2.0866 | 0.0292 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret14_cross_up_0` | one_head_filter_pi_star | 14 | 1.2171 | 1.9342 | 0.6429 | 1.0288 | 0.0235 | 0.2143 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret14_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7624 | 0.6758 | 3.6855 | 0.0199 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret14_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.7295 | 0.6728 | 3.5175 | 0.0190 | 0.3687 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret14_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1348 | 0.6871 | 3.9222 | 0.0173 | 0.4110 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret14_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0759 | 0.6826 | 3.8227 | 0.0168 | 0.4192 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret14_cross_down_0` | one_head_filter_pi_star | 21 | 1.7344 | 1.6894 | 0.5714 | 0.9943 | 0.0151 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret14_cross_down_0` | one_head_filter_pi_star | 34 | 2.7970 | 1.9684 | 0.6471 | 1.5514 | 0.0128 | 0.1471 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret14_cross_down_0` | one_head_filter_pi_star | 18 | 1.4808 | 1.4487 | 0.5556 | 0.6563 | 0.0091 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret14_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.2108 | 0.5949 | 0.9626 | 0.0067 | 0.2025 | ok | RAN |
| ETHUSDT | 8 | `ret14_pos_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1944 | 0.5849 | 0.9198 | 0.0062 | 0.1950 | ok | RAN |
| SOLUSDT | 4 | `ret14_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.4231 | 0.6039 | 2.2029 | 0.0062 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `ret14_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3963 | 0.5953 | 2.1219 | 0.0059 | 0.2512 | ok | RAN |
| ETHUSDT | 8 | `ret14_cross_down_0` | one_head_filter_pi_star | 30 | 2.4777 | 1.0818 | 0.5667 | 0.1815 | 0.0036 | 0.1667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret14_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0226 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret14_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret14_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret14_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret14_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret14_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret14_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret14_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
