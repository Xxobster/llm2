# Autonomy public-indicator hunt gen 1893

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T224654Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret314_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2616 | 0.6185 | 1.4102 | 0.0076 | 0.1850 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret314_neg_at_h` | one_head_filter_pi_star | 157 | 12.8255 | 1.1840 | 0.5860 | 0.9766 | 0.0054 | 0.1975 | ok | RAN |
| SOLUSDT | 8 | `ret314_pos_at_h` | one_head_filter_pi_star | 152 | 12.4648 | 1.2426 | 0.5658 | 1.1330 | 0.0043 | 0.1184 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret314_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.1487 | 0.5570 | 0.7422 | 0.0028 | 0.1076 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret314_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 0.9950 | 0.5625 | -0.0299 | -0.0001 | 0.1420 | ok | RAN |
| SOLUSDT | 8 | `ret314_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 0.9326 | 0.5471 | -0.4039 | -0.0014 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret314_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8492 | 0.5422 | -0.8538 | -0.0059 | 0.0843 | ok | RAN |
| ETHUSDT | 8 | `ret314_pos_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8607 | 0.5506 | -0.7842 | -0.0059 | 0.0949 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret314_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4142 | 0.2632 | -1.4203 | -0.0718 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret314_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret314_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret314_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret314_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret314_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
