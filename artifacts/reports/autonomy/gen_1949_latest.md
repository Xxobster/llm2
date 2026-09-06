# Autonomy public-indicator hunt gen 1949

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T040112Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret322_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 1.2009 | 0.6023 | 1.1182 | 0.0061 | 0.1988 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret322_pos_at_h` | one_head_filter_pi_star | 153 | 12.4757 | 1.2398 | 0.5621 | 1.1383 | 0.0043 | 0.1046 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret322_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 1.1070 | 0.5769 | 0.5956 | 0.0034 | 0.2115 | ok | RAN |
| SOLUSDT | 4 | `ret322_pos_at_h` | one_head_filter_pi_star | 172 | 14.1048 | 1.1421 | 0.5581 | 0.7362 | 0.0026 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret322_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 0.9781 | 0.5569 | -0.1284 | -0.0005 | 0.1557 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret322_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 0.8976 | 0.5329 | -0.6171 | -0.0023 | 0.1579 | ok | RAN |
| ETHUSDT | 8 | `ret322_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 0.8641 | 0.5491 | -0.8004 | -0.0055 | 0.1040 | ok | RAN |
| ETHUSDT | 4 | `ret322_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7256 | 0.5238 | -1.7922 | -0.0117 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret322_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0607 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret322_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret322_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret322_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret322_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret322_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
