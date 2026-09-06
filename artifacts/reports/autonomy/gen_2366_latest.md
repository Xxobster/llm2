# Autonomy public-indicator hunt gen 2366

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T091035Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma547_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.1672 | 0.5936 | 0.9939 | 0.0050 | 0.1872 | ok | RAN |
| ETHUSDT | 8 | `wma547_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1448 | 0.5892 | 0.8749 | 0.0044 | 0.1838 | ok | RAN |
| SOLUSDT | 4 | `wma547_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.1136 | 0.5585 | 0.6416 | 0.0021 | 0.1011 | ok | RAN |
| SOLUSDT | 8 | `wma547_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.1155 | 0.5568 | 0.6300 | 0.0020 | 0.0973 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma547_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 0.9899 | 0.5625 | -0.0600 | -0.0002 | 0.1534 | ok | RAN |
| SOLUSDT | 8 | `wma547_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 0.9591 | 0.5479 | -0.2521 | -0.0009 | 0.1596 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma547_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8075 | 0.5241 | -1.2406 | -0.0078 | 0.0963 | ok | RAN |
| ETHUSDT | 4 | `wma547_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8108 | 0.5344 | -1.2335 | -0.0079 | 0.0952 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma547_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma547_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma547_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma547_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma547_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma547_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
