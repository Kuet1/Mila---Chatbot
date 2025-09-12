from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# Cria o Banco de dados
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
