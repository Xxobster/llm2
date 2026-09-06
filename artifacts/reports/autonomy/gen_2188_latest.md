# Autonomy public-indicator hunt gen 2188

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T105623Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1067_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1067_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1067_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.2270 | 0.6071 | 0.9220 | 0.0039 | 0.1429 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1067_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0552 | 0.5546 | 0.2450 | 0.0010 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1067_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9948 | 0.5455 | -0.0359 | -0.0001 | 0.1326 | ok | RAN |
| ETHUSDT | 8 | `ema1067_below_at_h` | one_head_filter_pi_star | 245 | 20.0143 | 0.9628 | 0.5469 | -0.2778 | -0.0012 | 0.1551 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1067_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 0.9442 | 0.5493 | -0.3695 | -0.0017 | 0.1549 | ok | RAN |
| SOLUSDT | 4 | `ema1067_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9210 | 0.5364 | -0.5645 | -0.0017 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `ema1067_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 0.9252 | 0.5556 | -0.3570 | -0.0032 | 0.1270 | ok | RAN |
| ETHUSDT | 8 | `ema1067_above_at_h` | one_head_filter_pi_star | 115 | 9.4529 | 0.9069 | 0.5478 | -0.4187 | -0.0039 | 0.1304 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1067_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1067_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1067_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1067_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
