# Autonomy public-indicator hunt gen 2037

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T133058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret334_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.2356 | 0.6071 | 1.2849 | 0.0072 | 0.1964 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret334_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 1.1509 | 0.5952 | 0.8519 | 0.0045 | 0.1964 | ok | RAN |
| SOLUSDT | 8 | `ret334_pos_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.1920 | 0.5548 | 0.9520 | 0.0036 | 0.1226 | ok | RAN |
| SOLUSDT | 4 | `ret334_pos_at_h` | one_head_filter_pi_star | 155 | 12.6388 | 1.1339 | 0.5484 | 0.6655 | 0.0025 | 0.1097 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret334_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 0.9955 | 0.5607 | -0.0255 | -0.0001 | 0.1503 | ok | RAN |
| SOLUSDT | 4 | `ret334_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9954 | 0.5661 | -0.0276 | -0.0001 | 0.1376 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret334_pos_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 0.7788 | 0.5437 | -1.3107 | -0.0091 | 0.0938 | ok | RAN |
| ETHUSDT | 8 | `ret334_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.7844 | 0.5361 | -1.2517 | -0.0093 | 0.0964 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret334_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0560 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret334_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3953 | 0.2222 | -1.4772 | -0.0777 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret334_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret334_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret334_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret334_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
