"""structure_v1_no_retrace drops every last_retrace* column."""

from __future__ import annotations

import pandas as pd

from llm2.features.structure_v1 import drop_last_retrace_columns


def test_drop_last_retrace_columns_is_vectorized_and_strict():
    frame = pd.DataFrame(
        {
            "struct_dir": [1.0, -1.0],
            "last_retrace_pct": [0.5, 0.6],
            "last_retrace_pct_4h": [0.4, 0.3],
            "dist_last_sh_pct": [0.01, 0.02],
            "Last_Retrace_Pct_weird": [9.0, 8.0],
        }
    )
    out = drop_last_retrace_columns(frame)
    assert "last_retrace_pct" not in out.columns
    assert "last_retrace_pct_4h" not in out.columns
    assert "Last_Retrace_Pct_weird" not in out.columns
    assert list(out.columns) == ["struct_dir", "dist_last_sh_pct"]
