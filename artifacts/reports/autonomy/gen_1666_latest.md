# Autonomy public-indicator hunt gen 1666

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T003649Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1520_pos_at_h` | one_head_filter_pi_star | 17 | 1.5161 | 1.3208 | 0.6471 | 0.5277 | 0.0053 | 0.1176 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1520_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0071 | 0.5493 | 0.0544 | 0.0001 | 0.1254 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1520_neg_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9755 | 0.5434 | -0.1961 | -0.0005 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1520_neg_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9401 | 0.5498 | -0.4925 | -0.0020 | 0.1390 | ok | RAN |
| ETHUSDT | 8 | `ret1520_neg_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9203 | 0.5463 | -0.6703 | -0.0027 | 0.1373 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1520_pos_at_h` | one_head_filter_pi_star | 13 | 3.9230 | 0.5685 | 0.3846 | -1.7566 | -0.0210 | 0.0769 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1520_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4101 | 0.3000 | -1.4065 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1520_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.2100 | 0.1875 | -2.0307 | -0.1031 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1520_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1520_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1520_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1520_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1520_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1520_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
