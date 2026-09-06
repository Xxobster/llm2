# Autonomy public-indicator hunt gen 012

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T081533Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `mfi_oversold_at_h` | one_head_filter_pi_star | 18 | 1.9490 | 3.3179 | 0.8333 | 2.0593 | 0.0403 | 0.3889 | EBR>35% | RAN |
| ETHUSDT | 4 | `mfi_cross_up_20` | one_head_filter_pi_star | 48 | 4.0471 | 3.3919 | 0.7708 | 3.4420 | 0.0349 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `mfi_cross_up_20` | one_head_filter_pi_star | 57 | 4.8059 | 3.0123 | 0.7544 | 3.4824 | 0.0306 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `mfi_overbought_at_h` | one_head_filter_pi_star | 23 | 2.0399 | 2.2548 | 0.6087 | 1.7379 | 0.0300 | 0.2174 | TPM<MIN | RAN |
| SOLUSDT | 4 | `mfi_oversold_at_h` | one_head_filter_pi_star | 24 | 2.3457 | 2.8358 | 0.7083 | 2.2081 | 0.0280 | 0.4583 | EBR>35% | RAN |
| SOLUSDT | 8 | `mfi_cross_up_20` | one_head_filter_pi_star | 57 | 4.7978 | 2.3833 | 0.7018 | 2.8940 | 0.0194 | 0.4561 | EBR>35% | RAN |
| SOLUSDT | 4 | `mfi_cross_up_20` | one_head_filter_pi_star | 35 | 3.0828 | 1.9657 | 0.6857 | 1.7514 | 0.0168 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `mfi_cross_down_80` | one_head_filter_pi_star | 49 | 4.0725 | 1.9698 | 0.6735 | 2.0168 | 0.0135 | 0.3061 | ok | RAN |
| SOLUSDT | 8 | `mfi_cross_down_80` | one_head_filter_pi_star | 65 | 5.4023 | 1.6985 | 0.6308 | 1.9455 | 0.0113 | 0.2923 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `mfi_oversold_at_h` | one_head_filter_pi_star | 20 | 1.7484 | 1.4749 | 0.6500 | 0.7990 | 0.0099 | 0.5500 | EBR>35% | RAN |
| ETHUSDT | 4 | `mfi_cross_down_80` | one_head_filter_pi_star | 36 | 3.0291 | 1.1675 | 0.5833 | 0.4055 | 0.0049 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `mfi_cross_down_80` | one_head_filter_pi_star | 58 | 4.7866 | 1.1171 | 0.5690 | 0.3790 | 0.0035 | 0.2069 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `mfi_cross_down_80` | one_head_filter_pi_star | 14 | 1.7704 | 0.5407 | 0.2857 | -1.0796 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `mfi_cross_down_80` | one_head_filter_pi_star | 11 | 2.0796 | 0.1502 | 0.2727 | -2.8529 | -0.1297 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `mfi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `mfi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `mfi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `mfi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `mfi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `mfi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `mfi_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mfi_oversold_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mfi_overbought_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `mfi_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
