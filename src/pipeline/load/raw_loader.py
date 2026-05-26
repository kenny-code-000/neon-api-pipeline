import json
from ..db import executemany

# UPSERT_RAW = """
# INSERT INTO raw_events (event_id, source, payload)
# VALUES (%s, %s, %s::jsonb)
# ON CONFLICT (