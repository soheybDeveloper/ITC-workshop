from src.actions.db_connection import get_connection

def execute(limit: int = 10, offset: int = 0):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        SELECT * FROM memories
        ORDER BY created_at DESC
        LIMIT ? OFFSET ?
    ''', (limit, offset))
    records = c.fetchall()
    conn.close()
    return [dict(row) for row in records]
