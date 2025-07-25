from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only. Replace with frontend URL in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = joblib.load("model/transaction_model.joblib")

# Define the input schema
class TransactionData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float

@app.post("/predict")
def predict(data: TransactionData):
    input_data = np.array([[data.feature1, data.feature2, data.feature3, data.feature4, data.feature5]])
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    return {
        "prediction": int(prediction[0]),
        "probability": probability[0].tolist()
    }
@app.get("/")
def read_root():
    return {"message": "Andromeda Security ML API is running "}

#class Features(BaseModel):
    #feature1: float
    #feature2: float
    #feature3: float
    #feature4: float
    #feature5: float

#@app.post("/predict")
#def predict(features: Features):
    #return {"prediction": "normal", "confidence": 0.95}

