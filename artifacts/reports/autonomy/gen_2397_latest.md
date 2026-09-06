# Autonomy public-indicator hunt gen 2397

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T132934Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret386_neg_at_h` | one_head_filter_pi_star | 161 | 13.1522 | 1.2433 | 0.5963 | 1.2624 | 0.0072 | 0.1863 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret386_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 1.1804 | 0.5943 | 1.0176 | 0.0054 | 0.1657 | ok | RAN |
| SOLUSDT | 8 | `ret386_pos_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.1412 | 0.5576 | 0.7237 | 0.0026 | 0.1091 | ok | RAN |
| SOLUSDT | 4 | `ret386_pos_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.1003 | 0.5649 | 0.5020 | 0.0019 | 0.1039 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret386_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9795 | 0.5661 | -0.1264 | -0.0004 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `ret386_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 0.9326 | 0.5435 | -0.4179 | -0.0015 | 0.1522 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret386_pos_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8351 | 0.5337 | -0.9699 | -0.0069 | 0.0955 | ok | RAN |
| ETHUSDT | 4 | `ret386_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 0.7868 | 0.5282 | -1.3557 | -0.0089 | 0.1077 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret386_pos_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.4889 | 0.2857 | -1.2342 | -0.0586 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret386_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0652 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret386_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret386_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret386_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret386_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
