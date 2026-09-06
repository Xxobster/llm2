# Autonomy public-indicator hunt gen 156

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T194156Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema45_cross_up` | one_head_filter_pi_star | 16 | 1.3561 | 13.5790 | 0.8125 | 2.9141 | 0.0501 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema45_cross_down` | one_head_filter_pi_star | 14 | 1.1949 | 3.3052 | 0.7857 | 1.7268 | 0.0341 | 0.0714 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema45_cross_down` | one_head_filter_pi_star | 24 | 2.0484 | 5.0428 | 0.7917 | 2.6524 | 0.0305 | 0.0833 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema45_below_at_h` | one_head_filter_pi_star | 212 | 17.3185 | 1.8021 | 0.6840 | 3.8865 | 0.0207 | 0.3774 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema45_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7961 | 0.6822 | 3.8424 | 0.0206 | 0.3738 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema45_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1128 | 0.6855 | 3.8514 | 0.0171 | 0.4214 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema45_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.0841 | 0.6770 | 3.8085 | 0.0166 | 0.4099 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema45_cross_down` | one_head_filter_pi_star | 17 | 1.9955 | 1.3584 | 0.5294 | 0.6870 | 0.0132 | 0.2941 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema45_above_at_h` | one_head_filter_pi_star | 164 | 13.5335 | 1.2660 | 0.6037 | 1.2095 | 0.0082 | 0.2073 | ok | RAN |
| ETHUSDT | 8 | `ema45_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2543 | 0.6025 | 1.1562 | 0.0079 | 0.2112 | ok | RAN |
| SOLUSDT | 8 | `ema45_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3858 | 0.6037 | 2.0676 | 0.0056 | 0.2442 | ok | RAN |
| SOLUSDT | 4 | `ema45_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3473 | 0.5962 | 1.8755 | 0.0051 | 0.2488 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema45_cross_up` | one_head_filter_pi_star | 16 | 1.3926 | 1.0243 | 0.5625 | 0.0415 | 0.0009 | 0.3125 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
