from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app import models, schemas
from app.predictor import predict_churn, get_risk_level

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Churn Prediction API")

@app.get("/")
def root():
    return {"message": "Churn Prediction API is running"}

@app.post("/customers", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customer_id}/risk", response_model=schemas.RiskResponse)
def get_risk(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    customer_data = {
        "gender": customer.gender,
        "senior_citizen": customer.senior_citizen,
        "partner": customer.partner,
        "dependents": customer.dependents,
        "tenure": customer.tenure,
        "phone_service": customer.phone_service,
        "multiple_lines": customer.multiple_lines,
        "internet_service": customer.internet_service,
        "online_security": customer.online_security,
        "online_backup": customer.online_backup,
        "device_protection": customer.device_protection,
        "tech_support": customer.tech_support,
        "streaming_tv": customer.streaming_tv,
        "streaming_movies": customer.streaming_movies,
        "contract": customer.contract,
        "paperless_billing": customer.paperless_billing,
        "payment_method": customer.payment_method,
        "monthly_charges": customer.monthly_charges,
        "total_charges": customer.total_charges
    }
    
    probability = predict_churn(customer_data)
    customer.churn_probability = probability
    db.commit()
    
    return {
        "customer_id": customer_id,
        "churn_probability": probability,
        "risk_level": get_risk_level(probability)
    }

@app.get("/customers/high-risk")
def get_high_risk(threshold: float = 0.7, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).filter(
        models.Customer.churn_probability >= threshold
    ).all()
    return {"high_risk_customers": len(customers), "customers": customers}

@app.post("/customers/score-all")
def score_all(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    scored = 0
    for customer in customers:
        customer_data = {
            "gender": customer.gender,
            "senior_citizen": customer.senior_citizen,
            "partner": customer.partner,
            "dependents": customer.dependents,
            "tenure": customer.tenure,
            "phone_service": customer.phone_service,
            "multiple_lines": customer.multiple_lines,
            "internet_service": customer.internet_service,
            "online_security": customer.online_security,
            "online_backup": customer.online_backup,
            "device_protection": customer.device_protection,
            "tech_support": customer.tech_support,
            "streaming_tv": customer.streaming_tv,
            "streaming_movies": customer.streaming_movies,
            "contract": customer.contract,
            "paperless_billing": customer.paperless_billing,
            "payment_method": customer.payment_method,
            "monthly_charges": customer.monthly_charges,
            "total_charges": customer.total_charges
        }
        customer.churn_probability = predict_churn(customer_data)
        scored += 1
    db.commit()
    return {"message": f"Scored {scored} customers successfully"}