# Autonomy public-indicator hunt gen 1619

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T195451Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma690_below_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.1854 | 0.5750 | 0.9718 | 0.0054 | 0.1938 | ok | RAN |
| SOLUSDT | 8 | `sma690_above_at_h` | one_head_filter_pi_star | 101 | 8.2825 | 1.2833 | 0.5842 | 1.0858 | 0.0048 | 0.1188 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma690_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1504 | 0.5801 | 0.8657 | 0.0045 | 0.1878 | ok | RAN |
| SOLUSDT | 4 | `sma690_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.0141 | 0.5308 | 0.0692 | 0.0003 | 0.1231 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma690_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 0.9733 | 0.5502 | -0.1655 | -0.0006 | 0.1340 | ok | RAN |
| SOLUSDT | 4 | `sma690_below_at_h` | one_head_filter_pi_star | 191 | 15.5382 | 0.9416 | 0.5550 | -0.3522 | -0.0012 | 0.1361 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma690_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.8990 | 0.5629 | -0.5506 | -0.0042 | 0.1126 | ok | RAN |
| ETHUSDT | 4 | `sma690_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.7487 | 0.5307 | -1.5412 | -0.0110 | 0.1006 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma690_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma690_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma690_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma690_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
