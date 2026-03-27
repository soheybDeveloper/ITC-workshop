import sqlite3
import os
from config.config import Config

from src.console.commands.run_migration import run_migrations

def execute():
    os.makedirs("database", exist_ok=True)
    run_migrations()
