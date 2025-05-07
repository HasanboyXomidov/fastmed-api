from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://fastmed_user:secret123@localhost/fastmed"

#DATABASE_URL = "mysql+pymysql://root:@localhost/fastmed"

#DATABASE_URL = "mysql+pymysql://root:@localhost/fastmed"


#server=localhost;database=myshops_db;user=root;
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
