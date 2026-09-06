# Autonomy public-indicator hunt gen 1707

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T054045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma702_below_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1662 | 0.5829 | 0.9504 | 0.0049 | 0.1886 | ok | RAN |
| ETHUSDT | 8 | `sma702_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1355 | 0.5689 | 0.7395 | 0.0041 | 0.1737 | ok | RAN |
| SOLUSDT | 8 | `sma702_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0767 | 0.5556 | 0.3709 | 0.0014 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `sma702_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.0334 | 0.5338 | 0.1615 | 0.0006 | 0.1203 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma702_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 0.9588 | 0.5550 | -0.2509 | -0.0009 | 0.1350 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma702_below_at_h` | one_head_filter_pi_star | 195 | 15.8636 | 0.9159 | 0.5538 | -0.5232 | -0.0018 | 0.1436 | ok | RAN |
| ETHUSDT | 8 | `sma702_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 0.9057 | 0.5682 | -0.4849 | -0.0036 | 0.1061 | ok | RAN |
| ETHUSDT | 4 | `sma702_above_at_h` | one_head_filter_pi_star | 137 | 11.3054 | 0.8256 | 0.5401 | -0.9025 | -0.0074 | 0.0949 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma702_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma702_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma702_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma702_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma702_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma702_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
