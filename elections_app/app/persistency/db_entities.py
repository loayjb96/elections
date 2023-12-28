from sqlalchemy import Column, Integer, String, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'

    identity_number = Column(String, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    father_name = Column(String)
    locality_code = Column(String)
    ballot_number = Column(String)
    locality_name = Column(String)
    street_code = Column(String)
    street_name = Column(String)
    house_number = Column(String)
    ballot_order_number = Column(String)
    postal_code = Column(String)
    voted = Column(Boolean)

# Database connection
DATABASE_URL = 'postgresql://default:J1cGL3KPoBUt@ep-calm-union-38725535-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb'
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)