# Autonomy public-indicator hunt gen 2323

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T032650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma783_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1841 | 0.5805 | 1.0295 | 0.0053 | 0.1839 | ok | RAN |
| ETHUSDT | 4 | `sma783_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1496 | 0.5801 | 0.8285 | 0.0043 | 0.1878 | ok | RAN |
| SOLUSDT | 8 | `sma783_above_at_h` | one_head_filter_pi_star | 128 | 10.4966 | 1.0992 | 0.5547 | 0.4501 | 0.0018 | 0.1172 | ok | RAN |
| SOLUSDT | 4 | `sma783_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0303 | 0.5426 | 0.1446 | 0.0006 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma783_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9421 | 0.5610 | -0.3583 | -0.0012 | 0.1268 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma783_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9046 | 0.5320 | -0.6055 | -0.0021 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma783_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 0.9249 | 0.5665 | -0.4095 | -0.0030 | 0.0983 | ok | RAN |
| ETHUSDT | 4 | `sma783_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8792 | 0.5600 | -0.6369 | -0.0051 | 0.1133 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma783_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma783_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma783_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma783_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma783_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma783_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
