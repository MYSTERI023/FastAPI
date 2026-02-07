import streamlit as st
import requests
import json
st.title('Health Isurance Prediction App',text_alignment='center')
name =st.text_input('Enter Your Name')
age = st.number_input('Enter age:',min_value=1, max_value=100, step=1)
bmi = st.number_input('Enter your BMI',min_value=10.0, max_value=50.0, step=0.1)
st.link_button("Know Your BMI", "https://extras.bhf.org.uk/patientinfo/bmi-v1.01/app/index.html")
children = st.number_input('Enter no of children',min_value = 0,step=1)
sex = st.pills('Enter your gender',['Male','Female'])
sex_enc = 1 if sex=='Female'else 0
smoker = st.pills('Do you smoke',['Yes','No'])
smoker_enc = 0 if smoker=='Yes' else 1
X_test = [[age,bmi,children,sex_enc,smoker_enc]]
if st.button("SUBMIT"):
    obj1 = json.dumps({"age":int(age),"bmi":float(bmi),"children":int(children),"sex_enc":int(sex_enc),"smoker_enc":int(smoker_enc)})
    url = 'http://127.0.0.1:8000/predict'
    response = requests.post(url = url,data=obj1)
    output = json.loads(response.text)
    st.success(output["predicted_insu"])