# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)
import pickle


# title of the sidebar
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

# title of the body
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)


# defining variables for user input
km = st.sidebar.slider("What is total KM the has car?", 0, 317000, step=100)
Comfort_Convenience = st.sidebar.slider("How many Comfort Convenience?", 1, 33, step=1)
Safety_Security = st.sidebar.slider("How many Safety Security?", 1, 29, step=1)
hp_kW = st.sidebar.slider("What is the Hourse power in kW?", 40, 294, step=10)
Weight_kg = st.sidebar.slider("What is the weight ?", 840, 2471, step=100)
cons_comb = st.sidebar.slider("What is the weight ?", 3, 9, step=1)


# converting user inputs into dictionary format
my_dict = {
    "km": km,
    "Comfort_Convenience": Comfort_Convenience,
    "Safety_Security": Safety_Security,
    'hp_kW': hp_kW,
    "Weight_kg": Weight_kg,
    "cons_comb": cons_comb
}


# To load machine learning model

filename = "saved_model1.pkl"
model=pickle.load(open(filename, "rb"))

df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
