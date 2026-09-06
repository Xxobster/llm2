# Autonomy public-indicator hunt gen 161

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T200308Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema18_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema18_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema18_cross_down` | one_head_filter_pi_star | 35 | 2.9635 | 4.0907 | 0.7714 | 2.9020 | 0.0194 | 0.0857 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema18_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1907 | 0.6951 | 4.0606 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema18_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema18_cross_up` | one_head_filter_pi_star | 32 | 2.6332 | 1.2619 | 0.5938 | 0.5769 | 0.0100 | 0.2188 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema18_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.1890 | 0.5901 | 0.8787 | 0.0061 | 0.2050 | ok | RAN |
| ETHUSDT | 8 | `ema18_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1807 | 0.5912 | 0.8395 | 0.0058 | 0.2075 | ok | RAN |
| SOLUSDT | 8 | `ema18_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3625 | 0.5915 | 1.9661 | 0.0054 | 0.2394 | ok | RAN |
| SOLUSDT | 4 | `ema18_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3585 | 0.5972 | 1.9562 | 0.0053 | 0.2407 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema18_cross_down` | one_head_filter_pi_star | 29 | 2.9047 | 0.9887 | 0.4828 | -0.0271 | -0.0004 | 0.1724 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema18_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema18_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema18_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema18_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema18_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
