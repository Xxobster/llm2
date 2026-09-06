# Autonomy public-indicator hunt gen 947

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T064132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma630_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1532 | 0.6961 | 4.6531 | 0.0256 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma630_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9908 | 0.6809 | 4.2981 | 0.0232 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma630_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 1.8645 | 0.6634 | 3.6807 | 0.0130 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma630_below_at_h` | one_head_filter_pi_star | 206 | 16.7585 | 1.8164 | 0.6650 | 3.5788 | 0.0123 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma630_above_at_h` | one_head_filter_pi_star | 159 | 13.0388 | 1.5954 | 0.6164 | 2.5132 | 0.0094 | 0.3082 | ok | RAN |
| SOLUSDT | 4 | `sma630_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5787 | 0.6250 | 2.2843 | 0.0091 | 0.3264 | ok | RAN |
| ETHUSDT | 8 | `sma630_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.1154 | 0.5926 | 0.6026 | 0.0044 | 0.2160 | ok | RAN |
| ETHUSDT | 4 | `sma630_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.0924 | 0.5839 | 0.4880 | 0.0036 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma630_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma630_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma630_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma630_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
