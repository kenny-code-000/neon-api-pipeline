INSERT INTO mart_event_counts_daily (day, source, event_count)
SELECT
  COALESCE(event_ts::date, ingested_at::date) AS day,
  source,
  COUNT(*) AS event_count
FROM stg_events
GROUP BY 1, 2
ON CONFLICT (day) DO NOTHING;