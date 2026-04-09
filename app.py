# bmi_app.py
import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")

st.write("Enter your weight in kilograms and height in meters.")

weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height * height)
        st.success(f"Your BMI is: {bmi:.2f}")
    else:
        st.error("Height must be greater than 0.")
