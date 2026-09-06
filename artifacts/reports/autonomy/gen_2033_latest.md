# Autonomy public-indicator hunt gen 2033

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T130254Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4640_above_at_h` | one_head_filter_pi_star | 55 | 4.5213 | 1.8126 | 0.6545 | 1.6754 | 0.0111 | 0.0909 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4640_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.4252 | 0.6094 | 1.1131 | 0.0071 | 0.1250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema4640_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9858 | 0.5598 | -0.1134 | -0.0005 | 0.1341 | ok | RAN |
| SOLUSDT | 8 | `ema4640_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9751 | 0.5354 | -0.1953 | -0.0005 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `ema4640_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9633 | 0.5565 | -0.3048 | -0.0012 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `ema4640_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 0.9312 | 0.5249 | -0.5314 | -0.0015 | 0.1329 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4640_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9122 | 0.5294 | -0.4099 | -0.0043 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema4640_above_at_h` | one_head_filter_pi_star | 40 | 11.6752 | 0.8061 | 0.5000 | -1.1558 | -0.0100 | 0.2000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4640_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4640_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
