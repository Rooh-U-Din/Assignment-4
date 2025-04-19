# Project 8: Create a Python Streamlit BMI Calculator

import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height in cm:", 100, 250, 175)
weight = st.slider("Enter your weight in kg:", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

st.write("BMI Categories:")
st.write("Underweight: BMI < 18.5")
st.write("Normal weight: 18.5 <= BMI < 25")
st.write("Overweight: 25 <= BMI < 30")
st.write("Obesity: BMI >= 30")
