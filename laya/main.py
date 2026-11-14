"""Ponto de entrada: pergunta -> dados -> resposta."""

from laya.db.repositorio import listar_dados
from laya.llm.cliente import avaliar_contexto
from laya.servicos.contexto import montar_contexto


def main() -> None:
    pergunta = input("Pergunta: ").strip()
    if not pergunta:
        print("Digite uma pergunta.")
        return

    dados = listar_dados()
    contexto = montar_contexto(dados)
    probabilidade = avaliar_contexto(pergunta, contexto)
    print(f"Probabilidade de o contexto conter dados suficientes: {probabilidade:.1%}")


if __name__ == "__main__":
    main()
