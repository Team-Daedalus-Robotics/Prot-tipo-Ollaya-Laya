"""Engine e fábrica de sessões do SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from laya.config import DATABASE_URL,  DATABASE_EXTERN_URL


engine = create_engine(DATABASE_URL)
engine_test = create_engine(DATABASE_EXTERN_URL)
session = sessionmaker(bind=engine, expire_on_commit=False)
base_session = sessionmaker(DATABASE_EXTERN_URL)
sessiontest = base_session()
