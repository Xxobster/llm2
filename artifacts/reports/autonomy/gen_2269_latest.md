# Autonomy public-indicator hunt gen 2269

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T205755Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret367_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 1.0944 | 0.5786 | 0.5228 | 0.0029 | 0.1887 | ok | RAN |
| ETHUSDT | 8 | `ret367_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.0558 | 0.5604 | 0.3381 | 0.0018 | 0.1868 | ok | RAN |
| SOLUSDT | 8 | `ret367_pos_at_h` | one_head_filter_pi_star | 156 | 12.7203 | 1.0869 | 0.5449 | 0.4429 | 0.0017 | 0.1154 | ok | RAN |
| SOLUSDT | 4 | `ret367_pos_at_h` | one_head_filter_pi_star | 162 | 13.2095 | 1.0558 | 0.5370 | 0.2944 | 0.0011 | 0.1049 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret367_neg_at_h` | one_head_filter_pi_star | 199 | 16.2724 | 0.9800 | 0.5628 | -0.1239 | -0.0004 | 0.1407 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret367_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9083 | 0.5500 | -0.5646 | -0.0020 | 0.1500 | ok | RAN |
| ETHUSDT | 8 | `ret367_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.7967 | 0.5397 | -1.2668 | -0.0086 | 0.1058 | ok | RAN |
| ETHUSDT | 4 | `ret367_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.7982 | 0.5337 | -1.2278 | -0.0088 | 0.0933 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret367_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret367_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret367_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret367_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret367_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret367_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
