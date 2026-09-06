# Autonomy public-indicator hunt gen 104

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T162014Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma10_above_at_h` | one_head_filter_pi_star | 15 | 1.3351 | 8.8790 | 0.9333 | 2.6997 | 0.0729 | 0.8667 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma10_below_at_h` | one_head_filter_pi_star | 57 | 4.9880 | 2.6191 | 0.7544 | 3.2118 | 0.0404 | 0.3860 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma10_above_at_h` | one_head_filter_pi_star | 17 | 1.8144 | 2.5466 | 0.8235 | 1.9847 | 0.0219 | 0.7647 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma10_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7855 | 0.6757 | 3.7904 | 0.0203 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma10_cross_up` | one_head_filter_pi_star | 205 | 16.7466 | 1.6957 | 0.6634 | 3.1749 | 0.0189 | 0.3366 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma10_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.1810 | 0.6890 | 4.0407 | 0.0179 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma10_cross_up` | one_head_filter_pi_star | 111 | 9.0766 | 2.1300 | 0.7117 | 3.2304 | 0.0158 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma10_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `sma10_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.4093 | 0.6019 | 2.1909 | 0.0061 | 0.2500 | ok | RAN |
| SOLUSDT | 8 | `sma10_cross_down` | one_head_filter_pi_star | 193 | 15.7373 | 1.2844 | 0.5855 | 1.4895 | 0.0042 | 0.1969 | ok | RAN |
| ETHUSDT | 8 | `sma10_cross_down` | one_head_filter_pi_star | 136 | 11.2229 | 1.0818 | 0.5662 | 0.3794 | 0.0027 | 0.1618 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma10_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma10_cross_down` | one_head_filter_pi_star | 13 | 1.1063 | 0.1711 | 0.2308 | -1.8537 | -0.0705 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma10_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma10_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma10_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma10_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `sma10_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma10_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma10_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma10_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma10_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma10_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma10_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
