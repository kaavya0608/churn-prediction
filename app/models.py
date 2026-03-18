from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(Integer)
    senior_citizen = Column(Integer)
    partner = Column(Integer)
    dependents = Column(Integer)
    tenure = Column(Integer)
    phone_service = Column(Integer)
    multiple_lines = Column(String)
    internet_service = Column(String)
    online_security = Column(String)
    online_backup = Column(String)
    device_protection = Column(String)
    tech_support = Column(String)
    streaming_tv = Column(String)
    streaming_movies = Column(String)
    contract = Column(String)
    paperless_billing = Column(Integer)
    payment_method = Column(String)
    monthly_charges = Column(Float)
    total_charges = Column(Float)
    churn_probability = Column(Float, nullable=True)