import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "GCC-Comedor-API"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL = "sqlite:///./sql_app.db"

    # HASHING TOKEN
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    TEST_USER_EMAIL = "test@example.com"


settings = Settings()
