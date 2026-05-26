from pathlib import Path
from ..db import execute

def run_all_sql(sql_dir: str = "sql"):
    paths = sorted(Path(sql_dir).glob("*.sql"))
    for p in paths:
        execute(p.read_text(encoding="utf-8"))