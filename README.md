# Customer Churn Prediction System

An end-to-end machine learning system that predicts customer churn probability and serves predictions via a REST API.

## Tech Stack
- **ML**: Python, pandas, scikit-learn, Logistic Regression
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Testing**: Pytest
- **Deployment**: Docker, Docker Compose

## Project Structure
```
churn-prediction/
├── app/
│   ├── main.py          # FastAPI endpoints
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # DB connection
│   └── predictor.py     # ML model loader
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
├── models/              # Saved model files
├── data/                # Dataset files
├── test_api.py          # Pytest tests
├── Dockerfile
└── docker-compose.yml
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/customers` | Add a new customer |
| GET | `/customers/{id}/risk` | Get churn risk score |
| GET | `/customers/high-risk` | List high risk customers |
| POST | `/customers/score-all` | Score all customers |

## Quick Start

### Run with Docker
```bash
docker-compose up --build
```

### Run locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Run tests
```bash
pytest test_api.py -v
```

## API docs
Once running, visit `http://localhost:8000/docs` for interactive Swagger UI.

## Model Performance
- **Algorithm**: Logistic Regression
- **ROC-AUC**: 0.832
- **Dataset**: Telco Customer Churn (7,032 records)

## Sample Response
```json
{
  "customer_id": 1,
  "churn_probability": 0.82,
  "risk_level": "high"
}
```
