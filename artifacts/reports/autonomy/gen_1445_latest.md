# Autonomy public-indicator hunt gen 1445

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T205910Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret250_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.1891 | 0.7069 | 4.6123 | 0.0269 | 0.3851 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret250_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0202 | 0.6944 | 4.3631 | 0.0245 | 0.3722 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret250_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8353 | 0.6458 | 3.6462 | 0.0128 | 0.3490 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret250_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.7090 | 0.6389 | 3.1431 | 0.0112 | 0.3389 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret250_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5033 | 0.6178 | 2.3692 | 0.0079 | 0.2775 | ok | RAN |
| ETHUSDT | 4 | `ret250_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1906 | 0.5979 | 1.0067 | 0.0066 | 0.2371 | ok | RAN |
| SOLUSDT | 8 | `ret250_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.4170 | 0.6034 | 1.9227 | 0.0065 | 0.2874 | ok | RAN |
| ETHUSDT | 8 | `ret250_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1569 | 0.5888 | 0.8467 | 0.0056 | 0.2284 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret250_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0404 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret250_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret250_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret250_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret250_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret250_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
