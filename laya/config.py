"""Configuração da aplicação carregada a partir do ambiente e de ``.env``."""

import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

DATABASE_EXTERN_URL = os.getenv("DATABASE_URL", "sqlite:///teste.db")
#adiconar database interno
API_KEY = os.getenv("API_KEY", os.getenv("TYPESAFE_API_KEY", "local"))
BASE_URL = os.getenv(
    "BASE_URL",
    os.getenv("TYPESAFE_BASE_URL", "http://localhost:11435"),
).rstrip("/")
MODEL = os.getenv(
    "MODEL",
    os.getenv("TYPESAFE_DEFAULT_MODEL", "laya:multilingual"),
)
DECIDE_URL = f"{BASE_URL}/api/decide"
QUERY_LIMIT = int(os.getenv("QUERY_LIMIT", "100"))
