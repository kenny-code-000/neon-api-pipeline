CREATE TABLE IF NOT EXISTS raw_events (
  event_id        TEXT PRIMARY KEY,
  source          TEXT NOT NULL,
  payload         JSONB NOT NULL,
  ingested_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS stg_events (
  event_id        TEXT PRIMARY KEY,
  source          TEXT NOT NULL,
  event_type      TEXT,
  event_ts        TIMESTAMPTZ,
  ingested_at     TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS mart_event_counts_daily (
  day             DATE PRIMARY KEY,
  source          TEXT NOT NULL,
  event_count     BIGINT NOT NULL
);