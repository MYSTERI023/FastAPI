from fastapi import FastAPI
from pydantic import BaseModel
import pickle

final_model = pickle.load(open('final_HIP.pkl','rb'))
scaler = pickle.load(open('scaler1.pkl','rb'))
class person(BaseModel):
    age:int
    bmi:float
    children:int
    sex_enc:int
    smoker_enc:int

health_app = FastAPI()

@health_app.get('/')
def hello():
    return{'message':'hello'}

@health_app.post('/predict')
def predict(per:person):
    q = [[per.age,per.bmi,per.children,per.sex_enc,per.smoker_enc]]
    q_scaled = scaler.transform(q)
    yp = final_model.predict(q_scaled)[0]
    value = round(yp,2)
    return {'predicted_insu':value}