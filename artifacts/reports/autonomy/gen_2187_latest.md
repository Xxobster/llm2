# Autonomy public-indicator hunt gen 2187

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T104911Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma765_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1691 | 0.5879 | 1.0046 | 0.0051 | 0.1813 | ok | RAN |
| ETHUSDT | 4 | `sma765_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.1701 | 0.5876 | 0.9968 | 0.0050 | 0.1856 | ok | RAN |
| SOLUSDT | 8 | `sma765_above_at_h` | one_head_filter_pi_star | 117 | 9.5951 | 1.0879 | 0.5641 | 0.3827 | 0.0016 | 0.1453 | ok | RAN |
| SOLUSDT | 4 | `sma765_above_at_h` | one_head_filter_pi_star | 130 | 10.6606 | 1.0837 | 0.5538 | 0.3897 | 0.0016 | 0.1077 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma765_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9784 | 0.5535 | -0.1369 | -0.0005 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma765_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.9492 | 0.5743 | -0.2592 | -0.0020 | 0.1149 | ok | RAN |
| SOLUSDT | 8 | `sma765_below_at_h` | one_head_filter_pi_star | 216 | 17.5720 | 0.9061 | 0.5324 | -0.6142 | -0.0020 | 0.1343 | ok | RAN |
| ETHUSDT | 4 | `sma765_above_at_h` | one_head_filter_pi_star | 151 | 12.4120 | 0.8647 | 0.5629 | -0.7247 | -0.0057 | 0.1060 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma765_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma765_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma765_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma765_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma765_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
