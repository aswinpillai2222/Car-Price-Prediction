Car Price Prediction API 🚗💰

Overview

This repository contains a FastAPI-based car price prediction API deployed on Hugging Face Spaces. The API predicts car prices based on input features such as brand, model, year, engine size, fuel type, transmission, mileage, doors, and owner count.

Features

✅ Built with FastAPI for high-performance API requests✅ Uses Machine Learning (Random Forest) for price prediction✅ Deployed using Docker & Hugging Face Spaces✅ Supports both CURL and Python requests

📂 Project Structure

📁 Car-Price-Prediction-API
│── 📄 app.py            # FastAPI application
│── 📄 Dockerfile        # Configuration for deployment on Hugging Face Spaces
│── 📄 requirements.txt  # List of required Python packages
│── 📄 model.pkl         # Pre-trained machine learning model
│── 📄 encoder.pkl       # Label encoder for categorical features
│── 📄 car_price_dataset.csv  # Training dataset (optional)

🚀 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/car-price-prediction.git
cd car-price-prediction

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the API Locally

uvicorn app:app --reload --host 0.0.0.0 --port 7860

API will be available at: http://127.0.0.1:7860

📦 Deployment on Hugging Face Spaces

1️⃣ Create a Hugging Face Space

Go to Hugging Face Spaces

Click New Space → Set it to Docker

Clone this repository and push it to your Hugging Face Space.

2️⃣ Push Your Code to Hugging Face

git remote add origin git@huggingface.co:YOUR_USERNAME/car-price-prediction.git
git add .
git commit -m "Deploying API on Hugging Face Spaces"
git push -u origin main

Once deployed, your API will be available at:

https://car-price-prediction.hf.space

📌 API Endpoints

1️⃣ Test Root Endpoint

curl -X GET "https://car-price-prediction.hf.space/"

Response:

{ "message": "Car Price Prediction API is running on Hugging Face!" }

2️⃣ Test /predict Endpoint

Using CURL:

curl -X POST "https://car-price-prediction.hf.space/predict" \
     -H "Content-Type: application/json" \
     -d '{"Brand": "Toyota", "Model": "Corolla", "Year": 2015, "Engine_Size": 1.8, "Fuel_Type": "Petrol", "Transmission": "Automatic", "Mileage": 50000, "Doors": 4, "Owner_Count": 1}'

Using Python:

import requests

url = "https://car-price-prediction.hf.space/predict"
data = {
    "Brand": "Toyota",
    "Model": "Corolla",
    "Year": 2015,
    "Engine_Size": 1.8,
    "Fuel_Type": "Petrol",
    "Transmission": "Automatic",
    "Mileage": 50000,
    "Doors": 4,
    "Owner_Count": 1
}
response = requests.post(url, json=data)
print(response.json())

Example Response:

{
    "predicted_price": 450000
}

🛠 Troubleshooting & Debugging

1️⃣ If the API does not start locally:

Ensure dependencies are installed: pip install -r requirements.txt

Check port availability: netstat -an | find "7860"

2️⃣ If the Hugging Face Space is not deploying:

Ensure Docker is configured correctly

Run: git push -u origin main to update the deployment

👨‍💻 Contributing

If you would like to contribute to this project, fork the repository and submit a pull request.

📜 License

This project is MIT licensed. Feel free to use, modify, and distribute it as needed.

💡 Acknowledgments

🔹 Built with FastAPI & Machine Learning 🚀🔹 Deployed on Hugging Face Spaces🔹 Created by Aswin Pillai 🎯

