# Autonomy public-indicator hunt gen 067

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T135718Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema21_cross_up` | one_head_filter_pi_star | 27 | 2.3023 | 1.5916 | 0.6296 | 1.0592 | 0.0219 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema21_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 1.8239 | 0.6816 | 4.0067 | 0.0212 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema21_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.8214 | 0.6786 | 3.9995 | 0.0210 | 0.3705 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema21_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1901 | 0.6933 | 4.0585 | 0.0180 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema21_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1832 | 0.6890 | 4.0479 | 0.0180 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema21_cross_down` | one_head_filter_pi_star | 29 | 2.4555 | 3.0710 | 0.7241 | 2.2786 | 0.0173 | 0.1379 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema21_cross_down` | one_head_filter_pi_star | 20 | 2.4112 | 1.7097 | 0.5500 | 1.2650 | 0.0170 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema21_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0065 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `ema21_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1912 | 0.5938 | 0.8871 | 0.0061 | 0.2062 | ok | RAN |
| SOLUSDT | 8 | `ema21_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3631 | 0.5953 | 1.9695 | 0.0054 | 0.2372 | ok | RAN |
| SOLUSDT | 4 | `ema21_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3637 | 0.5972 | 1.9722 | 0.0053 | 0.2361 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema21_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema21_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema21_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema21_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema21_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema21_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ema21_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema21_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema21_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema21_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema21_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema21_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema21_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
