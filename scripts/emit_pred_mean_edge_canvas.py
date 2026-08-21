"""Emit canvases/pred-mean-edge-sweep.canvas.tsx with embedded sweep results."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "artifacts" / "reports" / "structure_v1_pred_mean_edge_sweep_001_canvas.json"
# Cursor IDE canvases path
CANVAS = (
    Path.home()
    / ".cursor"
    / "projects"
    / "d-projects-LLM2"
    / "canvases"
    / "pred-mean-edge-sweep.canvas.tsx"
)


def js(v) -> str:
    return json.dumps(v)


def main() -> int:
    d = json.loads(SRC.read_text(encoding="utf-8"))
    edges = d["edges"]
    cats = [str(e) for e in edges]

    # Live-direction curve series (skip BTC return packs)
    live_series_ids = [
        ("eth_multitrade_v1_2", "ETH multitrade v1.2 LIVE"),
        ("eth_k5_double3h_v1", "ETH K5 double LIVE"),
        ("sol_k5_double3h_v1", "SOL K5 double LIVE"),
        ("structure_v1_lgbm_ETHUSDT_1h_direction", "ETH single LIVE"),
        ("structure_v1_lgbm_SOLUSDT_1h_direction", "SOL single LIVE"),
    ]
    series = []
    for vid, name in live_series_ids:
        data = []
        for e in edges:
            hit = next(
                (
                    r
                    for r in d["all_rows"]
                    if r["version_id"] == vid and abs((r["edge"] or -1) - e) < 1e-9
                ),
                None,
            )
            data.append(
                round(hit["eru_pct"], 4)
                if hit and hit.get("eru_pct") is not None
                else 0.0
            )
        series.append({"name": name, "data": data})

    # All pack × edge matrix table rows (n>=1)
    table_all = []
    for r in sorted(
        d["all_rows"],
        key=lambda x: (
            0 if x["live"] else 1,
            x["version_id"] or "",
            x["edge"] or 0,
        ),
    ):
        if not r.get("n"):
            # keep zero-n with dash for return packs visibility
            if r.get("target") != "fwd_return":
                continue
        table_all.append(
            {
                "pack": (r["version_id"] or "")[:48],
                "sym": r["symbol"],
                "tgt": r["target"],
                "live": "LIVE" if r["live"] else "frozen",
                "acct": r.get("account") or "—",
                "edge": r["edge"],
                "n": r["n"],
                "eru": None
                if r.get("eru_pct") is None
                else round(r["eru_pct"], 4),
                "pf": None if r.get("pf") is None else round(r["pf"], 3),
                "wr": None if r.get("wr") is None else round(100 * r["wr"], 1),
                "pnl": None if r.get("net_pnl") is None else round(r["net_pnl"], 2),
            }
        )

    # Robust best: n>=200
    robust = sorted(
        [
            r
            for r in d["all_rows"]
            if (r.get("n") or 0) >= 200 and r.get("eru_pct") is not None
        ],
        key=lambda r: r["eru_pct"],
        reverse=True,
    )[:15]
    top_eru = d["top_eru"][:12]
    live_default = d["live_at_edge_0_10"]

    # Bar chart top robust
    bar_cats = [
        f"{r['version_id'][:22]}@{r['edge']}"
        + (" *" if r["live"] else "")
        for r in robust[:12]
    ]
    bar_vals = [round(r["eru_pct"], 4) for r in robust[:12]]

    content = f'''import {{
  BarChart,
  Callout,
  Card,
  CardBody,
  CardHeader,
  Divider,
  Grid,
  H1,
  H2,
  LineChart,
  Pill,
  Row,
  Spacer,
  Stack,
  Stat,
  Table,
  Text,
}} from "cursor/canvas";

/**
 * pred_mean absolute edge sweep — all live_packs geometries.
 * Source: structure_v1_pred_mean_edge_sweep_001
 * Outer folds v2 · hard end < 2026-05-01 · RESEARCH_ONLY diagnostic
 * Gate: long if pred_mean > edge, short if pred_mean < -edge
 */

const EDGES = {js(cats)};

const LIVE_ERU_SERIES = {js(series)};

const BAR_TOP_ROBUST = {{
  categories: {js(bar_cats)},
  values: {js(bar_vals)},
}};

const LIVE_AT_010 = {js([
    {
        "version_id": r["version_id"],
        "account": r.get("account"),
        "service": r.get("service"),
        "edge": r["edge"],
        "n": r["n"],
        "eru_pct": None if r.get("eru_pct") is None else round(r["eru_pct"], 4),
        "pf": None if r.get("pf") is None else round(r["pf"], 3),
        "target": r["target"],
    }
    for r in live_default
])};

const TOP_ERU = {js([
    {
        "pack": (r["version_id"] or "")[:40],
        "live": r["live"],
        "edge": r["edge"],
        "n": r["n"],
        "eru_pct": round(r["eru_pct"], 4) if r.get("eru_pct") is not None else None,
        "pf": None if r.get("pf") is None else round(r["pf"], 2),
    }
    for r in top_eru
])};

const ROBUST = {js([
    {
        "pack": (r["version_id"] or "")[:40],
        "live": r["live"],
        "edge": r["edge"],
        "n": r["n"],
        "eru_pct": round(r["eru_pct"], 4),
        "pf": None if r.get("pf") is None else round(r["pf"], 2),
        "wr": None if r.get("wr") is None else round(100 * r["wr"], 1),
    }
    for r in robust
])};

const ALL_ROWS = {js(table_all)};

export default function PredMeanEdgeSweep() {{
  const bestRobust = ROBUST[0];
  const liveMt = LIVE_AT_010.find((r) => String(r.version_id).includes("multitrade_v1_2"));
  const liveK5 = LIVE_AT_010.find((r) => String(r.version_id).includes("eth_k5"));

  return (
    <Stack gap={{20}} style={{{{ padding: 20, maxWidth: 1200 }}}}>
      <Stack gap={{6}}>
        <H1>pred_mean edge sweep — all strategies</H1>
        <Text tone="secondary" size="small">
          Outer fold geometry v2 · hard end exclusive 2026-05-01 · lockbox unused ·
          MIN_EXCHANGE · tradesim botsgeneral. Evidence class: MEASURE_DIAGNOSTIC
          (not a promotion certificate). Side rule: long if pred_mean &gt; edge,
          short if pred_mean &lt; −edge.
        </Text>
        <Row gap={{8}} style={{{{ flexWrap: "wrap" }}}}>
          <Pill tone="info" size="sm">22 packs × 9 edges</Pill>
          <Pill tone="neutral" size="sm">edges 0.10…0.90</Pill>
          <Pill tone="warning" size="sm">RESEARCH_ONLY</Pill>
        </Row>
      </Stack>

      <Callout tone="warning" title="Live vs grid">
        Direction packs live at min_edge = 0.10 today. BTC single + BTC K5 use
        target = forward return with live edge ≈ 0.0016 — absolute edges 0.10–0.90
        produce zero trades (return score ≠ direction score units). Higher edges
        raise per-trade Expectancy (return units) but shrink sample; n &lt; 50
        cells are not deployment evidence. Picking the outer-OOS champion edge
        is exploratory — freeze a single prereg before any promotion.
      </Callout>

      <Grid columns={{3}} gap={{12}}>
        <Stat
          label="Best robust E[r] (n≥200)"
          value={{bestRobust ? `${{bestRobust.eru_pct.toFixed(3)}}%` : "—"}}
          tone="success"
        />
        <Stat
          label="ETH MT v1.2 live @0.10"
          value={{liveMt?.eru_pct != null ? `${{liveMt.eru_pct.toFixed(3)}}%` : "—"}}
        />
        <Stat
          label="ETH K5 live @0.10"
          value={{liveK5?.eru_pct != null ? `${{liveK5.eru_pct.toFixed(3)}}%` : "—"}}
        />
      </Grid>

      <Card>
        <CardHeader title="Live direction packs — Expectancy (return units) % vs pred_mean edge" />
        <CardBody>
          <LineChart
            categories={{EDGES}}
            series={{LIVE_ERU_SERIES}}
            height={{280}}
            beginAtZero={{true}}
          />
          <Text tone="secondary" size="small">
            Y-axis: stitched outer-fold expectancy_return_units × 100 (percent).
            X-axis: absolute |pred_mean| entry threshold. Source: structure_v1_pred_mean_edge_sweep_001.
          </Text>
        </CardBody>
      </Card>

      <Card>
        <CardHeader title="Top expectancy by pack@edge (require n ≥ 200 trades)" />
        <CardBody>
          <BarChart
            categories={{BAR_TOP_ROBUST.categories}}
            series={{[{{ name: "E[r] %", data: BAR_TOP_ROBUST.values, tone: "info" }}]}}
            height={{300}}
            horizontal
          />
          <Text tone="secondary" size="small">
            * marks live packs. Filters out n&lt;200 sparse arms that inflate E[r]/PF.
          </Text>
        </CardBody>
      </Card>

      <H2>Live units (at edge 0.10 where applicable)</H2>
      <Table
        headers={{["Status", "Account", "Version", "Target", "Edge", "n", "E[r] %", "PF"]}}
        rows={{LIVE_AT_010.map((r) => [
          "LIVE",
          r.account || "—",
          String(r.version_id).slice(0, 36),
          r.target,
          r.edge,
          r.n,
          r.eru_pct == null ? "0 trades" : r.eru_pct.toFixed(3),
          r.pf == null ? "—" : r.pf.toFixed(2),
        ])}}
      />

      <H2>Best cells by E[r] (any sample size)</H2>
      <Table
        headers={{["Live?", "Pack", "Edge", "n", "E[r] %", "PF"]}}
        rows={{TOP_ERU.map((r) => [
          r.live ? "LIVE" : "frozen",
          r.pack,
          r.edge,
          r.n,
          r.eru_pct == null ? "—" : r.eru_pct.toFixed(3),
          r.pf == null ? "∞/—" : String(r.pf),
        ])}}
      />

      <H2>Robust ranking (n ≥ 200)</H2>
      <Table
        headers={{["Live?", "Pack", "Edge", "n", "E[r] %", "PF", "WR %"]}}
        rows={{ROBUST.map((r) => [
          r.live ? "LIVE" : "frozen",
          r.pack,
          r.edge,
          r.n,
          r.eru_pct.toFixed(3),
          r.pf == null ? "—" : String(r.pf),
          r.wr == null ? "—" : String(r.wr),
        ])}}
      />

      <Divider />
      <H2>Full metrics grid — all packs × edges (with trades, + BTC zero cells)</H2>
      <Text tone="secondary" size="small">
        {len(table_all)} rows · E[r] % = expectancy_return_units×100 · PF = profit
        factor · WR = win rate % · PnL = stitched net (MIN_EXCHANGE dust units)
      </Text>
      <Table
        headers={{["Live", "Acct", "Pack", "Sym", "Tgt", "Edge", "n", "E[r]%", "PF", "WR%", "PnL"]}}
        rows={{ALL_ROWS.map((r) => [
          r.live,
          r.acct,
          r.pack,
          r.sym,
          r.tgt,
          r.edge,
          r.n,
          r.eru == null ? "—" : r.eru.toFixed(3),
          r.pf == null ? "—" : String(r.pf),
          r.wr == null ? "—" : String(r.wr),
          r.pnl == null ? "—" : String(r.pnl),
        ])}}
      />

      <Spacer height={{8}} />
      <Text tone="secondary" size="small">
        Report JSON: artifacts/reports/structure_v1_pred_mean_edge_sweep_001_latest.json ·
        CSV: …_all_cells.csv · generation {d.get("generation_id")}
      </Text>
    </Stack>
  );
}}
'''
    CANVAS.parent.mkdir(parents=True, exist_ok=True)
    CANVAS.write_text(content, encoding="utf-8")
    print("wrote", CANVAS, "bytes", CANVAS.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
