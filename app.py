import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIPML.pkl', 'rb'))

st.header('Medical Insurance Premium Predictor')

gender = st.selectbox('Gender', ['Male', 'Female'])
smoker = st.selectbox('Are You a Smoker', ['Yes', 'No'])
region = st.selectbox('Region', ['NorthWest', 'NorthEast', 'SouthWest', 'SouthEast'])
age = st.slider('Age', 5, 90)
bmi = st.slider('BMI', 5.0, 70.0)
children = st.slider('Number of Children', 0, 5)

if gender == 'Male':
    gender = 1
else:
    gender = 0

if smoker == 'Yes':
    smoker = 1
else:
    smoker = 0

if region == 'SouthEast':
    region = 0
elif region == 'SouthWest':
    region = 1
elif region == 'NorthEast':
    region = 2
else:
    region = 3

input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1, -1)

predicted_premium = model.predict(input_data)

display_string = f'Your Predicted Medical Insurance Premium is : {predicted_premium[0]:.2f} $ (USD)'

st.markdown(display_string)