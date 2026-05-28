CREATE TABLE IF NOT EXISTS batteries (
    battery_id TEXT PRIMARY KEY,
    test_type TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    battery_id TEXT,
    timestamp TEXT,
    voltage REAL,
    current REAL,
    temperature REAL,
    capacity REAL,
    retention_rate REAL,
    cycle_number INTEGER,
    duration_minutes INTEGER,
    duration_category TEXT,
    hour INTEGER,
    day_of_week TEXT,
    FOREIGN KEY (battery_id) REFERENCES batteries(battery_id)
);
