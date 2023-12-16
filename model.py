from sqlalchemy import create_engine, Column, Integer, String, DateTime, DECIMAL, func
from sqlalchemy.orm import sessionmaker, declarative_base
import config


database=config.DATABASES['DBNAME']
user=config.DATABASES['USER']
password=config.DATABASES['PASSWORD']
host=config.DATABASES['HOST']
port=config.DATABASES['PORT']

connection_string = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}/{database}',echo=False)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class StockEODPrice(Base):
    __tablename__ = 'stock_eod_price'

    id = Column(Integer, primary_key=True)
    stock_ticker = Column(String(10))
    eod_date = Column(String(50))
    open_price = Column(DECIMAL(14,7))
    close_price = Column(DECIMAL(14,7))
    created_date = Column(DateTime, default=func.current_timestamp())
Base.metadata.create_all(engine)