# Autonomy public-indicator hunt gen 004

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260821T050027Z`. Arms: 51.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `kc_break_down_at_h` | one_head_filter_pi_star | 17 | 1.5984 | 4.4763 | 0.8235 | 2.5204 | 0.0613 | 0.6471 | EBR>35% | RAN |
| ETHUSDT | 8 | `kc_break_up_at_h` | one_head_filter_pi_star | 20 | 1.7588 | 3.8049 | 0.7000 | 2.4158 | 0.0509 | 0.4500 | EBR>35% | RAN |
| ETHUSDT | 4 | `psar_flip_down` | one_head_filter_pi_star | 13 | 1.1441 | 5.4206 | 0.7692 | 2.3559 | 0.0418 | 0.3077 | TPM<MIN | RAN |
| ETHUSDT | 4 | `kc_break_down_at_h` | one_head_filter_pi_star | 29 | 2.6345 | 2.0787 | 0.7241 | 1.8705 | 0.0279 | 0.5517 | EBR>35% | RAN |
| SOLUSDT | 8 | `psar_flip_up` | one_head_filter_pi_star | 60 | 4.9963 | 2.8020 | 0.7667 | 3.3560 | 0.0207 | 0.3500 | GATE_CAND | RAN |
| ETHUSDT | 8 | `wr_cross_up_neg80` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0204 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `wr_cross_up_neg80` | one_head_filter_pi_star | 212 | 17.3185 | 1.7461 | 0.6792 | 3.5381 | 0.0197 | 0.3821 | EBR>35% | RAN |
| SOLUSDT | 4 | `kc_break_down_at_h` | one_head_filter_pi_star | 45 | 3.9339 | 1.9005 | 0.6889 | 1.9783 | 0.0185 | 0.5556 | EBR>35% | RAN |
| SOLUSDT | 8 | `wr_cross_up_neg80` | one_head_filter_pi_star | 160 | 13.0833 | 2.1227 | 0.6813 | 3.8351 | 0.0174 | 0.4188 | EBR>35% | RAN |
| SOLUSDT | 4 | `wr_cross_up_neg80` | one_head_filter_pi_star | 148 | 12.1021 | 2.0058 | 0.6757 | 3.4209 | 0.0160 | 0.4122 | EBR>35% | RAN |
| ETHUSDT | 4 | `kc_break_up_at_h` | one_head_filter_pi_star | 40 | 3.4082 | 1.3610 | 0.6000 | 0.9386 | 0.0158 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `psar_flip_up` | one_head_filter_pi_star | 80 | 6.6403 | 1.4023 | 0.6375 | 1.4003 | 0.0119 | 0.2750 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `kc_break_up_at_h` | one_head_filter_pi_star | 36 | 3.2265 | 1.2668 | 0.5556 | 0.7024 | 0.0074 | 0.4167 | EBR>35% | RAN |
| ETHUSDT | 8 | `wr_cross_down_neg20` | one_head_filter_pi_star | 158 | 13.0384 | 1.2237 | 0.5886 | 1.0210 | 0.0073 | 0.1962 | ok | RAN |
| SOLUSDT | 4 | `wr_cross_down_neg20` | one_head_filter_pi_star | 196 | 15.9819 | 1.3700 | 0.5816 | 1.8619 | 0.0054 | 0.2296 | ok | RAN |
| SOLUSDT | 8 | `wr_cross_down_neg20` | one_head_filter_pi_star | 212 | 17.2866 | 1.3468 | 0.5849 | 1.8642 | 0.0052 | 0.2453 | ok | RAN |
| SOLUSDT | 8 | `psar_flip_down` | one_head_filter_pi_star | 87 | 7.0940 | 1.2989 | 0.5862 | 1.1154 | 0.0044 | 0.1954 | ok | RAN |
| ETHUSDT | 4 | `wr_cross_down_neg20` | one_head_filter_pi_star | 148 | 12.2132 | 1.1234 | 0.5811 | 0.5655 | 0.0042 | 0.1757 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wr_overbought_at_h` | one_head_filter_pi_star | 14 | 1.9644 | 0.9061 | 0.5000 | -0.2392 | -0.0033 | 0.6429 | EBR>35% | RAN |
| ETHUSDT | 8 | `psar_flip_down` | one_head_filter_pi_star | 60 | 5.2802 | 0.7246 | 0.5167 | -1.0929 | -0.0101 | 0.1500 | ok | RAN |
| BTCUSDT | 4 | `kc_break_up_at_h` | one_head_filter_pi_star | 13 | 1.2533 | 0.9120 | 0.4615 | -0.1478 | -0.0162 | 0.0769 | TPM<MIN | RAN |
| SOLUSDT | 4 | `psar_flip_down` | one_head_filter_pi_star | 11 | 1.0811 | 0.5074 | 0.3636 | -1.1043 | -0.0171 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wr_cross_down_neg20` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wr_cross_down_neg20` | one_head_filter_pi_star | 16 | 1.3616 | 0.1082 | 0.1875 | -2.3673 | -0.0983 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wr_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `psar_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wr_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `psar_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wr_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `kc_break_up_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `kc_break_down_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wr_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wr_cross_up_neg80` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `kc_break_down_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `psar_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `psar_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wr_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wr_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wr_cross_up_neg80` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `kc_break_up_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `kc_break_down_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `psar_flip_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `psar_flip_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
