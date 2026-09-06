# Autonomy public-indicator hunt gen 1877

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T212125Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret311_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.2201 | 0.6178 | 1.1413 | 0.0064 | 0.1975 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret311_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 1.1881 | 0.5976 | 1.0655 | 0.0057 | 0.2071 | ok | RAN |
| SOLUSDT | 8 | `ret311_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.1386 | 0.5644 | 0.6991 | 0.0026 | 0.1166 | ok | RAN |
| SOLUSDT | 4 | `ret311_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.0816 | 0.5395 | 0.4145 | 0.0015 | 0.1053 | ok | RAN |
| SOLUSDT | 8 | `ret311_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0642 | 0.5722 | 0.3636 | 0.0012 | 0.1556 | ok | RAN |
| SOLUSDT | 4 | `ret311_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.0044 | 0.5683 | 0.0262 | 0.0001 | 0.1366 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret311_pos_at_h` | one_head_filter_pi_star | 150 | 12.3782 | 0.8249 | 0.5400 | -0.9883 | -0.0073 | 0.0867 | ok | RAN |
| ETHUSDT | 8 | `ret311_pos_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 0.7984 | 0.5359 | -1.1295 | -0.0084 | 0.0850 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret311_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0678 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret311_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4330 | 0.2778 | -1.3217 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret311_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret311_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret311_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret311_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
