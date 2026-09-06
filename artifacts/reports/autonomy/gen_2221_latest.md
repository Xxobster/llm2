# Autonomy public-indicator hunt gen 2221

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T151403Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret361_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 1.2876 | 0.6037 | 1.4758 | 0.0085 | 0.2073 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret361_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 1.2084 | 0.5855 | 1.0622 | 0.0061 | 0.2105 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret361_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.1577 | 0.5581 | 0.8142 | 0.0029 | 0.1105 | ok | RAN |
| SOLUSDT | 8 | `ret361_pos_at_h` | one_head_filter_pi_star | 151 | 12.3827 | 1.1322 | 0.5695 | 0.6658 | 0.0026 | 0.1258 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret361_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 0.9379 | 0.5632 | -0.3915 | -0.0013 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ret361_neg_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 0.8647 | 0.5361 | -0.8711 | -0.0031 | 0.1495 | ok | RAN |
| ETHUSDT | 8 | `ret361_pos_at_h` | one_head_filter_pi_star | 198 | 16.2220 | 0.8077 | 0.5404 | -1.2074 | -0.0079 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `ret361_pos_at_h` | one_head_filter_pi_star | 194 | 15.8942 | 0.7898 | 0.5309 | -1.2950 | -0.0091 | 0.0979 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret361_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5979 | 0.2778 | -0.7871 | -0.0333 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret361_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.3886 | 0.2105 | -1.5181 | -0.0726 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret361_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret361_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret361_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret361_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
