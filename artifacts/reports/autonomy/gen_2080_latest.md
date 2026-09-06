# Autonomy public-indicator hunt gen 2080

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T192504Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma4800_above_at_h` | one_head_filter_pi_star | 47 | 4.0022 | 1.8760 | 0.6170 | 1.5851 | 0.0122 | 0.0851 | ok | RAN |
| SOLUSDT | 8 | `sma4800_above_at_h` | one_head_filter_pi_star | 67 | 5.6273 | 1.6276 | 0.6269 | 1.5478 | 0.0097 | 0.0896 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4800_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 1.0124 | 0.5478 | 0.0926 | 0.0002 | 0.1401 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma4800_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.0014 | 0.5575 | 0.0112 | 0.0000 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `sma4800_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9749 | 0.5552 | -0.2017 | -0.0008 | 0.1343 | ok | RAN |
| SOLUSDT | 8 | `sma4800_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9500 | 0.5331 | -0.3898 | -0.0010 | 0.1293 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4800_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.7998 | 0.5000 | -1.0154 | -0.0098 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `sma4800_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.7731 | 0.5000 | -1.2211 | -0.0129 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4800_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
