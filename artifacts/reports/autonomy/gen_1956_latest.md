# Autonomy public-indicator hunt gen 1956

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T044113Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1036_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.2312 | 0.6087 | 0.9226 | 0.0041 | 0.1391 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1036_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.2177 | 0.5847 | 0.9236 | 0.0037 | 0.1186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1036_below_at_h` | one_head_filter_pi_star | 239 | 19.5241 | 0.9684 | 0.5439 | -0.2235 | -0.0010 | 0.1506 | ok | RAN |
| SOLUSDT | 8 | `ema1036_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 0.9295 | 0.5376 | -0.5097 | -0.0015 | 0.1316 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1036_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9153 | 0.5341 | -0.6136 | -0.0019 | 0.1326 | ok | RAN |
| ETHUSDT | 8 | `ema1036_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9098 | 0.5385 | -0.6622 | -0.0029 | 0.1496 | ok | RAN |
| ETHUSDT | 4 | `ema1036_above_at_h` | one_head_filter_pi_star | 120 | 9.9034 | 0.8887 | 0.5583 | -0.5274 | -0.0050 | 0.1000 | ok | RAN |
| ETHUSDT | 8 | `ema1036_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.8667 | 0.5214 | -0.6395 | -0.0057 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1036_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6020 | 0.2941 | -0.7739 | -0.0340 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1036_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0577 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1036_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1036_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1036_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1036_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
