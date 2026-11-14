from typesafe_sdk import TypeSafeClient

from modelInfos import API_KEY, BASE_URL, MODEL
import requests



def criar_cliente():
    return TypeSafeClient(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL,
    )


# Already using a TypeSafe SDK? Set TYPESAFE_BASE_URL=http://localhost:11435 instead.

response = requests.post(
    "http://localhost:11435/api/decide",
    json={
        "model": MODEL,
        "state": "I was charged twice for my subscription this month and want a refund.",
        "questions": {
            "department": {
                "type": "choice",
                "instructions": "Which team should handle this?",
                "criteria": {
                    "billing": "Payments, invoices and refunds",
                    "technical": "Bugs, errors and outages",
                    "account": "Login, profile and settings"
                }
            },
            "refund": {
                "type": "noul",
                "instructions": "Is the customer asking for a refund?"
            }
        }
    },
)
answers = response.json()["answers"]
print(answers["department"]["choice"], answers["refund"]["noul"])