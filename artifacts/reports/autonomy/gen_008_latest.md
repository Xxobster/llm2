# Autonomy public-indicator hunt gen 008

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T072015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `rsi_oversold_at_h` | one_head_filter_pi_star | 20 | 1.8804 | 7.5317 | 0.9000 | 3.9262 | 0.0596 | 0.6000 | EBR>35% | RAN |
| ETHUSDT | 8 | `rsi_oversold_at_h` | one_head_filter_pi_star | 18 | 2.0101 | 3.0951 | 0.7778 | 2.4809 | 0.0521 | 0.6111 | EBR>35% | RAN |
| ETHUSDT | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 76 | 6.2865 | 2.6680 | 0.7500 | 3.6788 | 0.0318 | 0.4868 | EBR>35% | RAN |
| ETHUSDT | 8 | `rsi_cross_up_30` | one_head_filter_pi_star | 111 | 9.0677 | 2.3616 | 0.7297 | 4.2993 | 0.0298 | 0.4414 | EBR>35% | RAN |
| SOLUSDT | 4 | `rsi_oversold_at_h` | one_head_filter_pi_star | 42 | 3.6716 | 2.7859 | 0.7381 | 2.7840 | 0.0286 | 0.6190 | EBR>35% | RAN |
| SOLUSDT | 8 | `rsi_overbought_at_h` | one_head_filter_pi_star | 13 | 1.5221 | 2.3755 | 0.6923 | 1.8106 | 0.0247 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `rsi_overbought_at_h` | one_head_filter_pi_star | 30 | 2.5508 | 2.7838 | 0.7333 | 2.5788 | 0.0247 | 0.4667 | EBR>35% | RAN |
| SOLUSDT | 8 | `rsi_cross_up_30` | one_head_filter_pi_star | 91 | 7.5704 | 2.3626 | 0.7033 | 3.3535 | 0.0196 | 0.4835 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 56 | 4.6587 | 1.7505 | 0.6429 | 1.8070 | 0.0128 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `rsi_cross_down_70` | one_head_filter_pi_star | 83 | 6.8499 | 1.3270 | 0.6145 | 1.1238 | 0.0108 | 0.2048 | ok | RAN |
| ETHUSDT | 4 | `rsi_overbought_at_h` | one_head_filter_pi_star | 33 | 2.9020 | 1.2413 | 0.5758 | 0.5794 | 0.0103 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `rsi_cross_down_70` | one_head_filter_pi_star | 105 | 8.5617 | 1.4513 | 0.6190 | 1.7190 | 0.0074 | 0.2762 | ok | RAN |
| SOLUSDT | 4 | `rsi_cross_down_70` | one_head_filter_pi_star | 81 | 6.6048 | 1.3107 | 0.5926 | 1.0997 | 0.0055 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `rsi_cross_down_70` | one_head_filter_pi_star | 60 | 4.9517 | 1.0330 | 0.5833 | 0.1017 | 0.0012 | 0.1167 | ok | RAN |
| BTCUSDT | 8 | `rsi_cross_down_70` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0476 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `rsi_cross_down_70` | one_head_filter_pi_star | 12 | 1.1012 | 0.0676 | 0.0833 | -2.3882 | -0.1143 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `rsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `rsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `rsi_cross_up_30` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rsi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rsi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `rsi_cross_up_30` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
