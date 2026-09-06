# Autonomy public-indicator hunt gen 1907

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T000256Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma728_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1694 | 0.5824 | 0.9423 | 0.0047 | 0.1882 | ok | RAN |
| SOLUSDT | 8 | `sma728_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.1887 | 0.5669 | 0.8425 | 0.0033 | 0.1260 | ok | RAN |
| ETHUSDT | 8 | `sma728_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.0982 | 0.5714 | 0.6080 | 0.0030 | 0.1813 | ok | RAN |
| SOLUSDT | 4 | `sma728_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 1.0792 | 0.5510 | 0.3865 | 0.0015 | 0.1156 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma728_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 0.9983 | 0.5654 | -0.0105 | -0.0000 | 0.1262 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma728_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.9110 | 0.5440 | -0.5528 | -0.0019 | 0.1399 | ok | RAN |
| ETHUSDT | 4 | `sma728_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8774 | 0.5646 | -0.6483 | -0.0050 | 0.1020 | ok | RAN |
| ETHUSDT | 8 | `sma728_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 0.8555 | 0.5586 | -0.7563 | -0.0059 | 0.1103 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma728_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma728_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma728_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma728_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma728_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma728_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
