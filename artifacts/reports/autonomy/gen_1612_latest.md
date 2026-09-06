# Autonomy public-indicator hunt gen 1612

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T191643Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema989_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema989_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 1.0609 | 0.5833 | 0.2751 | 0.0024 | 0.1212 | ok | RAN |
| SOLUSDT | 4 | `ema989_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.1039 | 0.5593 | 0.4751 | 0.0019 | 0.1186 | ok | RAN |
| SOLUSDT | 8 | `ema989_below_at_h` | one_head_filter_pi_star | 251 | 20.5245 | 1.0467 | 0.5578 | 0.3043 | 0.0010 | 0.1315 | ok | RAN |
| SOLUSDT | 8 | `ema989_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.0347 | 0.5575 | 0.1556 | 0.0006 | 0.1239 | ok | RAN |
| ETHUSDT | 4 | `ema989_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.0110 | 0.5617 | 0.0745 | 0.0003 | 0.1489 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema989_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9403 | 0.5349 | -0.4156 | -0.0013 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema989_above_at_h` | one_head_filter_pi_star | 129 | 10.6453 | 0.9606 | 0.5581 | -0.1866 | -0.0017 | 0.1318 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema989_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 0.8646 | 0.5268 | -0.9788 | -0.0044 | 0.1518 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema989_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema989_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema989_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema989_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema989_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
