# Autonomy public-indicator hunt gen 2093

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T211438Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret342_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.2264 | 0.5899 | 1.2503 | 0.0068 | 0.2022 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret342_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.1800 | 0.5849 | 0.9359 | 0.0055 | 0.2075 | ok | RAN |
| SOLUSDT | 4 | `ret342_pos_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.2752 | 0.5909 | 1.2906 | 0.0049 | 0.1234 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret342_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.1469 | 0.5563 | 0.7155 | 0.0027 | 0.1126 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret342_neg_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9751 | 0.5672 | -0.1565 | -0.0005 | 0.1443 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret342_neg_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 0.9064 | 0.5590 | -0.6025 | -0.0020 | 0.1436 | ok | RAN |
| ETHUSDT | 8 | `ret342_pos_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7875 | 0.5484 | -1.3186 | -0.0091 | 0.1022 | ok | RAN |
| ETHUSDT | 4 | `ret342_pos_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 0.7526 | 0.5419 | -1.5177 | -0.0109 | 0.1117 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret342_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret342_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0783 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret342_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret342_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret342_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret342_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
