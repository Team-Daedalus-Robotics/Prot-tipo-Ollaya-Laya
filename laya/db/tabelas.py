"""Base declarativa para os mapeamentos SQLAlchemy do projeto."""

from sqlalchemy import MetaData, Table
from db.engine import engine
from models import Evento

metadata = MetaData(engine)

eventos = Table("evento", metadata,autoload_with=engine)
medidas = Table("medidas", metadata, autoload_with=engine)
rotacoes = Table("rotacoes", metadata, autoload_with=engine)
