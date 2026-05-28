import sqlite3
import pandas as pd

conn = sqlite3.connect('database/battery.db')

queries = {
    "Peak Testing Hours": """
        SELECT hour, COUNT(*) as test_count
        FROM test_results
        GROUP BY hour ORDER BY test_count DESC LIMIT 5
    """,
    "Average Retention by Test Type": """
        SELECT test_type,
               ROUND(AVG(retention_rate), 2) as avg_retention,
               COUNT(*) as total_tests
        FROM test_results
        GROUP BY test_type ORDER BY avg_retention DESC
    """,
    "Pass vs Fail Rate": """
        SELECT status, COUNT(*) as count,
               ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM test_results), 2) as percentage
        FROM test_results GROUP BY status
    """,
    "Overutilized Batteries (400+ cycles)": """
        SELECT battery_id, MAX(cycle_number) as max_cycles,
               ROUND(AVG(retention_rate), 2) as avg_retention
        FROM test_results
        GROUP BY battery_id
        HAVING max_cycles > 400
        ORDER BY max_cycles DESC
    """
}

for title, query in queries.items():
    print(f"\n{'='*40}")
    print(f"{title}")
    print('='*40)
    print(pd.read_sql_query(query, conn).to_string(index=False))

conn.close()
