# Autonomy public-indicator hunt gen 1782

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T124542Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma456_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1777 | 0.5944 | 1.0009 | 0.0055 | 0.1889 | ok | RAN |
| ETHUSDT | 4 | `wma456_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1309 | 0.5876 | 0.7763 | 0.0041 | 0.2034 | ok | RAN |
| SOLUSDT | 8 | `wma456_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0583 | 0.5640 | 0.3265 | 0.0012 | 0.1686 | ok | RAN |
| SOLUSDT | 4 | `wma456_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0515 | 0.5698 | 0.2886 | 0.0011 | 0.1628 | ok | RAN |
| SOLUSDT | 8 | `wma456_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0353 | 0.5430 | 0.2032 | 0.0006 | 0.1075 | ok | RAN |
| SOLUSDT | 4 | `wma456_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0218 | 0.5521 | 0.1260 | 0.0004 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma456_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8410 | 0.5368 | -0.9954 | -0.0063 | 0.0947 | ok | RAN |
| ETHUSDT | 8 | `wma456_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7860 | 0.5309 | -1.4040 | -0.0090 | 0.0876 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma456_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma456_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma456_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma456_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma456_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma456_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
