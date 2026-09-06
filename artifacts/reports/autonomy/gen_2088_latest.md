# Autonomy public-indicator hunt gen 2088

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T203035Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4820_above_at_h` | one_head_filter_pi_star | 50 | 4.1995 | 1.8416 | 0.6000 | 1.5642 | 0.0105 | 0.0600 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma4820_above_at_h` | one_head_filter_pi_star | 64 | 5.3753 | 1.1618 | 0.5625 | 0.4578 | 0.0030 | 0.1094 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma4820_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9950 | 0.5425 | -0.0375 | -0.0001 | 0.1340 | ok | RAN |
| SOLUSDT | 4 | `sma4820_below_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 0.9722 | 0.5380 | -0.2084 | -0.0006 | 0.1320 | ok | RAN |
| ETHUSDT | 8 | `sma4820_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9683 | 0.5546 | -0.2539 | -0.0010 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `sma4820_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9570 | 0.5506 | -0.3459 | -0.0014 | 0.1369 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma4820_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9022 | 0.5294 | -0.4750 | -0.0046 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4820_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.6593 | 0.4722 | -1.8799 | -0.0194 | 0.1389 | ok | RAN |
| ETHUSDT | 4 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
