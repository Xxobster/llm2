# Autonomy public-indicator hunt gen 057

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T131718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema821_cross_down_0` | one_head_filter_pi_star | 16 | 1.3679 | 11.4270 | 0.6875 | 2.7315 | 0.0528 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema821_cross_down_0` | one_head_filter_pi_star | 14 | 1.1969 | 10.0095 | 0.6429 | 2.4826 | 0.0497 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema821_cross_up_0` | one_head_filter_pi_star | 17 | 1.5812 | 1.9340 | 0.5882 | 1.1425 | 0.0274 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema821_cross_up_0` | one_head_filter_pi_star | 15 | 1.3952 | 1.9612 | 0.6000 | 1.0711 | 0.0254 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema821_neg_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0211 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema821_neg_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.7693 | 0.6727 | 3.7868 | 0.0203 | 0.3682 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema821_cross_up_0` | one_head_filter_pi_star | 24 | 2.1345 | 2.0157 | 0.6667 | 1.4410 | 0.0194 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema821_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2234 | 0.6928 | 4.1846 | 0.0185 | 0.4277 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema821_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1561 | 0.6914 | 3.9654 | 0.0175 | 0.4259 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema821_cross_up_0` | one_head_filter_pi_star | 21 | 2.0575 | 1.8048 | 0.6667 | 1.1865 | 0.0163 | 0.0952 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema821_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2621 | 0.6025 | 1.2020 | 0.0078 | 0.2050 | ok | RAN |
| ETHUSDT | 8 | `ema821_cross_down_0` | one_head_filter_pi_star | 37 | 3.0576 | 1.1626 | 0.5676 | 0.4022 | 0.0070 | 0.3243 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema821_pos_at_h` | one_head_filter_pi_star | 158 | 13.0384 | 1.1983 | 0.5949 | 0.9099 | 0.0063 | 0.2089 | ok | RAN |
| SOLUSDT | 8 | `ema821_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3776 | 0.6000 | 2.0374 | 0.0055 | 0.2419 | ok | RAN |
| SOLUSDT | 4 | `ema821_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3366 | 0.5943 | 1.8315 | 0.0050 | 0.2406 | ok | RAN |
| ETHUSDT | 4 | `ema821_cross_down_0` | one_head_filter_pi_star | 33 | 2.7271 | 1.0393 | 0.5455 | 0.0987 | 0.0019 | 0.3030 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema821_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema821_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema821_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema821_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema821_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema821_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema821_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema821_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
