# Autonomy public-indicator hunt gen 2097

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T214511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4800_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.6613 | 0.6458 | 1.3238 | 0.0094 | 0.0833 | ok | RAN |
| SOLUSDT | 8 | `ema4800_above_at_h` | one_head_filter_pi_star | 46 | 3.7815 | 1.4942 | 0.6304 | 0.9916 | 0.0078 | 0.1087 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4800_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9945 | 0.5409 | -0.0420 | -0.0001 | 0.1289 | ok | RAN |
| SOLUSDT | 8 | `ema4800_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9901 | 0.5390 | -0.0741 | -0.0002 | 0.1331 | ok | RAN |
| ETHUSDT | 8 | `ema4800_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9800 | 0.5594 | -0.1613 | -0.0007 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ema4800_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 0.9716 | 0.5591 | -0.2317 | -0.0009 | 0.1354 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4800_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.8867 | 0.5143 | -0.5456 | -0.0060 | 0.1714 | ok | RAN |
| ETHUSDT | 4 | `ema4800_above_at_h` | one_head_filter_pi_star | 40 | 4.7004 | 0.8501 | 0.5250 | -0.5015 | -0.0071 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema4800_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0527 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema4800_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4800_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4800_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4800_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
