from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#DATABASE_URL="postgresql://postgres:postgres@localhost:5432/paynet2"
DATABASE_URL="mysql+pymysql://admin:mysql@localhost:3306/paynet_new_lv"
#DATABASE_URL='sqlite:///./store.db'

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
