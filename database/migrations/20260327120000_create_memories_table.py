from src.actions.db_connection import get_connection

def execute():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            name TEXT NOT NULL,
            text TEXT NOT NULL,
            image_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

def rollback():
    conn = get_connection()
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS memories')
    conn.commit()
