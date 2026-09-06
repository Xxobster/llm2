# Autonomy public-indicator hunt gen 1604

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T183235Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema988_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema988_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.1200 | 0.5645 | 0.5505 | 0.0021 | 0.1290 | ok | RAN |
| SOLUSDT | 4 | `ema988_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.0653 | 0.5680 | 0.3046 | 0.0012 | 0.1280 | ok | RAN |
| ETHUSDT | 8 | `ema988_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.0252 | 0.5575 | 0.1665 | 0.0008 | 0.1549 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema988_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.9992 | 0.5536 | -0.0053 | -0.0000 | 0.1518 | ok | RAN |
| ETHUSDT | 8 | `ema988_above_at_h` | one_head_filter_pi_star | 143 | 11.8016 | 0.9810 | 0.5524 | -0.0922 | -0.0008 | 0.1259 | ok | RAN |
| SOLUSDT | 4 | `ema988_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 0.9444 | 0.5385 | -0.3773 | -0.0012 | 0.1296 | ok | RAN |
| SOLUSDT | 8 | `ema988_below_at_h` | one_head_filter_pi_star | 232 | 18.9708 | 0.9234 | 0.5388 | -0.5066 | -0.0017 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema988_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.9074 | 0.5620 | -0.4389 | -0.0040 | 0.1240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema988_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema988_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema988_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema988_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema988_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
