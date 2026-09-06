# Autonomy public-indicator hunt gen 2101

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T222351Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret343_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2968 | 0.6140 | 1.5413 | 0.0085 | 0.1930 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret343_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2612 | 0.5906 | 1.3580 | 0.0078 | 0.2047 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret343_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.2294 | 0.5665 | 1.1355 | 0.0041 | 0.1156 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret343_pos_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.1754 | 0.5671 | 0.8755 | 0.0032 | 0.1098 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret343_neg_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9557 | 0.5665 | -0.2764 | -0.0009 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret343_neg_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 0.9500 | 0.5588 | -0.3220 | -0.0010 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret343_pos_at_h` | one_head_filter_pi_star | 192 | 15.7304 | 0.8093 | 0.5469 | -1.2108 | -0.0082 | 0.0938 | ok | RAN |
| ETHUSDT | 8 | `ret343_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8084 | 0.5486 | -1.1573 | -0.0083 | 0.0857 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret343_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret343_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret343_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret343_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret343_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret343_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
