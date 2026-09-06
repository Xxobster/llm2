# Autonomy public-indicator hunt gen 1661

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T001046Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret281_neg_at_h` | one_head_filter_pi_star | 149 | 12.1719 | 1.2186 | 0.6040 | 1.1391 | 0.0066 | 0.1946 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret281_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.1482 | 0.5823 | 0.8394 | 0.0045 | 0.1899 | ok | RAN |
| SOLUSDT | 8 | `ret281_pos_at_h` | one_head_filter_pi_star | 173 | 14.1065 | 1.0927 | 0.5549 | 0.4898 | 0.0016 | 0.1156 | ok | RAN |
| SOLUSDT | 4 | `ret281_pos_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.0568 | 0.5562 | 0.2981 | 0.0010 | 0.1065 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret281_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 0.9964 | 0.5515 | -0.0204 | -0.0001 | 0.1455 | ok | RAN |
| SOLUSDT | 8 | `ret281_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 0.9535 | 0.5562 | -0.2738 | -0.0010 | 0.1461 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ret281_pos_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8375 | 0.5410 | -0.9851 | -0.0065 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `ret281_pos_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 0.8044 | 0.5367 | -1.2236 | -0.0080 | 0.1017 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret281_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4364 | 0.3000 | -1.3199 | -0.0664 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret281_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4385 | 0.3158 | -1.3087 | -0.0672 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret281_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret281_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret281_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret281_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
