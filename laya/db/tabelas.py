"""Base declarativa para os mapeamentos SQLAlchemy do projeto."""

from sqlalchemy import MetaData, Table
from db.engine import engine, sessiontest
from models import Evento

metadata = MetaData(engine)

eventos = Table("evento", metadata,autoload_with=engine)
medidas = Table("medidas", metadata, autoload_with=engine)
rotacoes = Table("rotacoes", metadata, autoload_with=engine)

def criar_evento(): pass