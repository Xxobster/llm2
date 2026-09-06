# Autonomy public-indicator hunt gen 1965

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T053053Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret324_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.2354 | 0.6025 | 1.2642 | 0.0071 | 0.2112 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret324_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.1467 | 0.5987 | 0.8065 | 0.0045 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `ret324_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.1557 | 0.5575 | 0.7885 | 0.0028 | 0.1034 | ok | RAN |
| SOLUSDT | 8 | `ret324_pos_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.1567 | 0.5556 | 0.7631 | 0.0028 | 0.1042 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret324_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9569 | 0.5469 | -0.2674 | -0.0009 | 0.1458 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret324_neg_at_h` | one_head_filter_pi_star | 182 | 14.8061 | 0.9191 | 0.5440 | -0.5086 | -0.0018 | 0.1538 | ok | RAN |
| ETHUSDT | 8 | `ret324_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 0.8536 | 0.5434 | -0.8697 | -0.0064 | 0.1040 | ok | RAN |
| ETHUSDT | 4 | `ret324_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.7629 | 0.5351 | -1.4992 | -0.0099 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret324_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0620 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret324_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0744 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret324_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret324_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret324_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret324_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
