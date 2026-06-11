import streamlit as st
import pickle

model = pickle.load(open("model.pkl","rb"))

st.title("Placement Prediction")

cgpa = st.number_input("CGPA")
iq = st.number_input("IQ")

if st.button("Predict"):
    prediction = model.predict([[cgpa, iq]])

    if prediction[0] == 1:
        st.success("Placed")
    else:
        st.error("Not Placed")
