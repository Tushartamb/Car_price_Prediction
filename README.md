# Car Price Prediction

## Overview

This project is a Machine Learning-based Car Price Prediction System that estimates the selling price of a used car based on multiple vehicle attributes.<br/>
The model is trained on historical car data and deployed using FastAPI, with a user-friendly web interface built using HTML, CSS, and JavaScript.<br/>
The application allows users to enter car details and instantly receive a predicted market price.<br/>

---

## Features

* Predicts car prices based on multiple vehicle attributes.<br/>
* Data preprocessing and feature engineering pipeline.<br/>
* Machine Learning model trained using Random Forest Regressor.<br/>
* Model evaluation using R² Score.<br/>
* FastAPI backend for serving predictions.<br/>
* Interactive frontend built with HTML, CSS, and JavaScript.<br/>
* Serialized model and preprocessing objects using Pickle for easy deployment.<br/>

---

## Dataset Features

The model uses the following input features:<br/>

| Feature           | Description                           |
| ----------------- | ------------------------------------- |
| Name              | Car Model Name                        |
| Year              | Manufacturing Year                    |
| Kilometers_Driven | Total Kilometers Driven               |
| Fuel_Type         | Fuel Type (Petrol, Diesel, CNG, etc.) |
| Transmission      | Manual or Automatic                   |
| Owner_Type        | Ownership History                     |
| Mileage           | Mileage of Vehicle                    |
| Engine            | Engine Capacity (CC)                  |
| Power             | Engine Power (BHP)                    |
| Seats             | Number of Seats                       |

Target Variable:<br/>

* Price<br/>

---

## Data Preprocessing

Several preprocessing steps were performed before model training.<br/>

### Data Cleaning

* Removed unwanted and irrelevant rows.<br/>
* Removed missing and inconsistent records.<br/>
* Removed extra characters from textual columns.<br/>
* Removed extra spaces from car names and categorical values.<br/>
* Filtered out car models appearing less than five times in the dataset to reduce noise.<br/>

### Categorical Encoding

The following categorical columns were converted into numerical format using LabelEncoder():<br/>

* Name<br/>
* Fuel_Type<br/>
* Transmission<br/>
* Owner_Type<br/>

### Feature and Target Separation

Input Features (X)<br/>

```python
X = data.drop("Price", axis=1)
```

Target Variable (Y)<br/>

```python
Y = data["Price"]
```

### Train-Test Split

The dataset was split into training and testing sets using train_test_split().<br/>
This helps evaluate the model on unseen data.<br/>

### Feature Scaling

Input features were standardized using StandardScaler().<br/>
Standardization improves model performance and ensures all features are on a similar scale.<br/>

---

## Model Training

The model was trained using Random Forest Regressor from Scikit-Learn.<br/>

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)
```

Random Forest was selected because it handles nonlinear relationships effectively and provides strong predictive performance for regression problems.<br/>

---

## Model Evaluation

Predictions were generated on the test dataset and evaluated using R² Score.<br/>
The R² Score was used to measure how well the model predicts car prices.<br/>
Additionally, graphs were plotted to visualize the relationship between actual and predicted prices and assess model performance visually.<br/>

---

## Model Serialization

To enable deployment and reuse without retraining, the following objects were saved as Pickle files:<br/>

* Trained Random Forest Model<br/>
* StandardScaler<br/>
* Name Encoder<br/>
* Fuel Type Encoder<br/>
* Transmission Encoder<br/>
* Owner Type Encoder<br/>

Example:<br/>

```python
import pickle

pickle.dump(model, open("model.pkl", "wb"))
```

---

## Backend Development

The backend was developed using FastAPI.<br/>

### Responsibilities

* Load trained model and preprocessing objects.<br/>
* Accept user input through API endpoints.<br/>
* Encode categorical values before prediction.<br/>
* Standardize numerical inputs using the saved scaler.<br/>
* Generate price predictions using the trained model.<br/>
* Return prediction results in JSON format.<br/>

FastAPI was chosen because it provides:<br/>

* High performance and speed.<br/>
* Automatic API documentation using Swagger UI.<br/>
* Easy integration with Machine Learning models.<br/>
* Asynchronous request handling capabilities.<br/>
* Scalable architecture for production deployment.<br/>

---

## Frontend Development

The frontend was built using HTML, CSS, and JavaScript.<br/>

### Features

* Responsive user interface.<br/>
* User-friendly form for entering vehicle details.<br/>
* Real-time communication with the FastAPI backend using Fetch API.<br/>
* Dynamic display of predicted car prices.<br/>
* Input validation for better user experience.<br/>
* Clean and modern design for easy interaction.<br/>

JavaScript collects user inputs from the form, sends them to the FastAPI prediction endpoint, receives the prediction response, and updates the webpage without requiring a page refresh.<br/>

---

## Technology Stack

### Machine Learning

* Python<br/>
* Pandas<br/>
* NumPy<br/>
* Scikit-Learn<br/>
* Matplotlib<br/>

### Backend

* FastAPI<br/>
* Uvicorn<br/>

### Frontend

* HTML<br/>
* CSS<br/>
* JavaScript<br/>

### Deployment & Serialization

* Pickle<br/>

---

## Project Workflow

1. Load Dataset<br/>
2. Clean and Preprocess Data<br/>
3. Encode Categorical Features<br/>
4. Split Data into Training and Testing Sets<br/>
5. Standardize Input Features<br/>
6. Train Random Forest Regressor<br/>
7. Evaluate Model Performance Using R² Score<br/>
8. Save Model, Encoders, and Scaler Using Pickle<br/>
9. Build FastAPI Backend APIs<br/>
10. Develop Interactive Frontend Interface<br/>
11. Connect Frontend with Backend Using Fetch API<br/>
12. Generate Real-Time Car Price Predictions<br/>
