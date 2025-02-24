from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

# Load trained model and encoder
model = joblib.load("car_price_model.pkl")
encoder = joblib.load("encoder.pkl")

@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running on Hugging Face!"}

@app.post("/predict")
def predict(data: dict):
    try:
        input_data = pd.DataFrame([data])

        # Convert categorical features using Label Encoder
        categorical_columns = ["Brand", "Model", "Fuel_Type", "Transmission"]
        for col in categorical_columns:
            if col in input_data.columns:
                input_data[col] = encoder.transform([input_data[col][0]])

        # Convert to numpy array
        input_array = np.array(input_data)

        # Make prediction
        prediction = model.predict(input_array)

        return {"predicted_price": round(prediction[0], 2)}

    except Exception as e:
        return {"error": str(e)}
