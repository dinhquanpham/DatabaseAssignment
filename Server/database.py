from sqlalchemy import create_engine
from typing import Generator
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:dinhquan@localhost:3306/hospital"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    print("Connect database successfully!")
except:
    print("Connect database fail!")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()