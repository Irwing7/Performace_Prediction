**Employee Performance Prediction App**

**Overview**

The Employee Performance Prediction App is a web-based application built with Streamlit. It uses a machine learning model to predict employee performance based on input parameters like:

1. Years at the company
2. Monthly salary
3. Overtime hours
4. Number of promotions
5. Satisfaction score
   
This project is designed to help organizations estimate employee performance scores, enabling better workforce planning and management.

**Features**

1. User-Friendly Interface: Intuitive and visually appealing UI for easy data input and interaction.
2. Real-Time Predictions: Provides quick predictions based on the given employee data.
3. Custom Styling: Styled using custom CSS for a polished appearance.
4. Secure Inputs: Handles edge cases with validation for all user inputs.

**How It Works**

**1. Input Details**
The user provides the following input parameters through the app interface:

* Years at the company
* Monthly salary
* Overtime hours
* Number of promotions
* Satisfaction score (scale of 0.0 to 5.0)
  
**2. Prediction**

The app normalizes the input data using a pre-trained scaler (scaler.pkl).
It then predicts the employee performance score using a machine learning model (model.pkl).

**3. Output**

Displays the predicted performance score with a clean and concise summary for the user.

**4. Files and Their Purpose**

* app.py -->
The main Streamlit app script. It contains:
  1. The logic for collecting user inputs.
  2. Integration of the pre-trained scaler and model for predictions.
  3. Custom styling and layout configurations.
  4. Prediction button and logic for displaying results.
   
* dataset.csv -->
The dataset used for training the machine learning model.

* model.pkl -->
The serialized machine learning model is used for prediction.

* scaler.pkl -->
The serialized scaler is used to normalize input data.

* notebook.ipynb -->
A Jupyter Notebook file containing:
  1. Exploratory data analysis (EDA).
  2. Data preprocessing steps.
  3. Model training pipeline.
