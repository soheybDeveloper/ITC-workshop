import os
import sys
import importlib.util

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.actions.db_connection import get_connection

def run_migrations():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    migrations_dir = os.path.join(root_dir, 'database', 'migrations')
    
    if not os.path.exists(migrations_dir):
        os.makedirs(migrations_dir)
        return
        
    conn = get_connection()
    c = conn.cursor()
    
    # Ensure migrations tracking table exists
    c.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL UNIQUE,
            executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    
    # Get already executed migrations
    c.execute('SELECT filename FROM migrations')
    executed = set(row[0] for row in c.fetchall())
        
    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.py') and f != '__init__.py'])
    
    for filename in migration_files:
        if filename in executed:
            continue
            
        filepath = os.path.join(migrations_dir, filename)
        module_name = filename[:-3]
        
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        print(f"Running migration: {filename}")
        if hasattr(module, 'execute'):
            try:
                module.execute()
                c.execute('INSERT INTO migrations (filename) VALUES (?)', (filename,))
                conn.commit()
                print(f"Successfully executed {filename}")
            except Exception as e:
                print(f"Failed to execute {filename}: {e}")
                if hasattr(module, 'rollback'):
                    print(f"Rolling back {filename}")
                    try:
                        module.rollback()
                        print(f"Rolled back {filename}")
                    except Exception as re:
                        print(f"Failed to rollback {filename}: {re}")
                break

if __name__ == "__main__":
    print("Running database migration loop...")
    run_migrations()
    print("Migration check completed.")
