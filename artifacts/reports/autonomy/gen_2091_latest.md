# Autonomy public-indicator hunt gen 2091

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T205722Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma752_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1946 | 0.5944 | 1.1017 | 0.0056 | 0.1889 | ok | RAN |
| ETHUSDT | 8 | `sma752_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.0803 | 0.5682 | 0.4886 | 0.0024 | 0.1761 | ok | RAN |
| SOLUSDT | 8 | `sma752_above_at_h` | one_head_filter_pi_star | 125 | 10.2512 | 1.1087 | 0.5520 | 0.4981 | 0.0020 | 0.1200 | ok | RAN |
| SOLUSDT | 4 | `sma752_above_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.0964 | 0.5430 | 0.4881 | 0.0018 | 0.1060 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma752_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9366 | 0.5476 | -0.4025 | -0.0013 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma752_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 0.9032 | 0.5529 | -0.6167 | -0.0021 | 0.1346 | ok | RAN |
| ETHUSDT | 8 | `sma752_above_at_h` | one_head_filter_pi_star | 136 | 11.1790 | 0.9478 | 0.5735 | -0.2624 | -0.0021 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `sma752_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8995 | 0.5616 | -0.5089 | -0.0042 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma752_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0535 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma752_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma752_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma752_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma752_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma752_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
