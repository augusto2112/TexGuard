
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from bin.db.base import Base

engine = create_engine('mysql+pymysql://root:@localhost/primalinea10', echo=False, encoding='utf-8', pool_recycle=10)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
