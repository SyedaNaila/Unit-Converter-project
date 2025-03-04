
import streamlit as st

# Streamlit app Title
st.title("Unit Converter")

# User se input lena
value = st.number_input("Enter the value:")  # User se value input lena
unit = st.selectbox(
    "Select the unit to convert from:",
    ["Celsius (°C)", "Fahrenheit (°F)", "Meters (m)", "Feet (ft)", "Kilograms (kg)", "Pounds (lbs)"]
)  # User se unit input lena

# Conversion logic
if unit == "Celsius (°C)":  # Celsius to Fahrenheit
    converted_value = (value * 9/5) + 32
    st.write(f"{value}°C is equal to {converted_value}°F")
elif unit == "Fahrenheit (°F)":  # Fahrenheit to Celsius
    converted_value = (value - 32) * 5/9
    st.write(f"{value}°F is equal to {converted_value}°C")
elif unit == "Meters (m)":  # Meters to Feet
    converted_value = value * 3.28084
    st.write(f"{value} meters is equal to {converted_value} feet")
elif unit == "Feet (ft)":  # Feet to Meters
    converted_value = value / 3.28084
    st.write(f"{value} feet is equal to {converted_value} meters")
elif unit == "Kilograms (kg)":  # Kilograms to Pounds
    converted_value = value * 2.20462
    st.write(f"{value} kilograms is equal to {converted_value} pounds")
elif unit == "Pounds (lbs)":  # Pounds to Kilograms
    converted_value = value / 2.20462
    st.write(f"{value} pounds is equal to {converted_value} kilograms")
else:
    st.write("Invalid unit entered. Please try again.")  # Agar unit sahi nahi hai