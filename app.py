import streamlit as st
import joblib
import pandas as pd
model = joblib.load("car_price_model.pkl")
st.title("🚗 Car Price Prediction")
st.write("Enter car details below")

model_year = st.number_input(
    "Model Year",
    min_value=2000,
    max_value=2025,
    value=2020
)

engine_size = st.number_input(
    "Engine Size",
    min_value=0.5,
    max_value=10.0,
    value=2.0
)

mileage = st.number_input(
    "km_driven",
    min_value=0,
    value=300000
)

doors = st.number_input(
    "Doors",
    min_value=2,
    max_value=6,
    value=4
)

owner_count = st.number_input(
    "Owner Count",
    min_value=0,
    max_value=10,
    value=1
)

horsepower = st.number_input(
    "Horsepower",
    min_value=50,
    max_value=1000,
    value=150
)

brand = st.selectbox(
    "Brand",
    ["Toyota","BMW","Ford","Honda",'Hyundai','Tesla']
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","Electric"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual","Automatic"]
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
    "Brand":[str(brand)],
    "Model_Year":[int(model_year)],
    "Engine_Size":[float(engine_size)],
    "Fuel_Type":[str(fuel_type)],
    "Transmission":[str(transmission)],
    "km_driven":[int(mileage)],
    "Doors":[int(doors)],
    "Owner_Count":[int(owner_count)],
    "Horsepower":[int(horsepower)]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Car Price: ${prediction[0]:,.2f}"
    )