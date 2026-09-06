# Autonomy public-indicator hunt gen 1625

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T202835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema3620_above_at_h` | one_head_filter_pi_star | 73 | 6.0010 | 1.7842 | 0.6712 | 1.8699 | 0.0098 | 0.1233 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3620_above_at_h` | one_head_filter_pi_star | 86 | 7.0697 | 1.5453 | 0.6512 | 1.5694 | 0.0076 | 0.1279 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3620_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 1.0560 | 0.5483 | 0.3926 | 0.0011 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema3620_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 0.9998 | 0.5379 | -0.0016 | -0.0000 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema3620_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9881 | 0.5588 | -0.0947 | -0.0004 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3620_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9420 | 0.5523 | -0.4923 | -0.0020 | 0.1395 | ok | RAN |
| ETHUSDT | 8 | `ema3620_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.6868 | 0.4706 | -1.6631 | -0.0154 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3620_above_at_h` | one_head_filter_pi_star | 33 | 9.7370 | 0.5767 | 0.4242 | -2.3810 | -0.0255 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
