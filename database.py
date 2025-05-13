from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
DATABASE_URL = "mysql+pymysql://fastmed_user:secret123@localhost/fastmed"

#DATABASE_URL = "mysql+pymysql://root:@localhost/fastmed"

#DATABASE_URL = "mysql+pymysql://root:@localhost/fastmed"


#server=localhost;database=myshops_db;user=root;
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# engine = create_async_engine(DATABASE_URL, echo=True)
# async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# async def get_async_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session

Base = declarative_base()
