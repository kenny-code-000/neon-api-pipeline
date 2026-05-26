from .extract.sample_api import fetch_events
from .load.raw_loader import load_raw
from .transform.run_sql import run_all_sql

def run():
    events = fetch_events()
    load_raw(events, source="sample_api")
    run_all_sql("sql")

if __name__ == "__main__":
    run()