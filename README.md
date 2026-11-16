# Laya

A command-line application that reads records from the configured database and uses the TypeSafe `/api/decide` endpoint to evaluate whether the context contains sufficient information to answer a question.

## Configuration

Create a `.env` file in the project root:

```dotenv
DATABASE_URL=sqlite:///./config/db/db.sqlite3
API_KEY=local
BASE_URL=http://localhost:11435
MODEL=laya:multilingual
QUERY_LIMIT=100
```

`DATABASE_URL` can point to another database supported by SQLAlchemy. The repository reflects the existing tables and reads up to `QUERY_LIMIT` rows from each table.

## Running

```sh
uv run laya
```

The process prompts the user for a question, queries the database, and displays the probability that the context contains sufficient information.

`/api/decide` returns typed decisions (`choice`, `score`, or `noul`), not generated text. To receive free-form responses in Portuguese, a generative endpoint must be connected.
