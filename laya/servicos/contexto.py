"""Conversão dos registros do banco em contexto legível pelo modelo."""

from collections.abc import Mapping, Sequence
from typing import Any


def montar_contexto(dados: Mapping[str, Sequence[Mapping[str, Any]]]) -> str:
    if not dados:
        return "O banco de dados não contém tabelas disponíveis."

    blocos = []
    for tabela, linhas in dados.items():
        blocos.append(f"Tabela {tabela} ({len(linhas)} registros):")
        if not linhas:
            blocos.append("  (sem registros)")
            continue
        for indice, linha in enumerate(linhas, start=1):
            valores = "; ".join(f"{coluna}: {valor}" for coluna, valor in linha.items())
            blocos.append(f"  {indice}. {valores}")

    return "\n".join(blocos)
