from src.actions.db_connection import get_connection

def execute():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM memories")
    count = c.fetchone()[0]
    conn.close()
    return count
