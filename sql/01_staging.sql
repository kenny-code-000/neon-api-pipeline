INSERT INTO stg_events (event_id, source, event_type, event_ts, ingested_at)
SELECT
  event_id,
  source,
  payload->>'type' AS event_type,
  (payload->>'timestamp')::timestamptz AS event_ts,
  ingested_at
FROM raw_events
ON CONFLICT (event_id) DO UPDATE
SET
  source = EXCLUDED.source,
  event_type = EXCLUDED.event_type,
  event_ts = EXCLUDED.event_ts,
  ingested_at = EXCLUDED.ingested_at;