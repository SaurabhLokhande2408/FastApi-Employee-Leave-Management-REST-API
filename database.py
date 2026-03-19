from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:roots@localhost:5432/Sugarboo"
engine=create_engine(db_url,pool_pre_ping=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)