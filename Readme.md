🚗 Car Price Prediction Using Linear Regression

Project Overview:

This project predicts the price of a car based on various features such as brand, model year, engine size, fuel type, transmission type, kilometers driven, number of doors, owner count, and horsepower.

The model is built using Machine Learning and deployed as an interactive web application using Streamlit.

---

Problem Statement

Estimating the price of a used car is important for buyers and sellers. This project uses Linear Regression to predict car prices based on historical vehicle data.

---

Dataset Features

* Brand
* Model_Year
* Engine_Size
* Fuel_Type
* Transmission
* km_driven
* Doors
* Owner_Count
* Horsepower

Target Variable

* Price

---

Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

---

Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Data Preprocessing
6. Train-Test Split
7. Linear Regression Model Training
8. Model Evaluation
9. Model Serialization using Joblib
10. Streamlit Deployment

---

Model Performance

* Algorithm: Linear Regression
* Evaluation Metrics:

  * R² Score
  * RMSE (Root Mean Squared Error)

The model achieved strong predictive performance on the test dataset.

---

Project Structure

Car_Price_Prediction/

├── app.py
├── car_price_model.pkl
├── requirements.txt
├── README.md

---

Run Locally

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app.py

---

Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter Tuning
* Cloud Deployment
* Enhanced UI Design

---

Author

Mahesh V
B. Tech - Computer Science and Engineering (Data Science)
Machine Learning | Data Analytics | Python | SQL

Live Demo

Streamlit App:
https://car-price-prediction-gcujpkwghqrtghpdenettn.streamlit.app/

GitHub Repository

Repository:
https://github.com/vmahi1206/Car-Price-Prediction
