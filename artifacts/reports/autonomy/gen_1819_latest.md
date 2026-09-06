# Autonomy public-indicator hunt gen 1819

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T160754Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma716_below_at_h` | one_head_filter_pi_star | 155 | 12.6621 | 1.2124 | 0.5806 | 1.0992 | 0.0057 | 0.1806 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma716_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1240 | 0.5650 | 0.7090 | 0.0038 | 0.1751 | ok | RAN |
| SOLUSDT | 8 | `sma716_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.0597 | 0.5448 | 0.2844 | 0.0011 | 0.1269 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma716_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 0.9908 | 0.5312 | -0.0444 | -0.0002 | 0.1328 | ok | RAN |
| SOLUSDT | 8 | `sma716_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 0.9529 | 0.5584 | -0.2883 | -0.0010 | 0.1371 | ok | RAN |
| ETHUSDT | 4 | `sma716_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.9742 | 0.5693 | -0.1247 | -0.0010 | 0.1095 | ok | RAN |
| SOLUSDT | 4 | `sma716_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.9335 | 0.5500 | -0.4131 | -0.0014 | 0.1350 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma716_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.9309 | 0.5741 | -0.3792 | -0.0027 | 0.1049 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma716_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma716_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma716_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma716_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma716_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma716_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
