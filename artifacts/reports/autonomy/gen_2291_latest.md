# Autonomy public-indicator hunt gen 2291

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T233649Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma778_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2777 | 0.5989 | 1.4749 | 0.0074 | 0.1864 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma778_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2454 | 0.5909 | 1.3412 | 0.0071 | 0.1761 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma778_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.1050 | 0.5586 | 0.5155 | 0.0019 | 0.1310 | ok | RAN |
| SOLUSDT | 4 | `sma778_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0765 | 0.5522 | 0.3608 | 0.0014 | 0.1269 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma778_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9526 | 0.5490 | -0.2952 | -0.0010 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma778_below_at_h` | one_head_filter_pi_star | 207 | 16.9266 | 0.8821 | 0.5362 | -0.7657 | -0.0026 | 0.1304 | ok | RAN |
| ETHUSDT | 8 | `sma778_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8952 | 0.5667 | -0.5413 | -0.0042 | 0.1200 | ok | RAN |
| ETHUSDT | 4 | `sma778_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.8930 | 0.5634 | -0.5390 | -0.0044 | 0.1127 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma778_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma778_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma778_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma778_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma778_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma778_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
