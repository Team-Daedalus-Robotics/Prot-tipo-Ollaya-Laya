import os
from pathlib import Path


def carregar_env():
    arquivo = Path(__file__).resolve().parents[3] / ".env"

    if arquivo.exists():
        for linha in arquivo.read_text().splitlines():
            if "=" in linha:
                nome, valor = linha.split("=", 1)
                os.environ.setdefault(nome.strip(), valor.strip().strip('"').strip("'"))


carregar_env()

BASE_URL = os.getenv("TYPESAFE_BASE_URL", "http://localhost:11435")
API_KEY = os.getenv("TYPESAFE_API_KEY", "local")
MODEL = os.getenv("TYPESAFE_DEFAULT_MODEL", "laya")
