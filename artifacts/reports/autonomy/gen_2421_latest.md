# Autonomy public-indicator hunt gen 2421

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T161541Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret389_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.2984 | 0.6188 | 1.5202 | 0.0086 | 0.1875 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret389_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2708 | 0.6158 | 1.4642 | 0.0079 | 0.1695 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret389_pos_at_h` | one_head_filter_pi_star | 122 | 10.0046 | 1.1925 | 0.5984 | 0.8239 | 0.0035 | 0.1148 | ok | RAN |
| SOLUSDT | 8 | `ret389_pos_at_h` | one_head_filter_pi_star | 146 | 11.9727 | 1.0401 | 0.5411 | 0.2055 | 0.0008 | 0.0959 | ok | RAN |
| SOLUSDT | 4 | `ret389_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.0102 | 0.5769 | 0.0613 | 0.0002 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret389_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 0.9187 | 0.5587 | -0.5056 | -0.0018 | 0.1508 | ok | RAN |
| ETHUSDT | 4 | `ret389_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8245 | 0.5376 | -1.1024 | -0.0076 | 0.1129 | ok | RAN |
| ETHUSDT | 8 | `ret389_pos_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.7799 | 0.5359 | -1.3260 | -0.0094 | 0.0994 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret389_pos_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.4889 | 0.2857 | -1.2342 | -0.0576 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret389_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.3937 | 0.2500 | -1.5052 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret389_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret389_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret389_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret389_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
