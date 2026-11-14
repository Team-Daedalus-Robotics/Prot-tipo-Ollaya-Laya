# Laya

Aplicação de linha de comando que lê registros do banco configurado e usa o
endpoint TypeSafe `/api/decide` para avaliar se o contexto contém dados
suficientes para responder a uma pergunta.

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```dotenv
DATABASE_URL=sqlite:///./config/db/db.sqlite3
API_KEY=local
BASE_URL=http://localhost:11435
MODEL=laya:multilingual
QUERY_LIMIT=100
```

`DATABASE_URL` pode apontar para outro banco suportado pelo SQLAlchemy. O
repositório reflete as tabelas existentes e lê até `QUERY_LIMIT` linhas de cada
tabela.

## Executar

```sh
uv run laya
```

O processo solicita uma pergunta, consulta o banco e mostra a probabilidade de
o contexto conter informação suficiente. `/api/decide` retorna decisões
tipadas (`choice`, `score` ou `noul`), não texto gerado; para receber respostas
livres em português, será necessário conectar um endpoint generativo.
