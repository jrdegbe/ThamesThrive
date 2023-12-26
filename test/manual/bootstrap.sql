CREATE DATABASE IF NOT EXISTS ThamesThrive;
CREATE TABLE ThamesThrive.event
(
    id UUID,
    type LowCardinality(String),
    timestamp DateTime,
    properties Float32
)
ENGINE = MergeTree()
PRIMARY KEY (user_id, timestamp)
