# Autonomy public-indicator hunt gen 2099

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T220837Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma753_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2228 | 0.5909 | 1.2567 | 0.0062 | 0.1932 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma753_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1175 | 0.5806 | 0.7019 | 0.0035 | 0.1774 | ok | RAN |
| SOLUSDT | 8 | `sma753_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0966 | 0.5504 | 0.4432 | 0.0018 | 0.1240 | ok | RAN |
| SOLUSDT | 4 | `sma753_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.0748 | 0.5504 | 0.3524 | 0.0014 | 0.1163 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma753_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9677 | 0.5519 | -0.2034 | -0.0007 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma753_below_at_h` | one_head_filter_pi_star | 211 | 17.1653 | 0.9188 | 0.5403 | -0.5220 | -0.0017 | 0.1422 | ok | RAN |
| ETHUSDT | 8 | `sma753_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 0.8611 | 0.5556 | -0.7963 | -0.0056 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma753_above_at_h` | one_head_filter_pi_star | 148 | 12.1654 | 0.8387 | 0.5676 | -0.8591 | -0.0069 | 0.1014 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma753_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma753_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma753_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma753_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma753_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma753_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
