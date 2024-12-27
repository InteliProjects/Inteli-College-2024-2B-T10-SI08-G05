from config.connections import get_postgres_connection

def log_observability(metric_name, start_time, end_time, details):
    conn = get_postgres_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS observability_g5 (
            id SERIAL PRIMARY KEY,
            metric_name VARCHAR(255),
            start_time TIMESTAMP,
            end_time TIMESTAMP,
            duration INTERVAL,
            details TEXT
        )
    ''')

    duration = end_time - start_time
    cursor.execute('''
        INSERT INTO observability_g5 (metric_name, start_time, end_time, duration, details)
        VALUES (%s, %s, %s, %s, %s)
    ''', (metric_name, start_time, end_time, duration, details))

    conn.commit()
    cursor.close()
    conn.close()