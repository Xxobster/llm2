# Autonomy public-indicator hunt gen 1957

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T044704Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret323_neg_at_h` | one_head_filter_pi_star | 136 | 11.1100 | 1.2750 | 0.6103 | 1.3019 | 0.0080 | 0.2206 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret323_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.2293 | 0.6101 | 1.2218 | 0.0069 | 0.1887 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret323_pos_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.1340 | 0.5513 | 0.6730 | 0.0025 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `ret323_pos_at_h` | one_head_filter_pi_star | 181 | 14.8429 | 1.0763 | 0.5470 | 0.4103 | 0.0015 | 0.1050 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret323_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 0.9991 | 0.5576 | -0.0050 | -0.0000 | 0.1455 | ok | RAN |
| SOLUSDT | 4 | `ret323_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 0.9921 | 0.5556 | -0.0467 | -0.0002 | 0.1579 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret323_pos_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 0.8405 | 0.5298 | -0.9233 | -0.0069 | 0.1071 | ok | RAN |
| ETHUSDT | 4 | `ret323_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 0.7627 | 0.5341 | -1.4417 | -0.0097 | 0.1023 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret323_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0607 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret323_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0688 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret323_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret323_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret323_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret323_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
