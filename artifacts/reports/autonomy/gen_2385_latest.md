# Autonomy public-indicator hunt gen 2385

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T115749Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5520_above_at_h` | one_head_filter_pi_star | 51 | 4.7165 | 1.6780 | 0.5882 | 1.5067 | 0.0091 | 0.1176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema5520_above_at_h` | one_head_filter_pi_star | 45 | 3.8661 | 1.3851 | 0.6000 | 0.8416 | 0.0061 | 0.1111 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5520_below_at_h` | one_head_filter_pi_star | 330 | 26.9844 | 0.9541 | 0.5364 | -0.3686 | -0.0009 | 0.1273 | ok | RAN |
| SOLUSDT | 8 | `ema5520_below_at_h` | one_head_filter_pi_star | 315 | 25.7578 | 0.9504 | 0.5302 | -0.3874 | -0.0010 | 0.1365 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5520_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9480 | 0.5536 | -0.4321 | -0.0017 | 0.1369 | ok | RAN |
| ETHUSDT | 8 | `ema5520_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9213 | 0.5510 | -0.6732 | -0.0027 | 0.1370 | ok | RAN |
| ETHUSDT | 8 | `ema5520_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.8910 | 0.5250 | -0.5410 | -0.0059 | 0.1750 | ok | RAN |
| ETHUSDT | 4 | `ema5520_above_at_h` | one_head_filter_pi_star | 59 | 6.7254 | 0.8827 | 0.5424 | -0.4637 | -0.0061 | 0.1525 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5520_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5520_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5520_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5520_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5520_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
