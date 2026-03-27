import os
import shutil
import sys

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.console.commands.run_migration import run_migrations

def copy_env_file():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    env_example = os.path.join(root_dir, '.env.example')
    env_file = os.path.join(root_dir, '.env')
    
    if os.path.exists(env_example):
        shutil.copy(env_example, env_file)
        print(f"Copied {env_example} to {env_file}")
    else:
        print(f"Error: {env_example} not found.")
        sys.exit(1)

def execute_migrations():
    print("Executing database migrations...")
    run_migrations()

def run_deploy_pipeline():
    print("Starting deploy pipeline...")
    copy_env_file()
    execute_migrations()
    print("Deploy pipeline completed successfully.")

if __name__ == "__main__":
    run_deploy_pipeline()
