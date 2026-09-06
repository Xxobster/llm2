# Autonomy public-indicator hunt gen 1950

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T040646Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma482_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1788 | 0.6022 | 1.0271 | 0.0053 | 0.1828 | ok | RAN |
| ETHUSDT | 4 | `wma482_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1185 | 0.5892 | 0.7173 | 0.0037 | 0.2054 | ok | RAN |
| SOLUSDT | 4 | `wma482_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0548 | 0.5667 | 0.3177 | 0.0011 | 0.1500 | ok | RAN |
| SOLUSDT | 4 | `wma482_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.0263 | 0.5431 | 0.1556 | 0.0005 | 0.1015 | ok | RAN |
| SOLUSDT | 8 | `wma482_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.0068 | 0.5385 | 0.0392 | 0.0001 | 0.1044 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma482_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9861 | 0.5470 | -0.0809 | -0.0003 | 0.1657 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma482_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 0.8266 | 0.5389 | -1.1264 | -0.0070 | 0.0933 | ok | RAN |
| ETHUSDT | 8 | `wma482_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 0.7992 | 0.5361 | -1.3252 | -0.0085 | 0.0928 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma482_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma482_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma482_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma482_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma482_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma482_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
