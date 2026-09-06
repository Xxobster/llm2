# Autonomy public-indicator hunt gen 1812

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T153001Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1017_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1017_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.3269 | 0.6330 | 1.2606 | 0.0054 | 0.1193 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1017_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1568 | 0.6000 | 0.6700 | 0.0029 | 0.1417 | ok | RAN |
| ETHUSDT | 4 | `ema1017_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.0143 | 0.5556 | 0.0942 | 0.0004 | 0.1511 | ok | RAN |
| SOLUSDT | 8 | `ema1017_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 1.0110 | 0.5494 | 0.0749 | 0.0002 | 0.1304 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1017_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 1.0029 | 0.5496 | 0.0188 | 0.0001 | 0.1157 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1017_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.9603 | 0.5652 | -0.1928 | -0.0017 | 0.1232 | ok | RAN |
| ETHUSDT | 8 | `ema1017_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 0.8825 | 0.5333 | -0.8557 | -0.0038 | 0.1511 | ok | RAN |
| ETHUSDT | 4 | `ema1017_above_at_h` | one_head_filter_pi_star | 133 | 10.9763 | 0.8957 | 0.5489 | -0.5276 | -0.0045 | 0.1203 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1017_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1017_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1017_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1017_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1017_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
