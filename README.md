**Overview**
The Employee Performance Prediction App is a web-based application built with Streamlit. It uses a machine learning model to predict employee performance based on input parameters like years at the company, monthly salary, overtime hours, number of promotions, and satisfaction score.

This project is designed to help organizations estimate employee performance scores to assist in workforce planning and management.

**Features**
User-Friendly Interface: Intuitive and visually appealing UI for easy data input and interaction.
Real-Time Predictions: Provides quick predictions based on the given employee data.
Custom Styling: Styled using custom CSS for a polished appearance.
Secure Inputs: Handles edge cases with validation for all user inputs.
How It Works
Input Details: The user inputs the following parameters:

Years at the company
Monthly salary
Overtime hours
Number of promotions
Satisfaction score (scale of 0.0 to 5.0)
Prediction: On submitting the details, the app:

Normalizes the input data using a pre-trained scaler (scaler.pkl).
Predicts the employee performance score using a machine learning model (model.pkl).
Output: Displays the predicted performance score with a clean and concise summary.

**Files and Their Purpose**
1. app.py
The main Streamlit app script. It contains:

The logic for user input collection.
Integration of the pre-trained scaler and model for predictions.
Custom styling and layout configurations.
Prediction button and logic for displaying results.
2. dataset.csv
Contains the dataset used for training the machine learning model.

3. model.pkl
Serialized machine learning model used for prediction.

4. scaler.pkl
Serialized scaler for normalizing input data.

5. notebook.ipynb
A Jupyter notebook file containing exploratory data analysis, preprocessing, and the model training pipeline.

