import datetime
from config.config import Config
from src.actions.db_connection import get_connection
from src.actions import get_memories_count_action

def execute(title: str, name: str, text: str, image_path: str = None):
    current_count = get_memories_count_action.execute()
    if current_count >= Config.MAX_UPLOADS:
        return False, "Maximum number of memories reached for this workshop!"

    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO memories (title, name, text, image_path, created_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, name, text, image_path, datetime.datetime.now()))
    conn.commit()
    conn.close()
    
    return True, "Memory saved successfully!"
