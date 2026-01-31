import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv  # Импортируем загрузчик

# Загружаем переменные из файла .env в систему
load_dotenv()

# Читаем переменную DATABASE_URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Проверка: если вдруг забыли создать .env, программа выдаст понятную ошибку
if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("DATABASE_URL не найден в файле .env!")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    client_encoding='utf8'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()