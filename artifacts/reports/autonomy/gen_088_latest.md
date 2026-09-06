# Autonomy public-indicator hunt gen 088

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T151757Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `pflag_any` | one_head_filter_pi_star | 23 | 1.9276 | 2.5372 | 0.6522 | 1.9181 | 0.0238 | 0.3478 | TPM<MIN | RAN |
| ETHUSDT | 8 | `pquiet_all` | one_head_filter_pi_star | 376 | 30.5883 | 1.6127 | 0.6489 | 3.9529 | 0.0166 | 0.3005 | GATE_CAND | RAN |
| ETHUSDT | 4 | `pquiet_all` | one_head_filter_pi_star | 382 | 31.0765 | 1.5807 | 0.6466 | 3.7966 | 0.0160 | 0.3037 | GATE_CAND | RAN |
| ETHUSDT | 4 | `pquiet_at_h` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `pquiet_at_h` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `pquiet_all` | one_head_filter_pi_star | 356 | 28.9613 | 1.8073 | 0.6545 | 4.6075 | 0.0113 | 0.3146 | GATE_CAND | RAN |
| SOLUSDT | 4 | `pquiet_at_h` | one_head_filter_pi_star | 381 | 30.9951 | 1.7170 | 0.6404 | 4.4876 | 0.0105 | 0.3176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `pquiet_at_h` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `pquiet_all` | one_head_filter_pi_star | 364 | 29.6121 | 1.6672 | 0.6401 | 4.2096 | 0.0099 | 0.3159 | GATE_CAND | RAN |
| BTCUSDT | 4 | `pquiet_all` | one_head_filter_pi_star | 26 | 2.5067 | 1.0782 | 0.4615 | 0.1712 | 0.0070 | 0.1538 | TPM<MIN | RAN |
| BTCUSDT | 4 | `pquiet_at_h` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `pquiet_at_h` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `pflag_any` | one_head_filter_pi_star | 23 | 2.1288 | 0.8880 | 0.4348 | -0.0049 | -0.0034 | 0.3043 | TPM<MIN | RAN |
| BTCUSDT | 8 | `pquiet_all` | one_head_filter_pi_star | 23 | 2.2174 | 0.9027 | 0.4348 | -0.2183 | -0.0091 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 4 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `pflag_any` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `pflag_any` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `pflag_any` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pflag_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pflag_any` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
