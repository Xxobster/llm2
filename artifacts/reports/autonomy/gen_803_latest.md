# Autonomy public-indicator hunt gen 803

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T155921Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma508_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0518 | 0.6935 | 4.4866 | 0.0246 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma508_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.0648 | 0.6878 | 4.5133 | 0.0241 | 0.3915 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma508_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.9449 | 0.6856 | 3.8826 | 0.0136 | 0.3402 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma508_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8204 | 0.6719 | 3.4612 | 0.0125 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma508_above_at_h` | one_head_filter_pi_star | 180 | 14.7609 | 1.6343 | 0.6167 | 2.7621 | 0.0095 | 0.2889 | ok | RAN |
| SOLUSDT | 8 | `sma508_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5935 | 0.6138 | 2.7161 | 0.0092 | 0.2751 | ok | RAN |
| ETHUSDT | 4 | `sma508_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2155 | 0.5967 | 1.1069 | 0.0078 | 0.2155 | ok | RAN |
| ETHUSDT | 8 | `sma508_above_at_h` | one_head_filter_pi_star | 159 | 13.0696 | 1.1825 | 0.6038 | 0.8951 | 0.0068 | 0.2138 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma508_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma508_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma508_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma508_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma508_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma508_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
