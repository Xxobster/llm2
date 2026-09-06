# Autonomy public-indicator hunt gen 1821

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T161837Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret303_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2415 | 0.6121 | 1.3035 | 0.0073 | 0.1939 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret303_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1830 | 0.6012 | 1.0326 | 0.0055 | 0.1850 | ok | RAN |
| SOLUSDT | 4 | `ret303_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.0850 | 0.5673 | 0.4803 | 0.0018 | 0.1462 | ok | RAN |
| SOLUSDT | 4 | `ret303_pos_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.0608 | 0.5347 | 0.2989 | 0.0012 | 0.1181 | ok | RAN |
| SOLUSDT | 8 | `ret303_pos_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.0557 | 0.5443 | 0.2927 | 0.0011 | 0.1139 | ok | RAN |
| SOLUSDT | 8 | `ret303_neg_at_h` | one_head_filter_pi_star | 165 | 13.5815 | 1.0239 | 0.5576 | 0.1335 | 0.0005 | 0.1636 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret303_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8037 | 0.5351 | -1.2223 | -0.0080 | 0.0973 | ok | RAN |
| ETHUSDT | 4 | `ret303_pos_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 0.8049 | 0.5421 | -1.2786 | -0.0082 | 0.1053 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret303_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4163 | 0.2353 | -1.3618 | -0.0742 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret303_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3982 | 0.2222 | -1.4603 | -0.0752 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret303_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret303_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret303_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret303_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
