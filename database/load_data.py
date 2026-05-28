import sqlite3
import pandas as pd
import os


def load_to_sqlite(csv_path, db_path='database/battery.db'):
    df = pd.read_csv(csv_path)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)

    with open('database/schema.sql', 'r') as f:
        conn.executescript(f.read())

    df.to_sql('test_results', conn, if_exists='replace', index=False)
    print(f"Loaded {len(df)} records into SQLite → {db_path}")
    conn.close()


if __name__ == "__main__":
    load_to_sqlite('data/cleaned/cleaned_battery_data.csv')
