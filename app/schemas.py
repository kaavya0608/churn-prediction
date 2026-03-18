from pydantic import BaseModel
from typing import Optional

class CustomerCreate(BaseModel):
    gender: int
    senior_citizen: int
    partner: int
    dependents: int
    tenure: int
    phone_service: int
    multiple_lines: str
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str
    contract: str
    paperless_billing: int
    payment_method: str
    monthly_charges: float
    total_charges: float

class CustomerResponse(BaseModel):
    id: int
    gender: int
    senior_citizen: int
    partner: int
    dependents: int
    tenure: int
    monthly_charges: float
    total_charges: float
    churn_probability: Optional[float] = None

    class Config:
        from_attributes = True

class RiskResponse(BaseModel):
    customer_id: int
    churn_probability: float
    risk_level: str