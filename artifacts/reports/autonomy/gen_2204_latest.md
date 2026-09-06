# Autonomy public-indicator hunt gen 2204

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T130234Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1069_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1069_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.3267 | 0.6306 | 1.2914 | 0.0053 | 0.1351 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1069_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.2462 | 0.5913 | 0.9919 | 0.0042 | 0.1391 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1069_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 0.9874 | 0.5433 | -0.0851 | -0.0003 | 0.1378 | ok | RAN |
| SOLUSDT | 4 | `ema1069_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9485 | 0.5399 | -0.3662 | -0.0011 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema1069_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9571 | 0.5371 | -0.2994 | -0.0014 | 0.1572 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1069_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9372 | 0.5489 | -0.4500 | -0.0020 | 0.1447 | ok | RAN |
| ETHUSDT | 4 | `ema1069_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.8544 | 0.5385 | -0.6826 | -0.0067 | 0.1197 | ok | RAN |
| ETHUSDT | 8 | `ema1069_above_at_h` | one_head_filter_pi_star | 114 | 9.3707 | 0.8367 | 0.5263 | -0.7732 | -0.0071 | 0.1228 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1069_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1069_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1069_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1069_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1069_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
