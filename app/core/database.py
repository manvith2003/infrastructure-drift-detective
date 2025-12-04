from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# SQLAlchemy base class for models
Base = declarative_base()

# Create engine using DB URL from settings (.env)
engine = create_engine(settings.DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
