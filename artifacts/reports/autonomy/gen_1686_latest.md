# Autonomy public-indicator hunt gen 1686

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T032002Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma441_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.1417 | 0.5938 | 0.8618 | 0.0043 | 0.1823 | ok | RAN |
| ETHUSDT | 8 | `wma441_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.0967 | 0.5798 | 0.5827 | 0.0030 | 0.1915 | ok | RAN |
| SOLUSDT | 8 | `wma441_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 1.0804 | 0.5740 | 0.4203 | 0.0017 | 0.1598 | ok | RAN |
| SOLUSDT | 4 | `wma441_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0713 | 0.5723 | 0.3957 | 0.0015 | 0.1503 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma441_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 0.9902 | 0.5469 | -0.0578 | -0.0002 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `wma441_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 0.9622 | 0.5368 | -0.2272 | -0.0007 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma441_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8610 | 0.5449 | -0.8372 | -0.0056 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma441_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8481 | 0.5351 | -0.9455 | -0.0062 | 0.0973 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma441_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma441_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma441_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma441_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma441_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma441_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
