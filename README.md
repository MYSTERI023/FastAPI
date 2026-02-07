# FastAPI
Health Insurance Cost Prediction – ML Deployment with FastAPI & Streamlit
This project builds and deploys a machine learning model to predict health insurance charges based on user inputs.
It demonstrates an end-to-end ML pipeline: training → API serving → web interface.
├── Health_model.ipynb         # Model training notebook
├── APP_HIP.py                 # FastAPI backend
├── front_end.py               # Streamlit frontend
├── final_HIP.pkl              # Trained model
├── scaler1.pkl                # Feature scaler
└── README.md

# Features
├── Data preprocessing & encoding
├── Feature scaling
├── Regression model training
├── REST API using FastAPI
├── Interactive web UI using Streamlit
├── Complete ML deployment workflow

# Model Inputs
1.Age
2.BMI
3.Number of children
4.Sex
5.Smoker

# System Flow
User → Streamlit → FastAPI → ML Model → Prediction → Streamlit

# Tech Stack
├── Python
├── Pandas, NumPy
├── Scikit-Learn
├── FastAPI
├── Streamlit
├── Uvicorn
