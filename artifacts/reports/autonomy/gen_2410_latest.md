# Autonomy public-indicator hunt gen 2410

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T150040Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret2264_pos_at_h` | one_head_filter_pi_star | 14 | 1.3941 | 2.2378 | 0.6429 | 1.2721 | 0.0148 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret2264_pos_at_h` | one_head_filter_pi_star | 24 | 2.3899 | 1.1871 | 0.5417 | 0.3574 | 0.0029 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret2264_neg_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 1.0114 | 0.5452 | 0.0918 | 0.0002 | 0.1299 | ok | RAN |
| SOLUSDT | 4 | `ret2264_neg_at_h` | one_head_filter_pi_star | 340 | 27.8021 | 1.0060 | 0.5471 | 0.0477 | 0.0001 | 0.1294 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ret2264_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9781 | 0.5529 | -0.1816 | -0.0007 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret2264_neg_at_h` | one_head_filter_pi_star | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret2264_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6686 | 0.3529 | -0.6902 | -0.0396 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret2264_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5855 | 0.3125 | -0.8513 | -0.0463 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret2264_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2264_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2264_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret2264_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret2264_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
