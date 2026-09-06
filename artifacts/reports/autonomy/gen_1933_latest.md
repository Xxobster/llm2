# Autonomy public-indicator hunt gen 1933

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T023317Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret319_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 1.2594 | 0.6139 | 1.3718 | 0.0078 | 0.2025 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret319_neg_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.2505 | 0.6163 | 1.3385 | 0.0071 | 0.1919 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret319_pos_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.2618 | 0.5625 | 1.1929 | 0.0047 | 0.1181 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret319_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.1533 | 0.5523 | 0.7733 | 0.0027 | 0.1047 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ret319_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 0.9713 | 0.5488 | -0.1670 | -0.0006 | 0.1524 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ret319_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 0.9193 | 0.5464 | -0.5083 | -0.0018 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret319_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 0.8140 | 0.5340 | -1.1511 | -0.0077 | 0.0995 | ok | RAN |
| ETHUSDT | 8 | `ret319_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.7900 | 0.5326 | -1.3235 | -0.0090 | 0.0924 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret319_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4058 | 0.2222 | -1.4199 | -0.0729 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret319_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0754 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret319_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret319_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret319_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret319_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
