# Autonomy public-indicator hunt gen 1580

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T155141Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema984_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema984_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.2228 | 0.5966 | 0.9300 | 0.0038 | 0.1345 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema984_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0516 | 0.5546 | 0.2353 | 0.0010 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ema984_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.0265 | 0.5531 | 0.1782 | 0.0008 | 0.1504 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema984_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.9990 | 0.5600 | -0.0063 | -0.0000 | 0.1511 | ok | RAN |
| SOLUSDT | 8 | `ema984_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9984 | 0.5490 | -0.0106 | -0.0000 | 0.1294 | ok | RAN |
| ETHUSDT | 8 | `ema984_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.9979 | 0.5517 | -0.0092 | -0.0001 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `ema984_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9657 | 0.5426 | -0.2369 | -0.0007 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `ema984_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9672 | 0.5610 | -0.1491 | -0.0014 | 0.1301 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema984_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0543 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema984_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema984_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema984_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema984_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
