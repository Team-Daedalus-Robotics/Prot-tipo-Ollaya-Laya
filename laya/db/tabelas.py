"""Base declarativa para os mapeamentos SQLAlchemy do projeto."""

from sqlalchemy import MetaData, Table
from db.engine import engine

from sqlalchemy.orm import DeclarativeBase

metadata = MetaData(engine)

eventos = Table("eventos", metadata,autoload_with=engine)
medidas = Table("medidas", metadata, autoload_with=engine)
rotacoes = Table("rotacoes", metadata, autoload_with=engine)
medidas = Table("medidas", metadata, autoload_with=engine)

class Base(DeclarativeBase):
    pass
