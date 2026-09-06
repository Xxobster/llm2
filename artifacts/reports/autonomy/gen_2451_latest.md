# Autonomy public-indicator hunt gen 2451

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T194635Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma799_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.2118 | 0.5818 | 1.1484 | 0.0061 | 0.1818 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma799_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.1550 | 0.5780 | 0.8654 | 0.0045 | 0.1850 | ok | RAN |
| SOLUSDT | 8 | `sma799_above_at_h` | one_head_filter_pi_star | 133 | 10.9067 | 1.0959 | 0.5489 | 0.4549 | 0.0017 | 0.1128 | ok | RAN |
| SOLUSDT | 4 | `sma799_above_at_h` | one_head_filter_pi_star | 133 | 10.8449 | 1.0667 | 0.5414 | 0.3129 | 0.0012 | 0.1053 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma799_below_at_h` | one_head_filter_pi_star | 225 | 18.3984 | 0.9911 | 0.5556 | -0.0559 | -0.0002 | 0.1333 | ok | RAN |
| SOLUSDT | 8 | `sma799_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9661 | 0.5567 | -0.2104 | -0.0007 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma799_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 0.8593 | 0.5465 | -0.7893 | -0.0057 | 0.1047 | ok | RAN |
| ETHUSDT | 4 | `sma799_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8058 | 0.5442 | -1.0439 | -0.0089 | 0.1020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma799_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma799_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0572 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma799_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma799_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma799_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma799_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
