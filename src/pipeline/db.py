import psycopg
from psycopg.rows import dict_row
from .config import DATABASE_URL

def get_conn():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

def execute(sql: str, params=None):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
        conn.commit()

def executemany(sql: str, seq_of_params):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, seq_of_params)
        conn.commit()