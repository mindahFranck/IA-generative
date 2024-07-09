from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class DetectionResult(Base):
    __tablename__ = "detection_results"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, index=True)
    country = Column(String, index=True)
    accuracy = Column(Float)
    timestamp = Column(DateTime)

class GenerationResult(Base):
    __tablename__ = "generation_results"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    generated_plate = Column(String)
    timestamp = Column(DateTime)

DATABASE_URL = "mysql+pymysql://root:@localhost/license_plate_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
