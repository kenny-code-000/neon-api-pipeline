import os

def must_getenv(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value

DATABASE_URL = must_getenv("DATABASE_URL")
API_BASE_URL = os.getenv("API_BASE_URL", "")
API_TOKEN = os.getenv("API_TOKEN", "")