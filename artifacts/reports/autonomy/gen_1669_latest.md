# Autonomy public-indicator hunt gen 1669

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T005232Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret282_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.1539 | 0.6012 | 0.8633 | 0.0046 | 0.1902 | ok | RAN |
| ETHUSDT | 4 | `ret282_neg_at_h` | one_head_filter_pi_star | 153 | 12.4987 | 1.1009 | 0.5817 | 0.5362 | 0.0031 | 0.1895 | ok | RAN |
| SOLUSDT | 8 | `ret282_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.1195 | 0.5569 | 0.6082 | 0.0022 | 0.1138 | ok | RAN |
| SOLUSDT | 4 | `ret282_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.0872 | 0.5610 | 0.4412 | 0.0016 | 0.0915 | ok | RAN |
| SOLUSDT | 4 | `ret282_neg_at_h` | one_head_filter_pi_star | 146 | 11.9385 | 1.0420 | 0.5685 | 0.2252 | 0.0009 | 0.1575 | ok | RAN |
| SOLUSDT | 8 | `ret282_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.0128 | 0.5532 | 0.0747 | 0.0003 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret282_pos_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.9015 | 0.5556 | -0.5514 | -0.0038 | 0.1049 | ok | RAN |
| ETHUSDT | 8 | `ret282_pos_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.8764 | 0.5497 | -0.7179 | -0.0048 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret282_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0652 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret282_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0688 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret282_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret282_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret282_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret282_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
