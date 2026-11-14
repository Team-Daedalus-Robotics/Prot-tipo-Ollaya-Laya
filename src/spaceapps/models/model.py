from typesafe_sdk import TypeSafeClient

from .modelInfos import API_KEY, BASE_URL, MODEL


def criar_cliente():
    return TypeSafeClient(
        api_key=API_KEY,
        base_url=BASE_URL,
        default_model=MODEL,
    )
