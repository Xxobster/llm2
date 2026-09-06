# Autonomy public-indicator hunt gen 1715

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T062802Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma703_below_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2526 | 0.5951 | 1.2924 | 0.0070 | 0.1963 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma703_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1806 | 0.5805 | 0.9849 | 0.0053 | 0.1839 | ok | RAN |
| SOLUSDT | 8 | `sma703_above_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.1038 | 0.5537 | 0.4631 | 0.0020 | 0.1322 | ok | RAN |
| SOLUSDT | 4 | `sma703_above_at_h` | one_head_filter_pi_star | 138 | 11.3167 | 1.0051 | 0.5362 | 0.0254 | 0.0001 | 0.1087 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma703_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 1.0036 | 0.5672 | 0.0220 | 0.0001 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma703_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 0.8845 | 0.5400 | -0.7278 | -0.0025 | 0.1400 | ok | RAN |
| ETHUSDT | 4 | `sma703_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 0.9162 | 0.5573 | -0.4189 | -0.0034 | 0.1221 | ok | RAN |
| ETHUSDT | 8 | `sma703_above_at_h` | one_head_filter_pi_star | 137 | 11.2612 | 0.8889 | 0.5547 | -0.5815 | -0.0044 | 0.1168 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma703_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma703_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0688 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma703_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma703_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma703_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma703_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
