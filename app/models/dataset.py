from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base

class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column(String)
    ingresos = Column(Float)
    poblacion = Column(Integer)


class EliminatedData(Base):
    __tablename__ = "eliminated_data"

    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column(String)
    ingresos = Column(String)
    poblacion = Column(String)
    razon_eliminacion = Column(String)  # "valor nulo", "duplicado", etc