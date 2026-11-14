from base import Base
from sqlalchemy import Column, Integer, DATETIME, String



class Evento(Base):
    __tablename__ = "evento"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DATETIME)
    valor = Column(Integer) # valor da temperatura por exemplo
    modelo_sensor = Column(String)
    unidade_de_medida = Column(String) #graus 
    medida = Column(String) #temperatura, umidade e etc

    def criar_evento(self): pass