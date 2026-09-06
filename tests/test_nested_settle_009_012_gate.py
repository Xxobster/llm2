from scripts.run_ml_lab_nested_settle_009_012_screen import _arm_id, gate_verdict

GATES = {
    "min_eligible_folds": 5,
    "min_pooled_oos_trades": 50,
    "min_pooled_profit_factor": 1.20,
    "min_sharpe_annualised": 1.00,
    "min_sharpe_hac_annualised": 0.75,
    "min_fraction_positive_folds": 0.80,
    "max_entry_bar_exit_rate": 0.25,
}


def test_arm_id_fold():
    spec = {"symbol": "BTCUSDT", "timeframe": "1h", "idea": "quad_slope_follow"}
    assert _arm_id(spec, "stitched") == "BTCUSDT|1h|quad_slope_follow|stitched"
    assert _arm_id(spec, "fold", 2) == "BTCUSDT|1h|quad_slope_follow|fold|fold2"


def test_gate_pass_and_fail():
    ok, fails = gate_verdict(
        {
            "n_trades": 200,
            "profit_factor": 1.40,
            "sharpe_annualised": 1.10,
            "sharpe_hac_annualised": 0.90,
            "entry_bar_exit_rate": 0.10,
            "n_folds_ran": 6,
            "n_folds_positive": 5,
        },
        GATES,
    )
    assert ok and not fails
    bad, why = gate_verdict(
        {
            "n_trades": 20,
            "profit_factor": 0.90,
            "sharpe_annualised": -0.4,
            "sharpe_hac_annualised": -0.3,
            "entry_bar_exit_rate": 0.30,
            "n_folds_ran": 6,
            "n_folds_positive": 2,
        },
        GATES,
    )
    assert not bad
    assert any("pf<" in x for x in why)
    assert any("entry_bar>" in x for x in why)
