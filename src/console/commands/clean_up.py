import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.actions.db_connection import get_connection

def clean_up():
    print("Starting cleanup process...")
    
    # 1. Clean up database table
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('DELETE FROM memories')
        conn.commit()
        print("Emptied the 'memories' table.")
    except Exception as e:
        print(f"Database clean up failed: {e}")

    # 2. Clean up uploads
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    uploads_dir = os.path.join(root_dir, 'storage', 'uploads')
    
    if os.path.exists(uploads_dir):
        files_removed = 0
        for filename in os.listdir(uploads_dir):
            if filename != '.gitignore':
                filepath = os.path.join(uploads_dir, filename)
                try:
                    if os.path.isfile(filepath) or os.path.islink(filepath):
                        os.unlink(filepath)
                        files_removed += 1
                except Exception as e:
                    print(f"Failed to delete {filepath}. Reason: {e}")
        print(f"Deleted {files_removed} files from {uploads_dir}.")
    else:
        print(f"Uploads directory {uploads_dir} does not exist.")

if __name__ == "__main__":
    clean_up()
    print("Cleanup completed.")
