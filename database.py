from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
#url creation
db_url="postgresql://postgres:roots@localhost:5432/Sugarboo"

#starting db engine
'''
pre-pool-ping checks if db is alive or not
'''
engine=create_engine(db_url,pool_pre_ping=True)

#starting sessions
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)