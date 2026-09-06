# Autonomy public-indicator hunt gen 1749

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T094232Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret293_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1671 | 0.5922 | 0.9744 | 0.0054 | 0.2067 | ok | RAN |
| ETHUSDT | 4 | `ret293_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1725 | 0.6145 | 0.9824 | 0.0052 | 0.1867 | ok | RAN |
| SOLUSDT | 8 | `ret293_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.0790 | 0.5607 | 0.4181 | 0.0015 | 0.1156 | ok | RAN |
| SOLUSDT | 4 | `ret293_neg_at_h` | one_head_filter_pi_star | 143 | 11.6932 | 1.0555 | 0.5664 | 0.2922 | 0.0012 | 0.1538 | ok | RAN |
| SOLUSDT | 4 | `ret293_pos_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.0271 | 0.5444 | 0.1469 | 0.0005 | 0.1006 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret293_neg_at_h` | one_head_filter_pi_star | 146 | 11.9385 | 0.9755 | 0.5548 | -0.1319 | -0.0005 | 0.1507 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret293_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 0.8383 | 0.5376 | -0.9440 | -0.0065 | 0.1098 | ok | RAN |
| ETHUSDT | 4 | `ret293_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 0.8125 | 0.5398 | -1.1262 | -0.0077 | 0.0966 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret293_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4194 | 0.3000 | -1.4074 | -0.0661 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret293_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret293_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret293_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret293_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret293_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
