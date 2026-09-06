# Autonomy public-indicator hunt gen 2065

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T172332Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4720_above_at_h` | one_head_filter_pi_star | 56 | 4.8111 | 1.5749 | 0.6250 | 1.3378 | 0.0092 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4720_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.4787 | 0.6290 | 1.2100 | 0.0079 | 0.1129 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4720_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9930 | 0.5387 | -0.0534 | -0.0001 | 0.1323 | ok | RAN |
| SOLUSDT | 8 | `ema4720_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9788 | 0.5389 | -0.1669 | -0.0004 | 0.1340 | ok | RAN |
| ETHUSDT | 8 | `ema4720_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9645 | 0.5572 | -0.2903 | -0.0012 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema4720_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9530 | 0.5546 | -0.3797 | -0.0016 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4720_above_at_h` | one_head_filter_pi_star | 39 | 11.3833 | 0.8391 | 0.5128 | -0.8819 | -0.0085 | 0.1795 | ok | RAN |
| ETHUSDT | 4 | `ema4720_above_at_h` | one_head_filter_pi_star | 37 | 10.7995 | 0.8346 | 0.5135 | -0.9799 | -0.0085 | 0.1622 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4720_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4720_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
