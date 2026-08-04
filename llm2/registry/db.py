"""SQLite research registry."""

from __future__ import annotations

import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from llm2.paths import RESEARCH_DB, ensure_artifact_dirs


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


class ResearchDB:
    def __init__(self, path: Path | None = None) -> None:
        ensure_artifact_dirs()
        self.path = path or RESEARCH_DB
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        schema_path = Path(__file__).with_name("schema.sql")
        sql = schema_path.read_text(encoding="utf-8")
        with self._connect() as conn:
            conn.executescript(sql)
            conn.commit()

    def create_generation(
        self,
        generation_id: str,
        *,
        max_trials: int = 200,
        hypothesis: str = "",
        config_hash: str = "",
    ) -> str:
        with self._connect() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO generations "
                "(generation_id, preregistered_at, max_trials, hypothesis, config_hash) "
                "VALUES (?, ?, ?, ?, ?)",
                (generation_id, _utcnow(), max_trials, hypothesis, config_hash),
            )
            conn.commit()
        return generation_id

    def register_trial(self, generation_id: str, **fields: Any) -> str:
        trial_id = fields.pop("trial_id", str(uuid.uuid4()))
        cols = ["trial_id", "generation_id", "created_at"]
        vals: list[Any] = [trial_id, generation_id, _utcnow()]
        for k, v in fields.items():
            cols.append(k)
            vals.append(v)
        placeholders = ", ".join("?" for _ in cols)
        col_sql = ", ".join(cols)
        with self._connect() as conn:
            conn.execute(f"INSERT INTO trials ({col_sql}) VALUES ({placeholders})", vals)
            conn.commit()
        return trial_id

    def list_trials(self, generation_id: str | None = None) -> list[dict[str, Any]]:
        with self._connect() as conn:
            if generation_id:
                rows = conn.execute(
                    "SELECT * FROM trials WHERE generation_id=? ORDER BY created_at",
                    (generation_id,),
                ).fetchall()
            else:
                rows = conn.execute("SELECT * FROM trials ORDER BY created_at DESC LIMIT 500").fetchall()
        return [dict(r) for r in rows]

    def log_interaction(self, role: str, content: str, *, session_id: str = "", tags: str = "") -> str:
        iid = str(uuid.uuid4())
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO interactions (interaction_id, session_id, role, content, tags, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (iid, session_id, role, content, tags, _utcnow()),
            )
            conn.commit()
        return iid
