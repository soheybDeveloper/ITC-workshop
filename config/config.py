import os

class Config:
    # App Settings
    APP_NAME = os.getenv("APP_NAME", "ITC Memories Wall")
    
    # Database
    DB_PATH = os.getenv("DB_PATH", "memories.db")
    
    # Validation Limits
    MAX_UPLOADS = int(os.getenv("MAX_UPLOADS", "50"))
    UPLOAD_LIMIT_MB = int(os.getenv("UPLOAD_LIMIT_MB", "2"))
