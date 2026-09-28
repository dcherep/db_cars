from sqlalchemy import create_engine
from models import Base

engine = create_engine("postgresql://admin:12345@217.71.129.139:6075/cars")

Base.metadata.create_all(bind=engine)
print("База данных и таблицы созданы")