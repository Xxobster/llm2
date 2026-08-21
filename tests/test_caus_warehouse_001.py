"""CAUS-WAREHOUSE-001 — leakage engine must catch warehouse-backed builders.

A missing binding of this identifier must fail the build exactly like a failing test.
"""

from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

LEAKAGE_SRC = Path(r"C:\projects\botsgeneral\packages\leakage\src")
LEAKAGE_TESTS = Path(r"C:\projects\botsgeneral\packages\leakage\tests")
CONFORMANCE_ID = "CAUS-WAREHOUSE-001"


@pytest.mark.conformance(CONFORMANCE_ID)
def test_caus_warehouse_001_binding_exists():
    """Discoverable pytest.mark.conformance binding (parity with tradesim style)."""
    text = (LEAKAGE_TESTS / "test_builder_responsiveness.py").read_text(encoding="utf-8")
    tree = ast.parse(text)
    found = False
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for dec in node.decorator_list:
            if (
                isinstance(dec, ast.Call)
                and isinstance(dec.func, ast.Attribute)
                and dec.func.attr == "conformance"
                and dec.args
                and isinstance(dec.args[0], ast.Constant)
                and dec.args[0].value == CONFORMANCE_ID
            ):
                found = True
    assert found, f"no pytest.mark.conformance('{CONFORMANCE_ID}') binding found"


@pytest.mark.conformance(CONFORMANCE_ID)
def test_warehouse_join_builder_is_caught_by_responsiveness_probe():
    import sys

    if str(LEAKAGE_SRC) not in sys.path:
        sys.path.insert(0, str(LEAKAGE_SRC))
    from leakage.ensure_source import prefer_botsgeneral_leakage

    prefer_botsgeneral_leakage()
    from leakage.checks import check_builder_responsiveness
    from leakage.types import CheckId

    n = 800
    rng = np.random.default_rng(0)
    close = 100 * np.exp(np.cumsum(rng.normal(0, 0.01, size=n)))
    idx = pd.date_range("2020-01-01", periods=n, freq="h", tz="UTC")
    ohlcv = pd.DataFrame(
        {
            "open": close,
            "high": close * 1.001,
            "low": close * 0.999,
            "close": close,
            "volume": 1.0,
        },
        index=idx,
    )

    def warehouse_join(ohlcv_in: pd.DataFrame, *, interval: str = "1h") -> pd.DataFrame:
        _ = interval
        # Classic false-PASS pattern: ignore prices, key only by index position.
        pos = np.arange(len(ohlcv_in), dtype=float)
        return pd.DataFrame(
            {"last_retrace_pct": np.sin(pos / 17.0), "struct_dir": np.sign(np.sin(pos / 31.0))},
            index=ohlcv_in.index,
        )

    findings = check_builder_responsiveness(ohlcv, warehouse_join, compare_rows=40)
    assert findings, "warehouse join must hard-fail responsiveness"
    assert any(f.check is CheckId.BUILDER_RESPONSIVENESS for f in findings)
    assert any(f.detail.get("code") == "EXTERNAL_CACHE_SUSPECTED" for f in findings)
