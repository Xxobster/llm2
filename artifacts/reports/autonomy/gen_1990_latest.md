# Autonomy public-indicator hunt gen 1990

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T080053Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma488_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1402 | 0.5912 | 0.8173 | 0.0042 | 0.1823 | ok | RAN |
| ETHUSDT | 4 | `wma488_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1338 | 0.5856 | 0.7954 | 0.0042 | 0.1934 | ok | RAN |
| SOLUSDT | 4 | `wma488_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0327 | 0.5469 | 0.1905 | 0.0006 | 0.0990 | ok | RAN |
| SOLUSDT | 8 | `wma488_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0194 | 0.5549 | 0.1152 | 0.0004 | 0.1593 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma488_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9864 | 0.5531 | -0.0789 | -0.0003 | 0.1508 | ok | RAN |
| SOLUSDT | 8 | `wma488_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 0.9799 | 0.5278 | -0.1167 | -0.0004 | 0.1056 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma488_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8270 | 0.5414 | -1.0756 | -0.0070 | 0.0994 | ok | RAN |
| ETHUSDT | 4 | `wma488_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.8153 | 0.5326 | -1.1648 | -0.0076 | 0.0978 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma488_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma488_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma488_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma488_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma488_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma488_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
