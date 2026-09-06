# Autonomy public-indicator hunt gen 1603

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T182556Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma688_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1868 | 0.5860 | 1.0597 | 0.0057 | 0.1774 | ok | RAN |
| ETHUSDT | 4 | `sma688_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1867 | 0.5843 | 1.0648 | 0.0055 | 0.1910 | ok | RAN |
| SOLUSDT | 8 | `sma688_above_at_h` | one_head_filter_pi_star | 110 | 9.0205 | 1.2168 | 0.5818 | 0.8996 | 0.0039 | 0.1364 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma688_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.0414 | 0.5319 | 0.2057 | 0.0008 | 0.1206 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma688_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.9102 | 0.5567 | -0.5529 | -0.0019 | 0.1443 | ok | RAN |
| SOLUSDT | 8 | `sma688_below_at_h` | one_head_filter_pi_star | 194 | 15.7823 | 0.9026 | 0.5515 | -0.6225 | -0.0021 | 0.1392 | ok | RAN |
| ETHUSDT | 4 | `sma688_above_at_h` | one_head_filter_pi_star | 142 | 11.6722 | 0.9019 | 0.5563 | -0.5161 | -0.0039 | 0.1127 | ok | RAN |
| ETHUSDT | 8 | `sma688_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 0.8923 | 0.5517 | -0.5780 | -0.0043 | 0.1103 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma688_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma688_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0675 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma688_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma688_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma688_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma688_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
