import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'


class Settings:
    PROJECT_NAME: str = "GCC-Comedor-API"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL = "sqlite:///./sql_app.db"


settings = Settings()