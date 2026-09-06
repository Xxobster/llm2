# Level redesign + soft VSA (`20260812T075302Z`)

**RESEARCH_ONLY**

## Level MAE (selected)
### BTCUSDT
| key | MAE | P90 | n |
|---|---:|---:|---:|
| level_vsa_ret_point | 0.006645250324428296 | 0.014932979791227858 | 15606 |
| level_vsa_ret_q50 | 0.006303730191416913 | 0.014627300560189984 | 15606 |
| level_vsa_ret_q50_narrow | 0.0041562932087086555 | 0.009779602767211903 | 7803 |
| level_vsa_atr_resid_point | 0.006588550251031955 | 0.014919999650168703 | 15606 |
| level_vsa_atr_resid_q50 | 0.006274828098417214 | 0.01474696813733547 | 15606 |
| level_vsa_atr_resid_q50_narrow | 0.004161781526314536 | 0.009644154589324704 | 7803 |
| level_strong_ret_point | 0.006677116951533933 | 0.01508607554631157 | 15606 |
| level_strong_ret_q50 | 0.00629817579764888 | 0.014719339734511373 | 15606 |
| level_strong_ret_q50_narrow | 0.004294119250016457 | 0.010000423121463693 | 7803 |
| level_strong_atr_resid_point | 0.006606490283212974 | 0.014955623046006727 | 15606 |
| level_strong_atr_resid_q50 | 0.006271643879544254 | 0.01468154839182815 | 15606 |
| level_strong_atr_resid_q50_narrow | 0.004120953548344487 | 0.00952253433780733 | 7803 |

### ETHUSDT
| key | MAE | P90 | n |
|---|---:|---:|---:|
| level_vsa_ret_point | 0.009369732676962578 | 0.020467426948312994 | 15517 |
| level_vsa_ret_q50 | 0.008853422864807826 | 0.02023346029906864 | 15517 |
| level_vsa_ret_q50_narrow | 0.0061509143170943355 | 0.01448385878153276 | 7759 |
| level_vsa_atr_resid_point | 0.00926882414294466 | 0.020635256032956812 | 15517 |
| level_vsa_atr_resid_q50 | 0.008836849219961558 | 0.020478960846084134 | 15517 |
| level_vsa_atr_resid_q50_narrow | 0.006051873005745606 | 0.014343582667551246 | 7759 |
| level_strong_ret_point | 0.00941042894265904 | 0.02074213857008326 | 15517 |
| level_strong_ret_q50 | 0.008872761206295808 | 0.02031741358780776 | 15517 |
| level_strong_ret_q50_narrow | 0.006167871378550911 | 0.01446120303656328 | 7759 |
| level_strong_atr_resid_point | 0.009253745084500742 | 0.02036993308013541 | 15517 |
| level_strong_atr_resid_q50 | 0.008872774599051225 | 0.020431877018481436 | 15517 |
| level_strong_atr_resid_q50_narrow | 0.0061018152941636475 | 0.014491816569120332 | 7759 |

### SOLUSDT
| key | MAE | P90 | n |
|---|---:|---:|---:|
| level_vsa_ret_point | 0.012793557078404967 | 0.028145788585235584 | 14461 |
| level_vsa_ret_q50 | 0.011909056203879921 | 0.027089240382670587 | 14461 |
| level_vsa_ret_q50_narrow | 0.008367464661281413 | 0.019701142477048898 | 7231 |
| level_vsa_atr_resid_point | 0.012612240567831598 | 0.027935243456076106 | 14461 |
| level_vsa_atr_resid_q50 | 0.011808530423380306 | 0.027035997563268105 | 14461 |
| level_vsa_atr_resid_q50_narrow | 0.008200422686879101 | 0.01966883885500157 | 7231 |
| level_strong_ret_point | 0.012774714921093387 | 0.028155358547640882 | 14461 |
| level_strong_ret_q50 | 0.011914116064270886 | 0.027302199547879994 | 14461 |
| level_strong_ret_q50_narrow | 0.008349740299718793 | 0.0199525792490455 | 7231 |
| level_strong_atr_resid_point | 0.012636850014137266 | 0.028181929304674308 | 14461 |
| level_strong_atr_resid_q50 | 0.011813004286058216 | 0.027283934792038254 | 14461 |
| level_strong_atr_resid_q50_narrow | 0.008157512434260718 | 0.01959814319549311 | 7231 |

## Trade arms
### BTCUSDT (level=ret, softVSA thr=0.667)
| tag | n_gated | n_tr | WR | PF | exp_intent | entry_bar% | pnl |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTCUSDT_ctrl_p75_ret | 4088 | 876 | 0.506 | 0.831 | -0.00782 | 10.6% | -31.96 |
| BTCUSDT_ctrl_p75_softvsa_ret | 2251 | 598 | 0.503 | 0.844 | -0.00945 | 13.0% | -21.27 |
| BTCUSDT_pi_band_ret | 371 | 113 | 0.504 | 1.002 | 0.00010 | 13.3% | 0.04 |
| BTCUSDT_q50_narrow_ret | 2250 | 598 | 0.477 | 0.708 | -0.01616 | 3.3% | -36.35 |

### ETHUSDT (level=atr, softVSA thr=0.667)
| tag | n_gated | n_tr | WR | PF | exp_intent | entry_bar% | pnl |
|---|---:|---:|---:|---:|---:|---:|---:|
| ETHUSDT_ctrl_p75_atr | 1591 | 400 | 0.642 | 1.729 | 0.01456 | 30.8% | 23.17 |
| ETHUSDT_ctrl_p75_softvsa_atr | 996 | 283 | 0.654 | 1.848 | 0.01875 | 32.5% | 18.67 |
| ETHUSDT_pi_band_atr | 29 | — | — | TOO_FEW | — | — | — |
| ETHUSDT_q50_narrow_atr | 812 | 265 | 0.532 | 0.917 | -0.00261 | 12.1% | -2.12 |

### SOLUSDT (level=ret, softVSA thr=0.667)
| tag | n_gated | n_tr | WR | PF | exp_intent | entry_bar% | pnl |
|---|---:|---:|---:|---:|---:|---:|---:|
| SOLUSDT_ctrl_p75_ret | 3777 | 845 | 0.711 | 2.365 | 0.01092 | 45.4% | 41.24 |
| SOLUSDT_ctrl_p75_softvsa_ret | 1707 | 437 | 0.767 | 3.332 | 0.01640 | 54.0% | 28.00 |
| SOLUSDT_pi_band_ret | 41 | — | — | TOO_FEW | — | — | — |
| SOLUSDT_q50_narrow_ret | 2157 | 607 | 0.591 | 1.264 | 0.00358 | 23.9% | 7.73 |

## SOL TF trial
- SOLUSDT_1h_p75_ret: n=2207 PF=3.055 WR=0.774 entry_bar%=70.2