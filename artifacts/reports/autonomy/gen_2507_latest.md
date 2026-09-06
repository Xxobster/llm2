# Autonomy public-indicator hunt gen 2507

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T015302Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma807_below_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.1852 | 0.5882 | 0.9507 | 0.0052 | 0.1824 | ok | RAN |
| ETHUSDT | 8 | `sma807_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1717 | 0.5909 | 0.9565 | 0.0050 | 0.1761 | ok | RAN |
| SOLUSDT | 4 | `sma807_above_at_h` | one_head_filter_pi_star | 146 | 11.9049 | 1.1458 | 0.5616 | 0.6941 | 0.0026 | 0.1233 | ok | RAN |
| SOLUSDT | 8 | `sma807_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1263 | 0.5515 | 0.6618 | 0.0023 | 0.1152 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma807_below_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9165 | 0.5528 | -0.5263 | -0.0018 | 0.1307 | ok | RAN |
| SOLUSDT | 8 | `sma807_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.9131 | 0.5408 | -0.5458 | -0.0020 | 0.1276 | ok | RAN |
| ETHUSDT | 4 | `sma807_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.9234 | 0.5696 | -0.4013 | -0.0031 | 0.1076 | ok | RAN |
| ETHUSDT | 8 | `sma807_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8539 | 0.5486 | -0.8224 | -0.0059 | 0.0971 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma807_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma807_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma807_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma807_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma807_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma807_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
