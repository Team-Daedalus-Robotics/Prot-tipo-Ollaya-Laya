"""Cliente para o endpoint ``/api/decide``."""

from typing import Any

import requests
from typesafe_sdk import TypeSafeClient

from laya.config import API_KEY, BASE_URL, DECIDE_URL, MODEL


def criar_cliente() -> TypeSafeClient:
    return TypeSafeClient(api_key=API_KEY, base_url=BASE_URL, model=MODEL)


def avaliar_contexto(pergunta: str, contexto: str, timeout: float = 60) -> float:
    """Retorna a probabilidade de o contexto conter dados para a pergunta.

    O endpoint ``/api/decide`` responde perguntas tipadas (choice, score, noul),
    não gera texto livre. Por isso, esta integração avalia suficiência do contexto.
    """
    resposta = requests.post(
        DECIDE_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": MODEL,
            "state": f"Contexto dos dados:\n{contexto}\n\nPergunta: {pergunta}",
            "questions": {
                "contexto_suficiente": {
                    "type": "noul",
                    "instructions": "O contexto contém dados suficientes para responder à pergunta do usuário?",
                    "criteria": {
                        "true": "O contexto contém dados suficientes para responder.",
                        "false": "O contexto não contém dados suficientes para responder.",
                    },
                }
            },
        },
        timeout=timeout,
    )
    resposta.raise_for_status()
    payload: dict[str, Any] = resposta.json()
    return float(payload["answers"]["contexto_suficiente"]["noul"])
