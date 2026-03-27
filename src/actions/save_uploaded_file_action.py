import os
import uuid
from config.config import Config

def execute(uploaded_file):
    if uploaded_file is None:
        return None, "No file uploaded"

    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > Config.UPLOAD_LIMIT_MB:
        return None, f"File is too large! Maximum allowed size is {Config.UPLOAD_LIMIT_MB}MB."

    ext = os.path.splitext(uploaded_file.name)[1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    
    # Update to new storage location
    save_path = os.path.join("storage", "uploads", unique_filename)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path, "File saved successfully!"
