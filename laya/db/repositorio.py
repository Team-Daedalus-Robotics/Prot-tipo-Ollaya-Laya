"""Consultas somente de leitura às tabelas disponíveis no banco."""

from typing import Any

from sqlalchemy import MetaData, select

from laya.config import QUERY_LIMIT
from laya.db.engine import engine


def listar_dados(limite: int = QUERY_LIMIT) -> dict[str, list[dict[str, Any]]]:
    """Lê até ``limite`` linhas de cada tabela refletida do banco configurado."""
    metadata = MetaData()
    metadata.reflect(bind=engine)
    dados: dict[str, list[dict[str, Any]]] = {}

    with engine.connect() as conexao:
        for tabela in metadata.sorted_tables:
            consulta = select(tabela).limit(limite)
            dados[tabela.name] = [dict(linha) for linha in conexao.execute(consulta).mappings()]

    return dados
