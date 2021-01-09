from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# connect_args={"check_same_thread": False} аргумент, требуемый только для SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# Сеанс для БД. Каждый экземпляр класса - новый сеанс
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для создания моделей
Base = declarative_base()
