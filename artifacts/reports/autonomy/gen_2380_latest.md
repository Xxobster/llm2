# Autonomy public-indicator hunt gen 2380

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T111702Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1092_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0822 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1092_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1092_above_at_h` | one_head_filter_pi_star | 121 | 10.0567 | 1.1594 | 0.5868 | 0.7055 | 0.0029 | 0.1488 | ok | RAN |
| SOLUSDT | 8 | `ema1092_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.1124 | 0.5943 | 0.4706 | 0.0020 | 0.1415 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1092_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9433 | 0.5446 | -0.3897 | -0.0018 | 0.1562 | ok | RAN |
| SOLUSDT | 4 | `ema1092_below_at_h` | one_head_filter_pi_star | 271 | 22.0464 | 0.9139 | 0.5277 | -0.6248 | -0.0019 | 0.1365 | ok | RAN |
| SOLUSDT | 8 | `ema1092_below_at_h` | one_head_filter_pi_star | 238 | 19.4615 | 0.9128 | 0.5294 | -0.6009 | -0.0019 | 0.1261 | ok | RAN |
| ETHUSDT | 8 | `ema1092_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9327 | 0.5424 | -0.4849 | -0.0022 | 0.1525 | ok | RAN |
| ETHUSDT | 4 | `ema1092_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.9077 | 0.5517 | -0.4257 | -0.0041 | 0.1121 | ok | RAN |
| ETHUSDT | 8 | `ema1092_above_at_h` | one_head_filter_pi_star | 99 | 8.1703 | 0.7880 | 0.5051 | -0.9836 | -0.0097 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1092_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1092_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1092_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1092_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
