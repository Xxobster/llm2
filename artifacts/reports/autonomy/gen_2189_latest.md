# Autonomy public-indicator hunt gen 2189

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T110414Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret356_neg_at_h` | one_head_filter_pi_star | 163 | 13.3156 | 1.2885 | 0.6074 | 1.4780 | 0.0084 | 0.2086 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret356_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2481 | 0.6012 | 1.3669 | 0.0076 | 0.1965 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret356_pos_at_h` | one_head_filter_pi_star | 154 | 12.5572 | 1.1770 | 0.5584 | 0.8578 | 0.0032 | 0.1169 | ok | RAN |
| SOLUSDT | 4 | `ret356_pos_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.1621 | 0.5563 | 0.8123 | 0.0031 | 0.1187 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret356_neg_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9817 | 0.5598 | -0.1125 | -0.0004 | 0.1340 | ok | RAN |
| SOLUSDT | 8 | `ret356_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9810 | 0.5608 | -0.1174 | -0.0004 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret356_pos_at_h` | one_head_filter_pi_star | 185 | 15.1569 | 0.8290 | 0.5459 | -0.9980 | -0.0073 | 0.0919 | ok | RAN |
| ETHUSDT | 4 | `ret356_pos_at_h` | one_head_filter_pi_star | 201 | 16.5868 | 0.7986 | 0.5373 | -1.2651 | -0.0085 | 0.0945 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret356_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0768 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret356_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0815 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret356_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret356_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret356_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret356_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
