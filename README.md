# Flight Price Prediction Model

This project implements a machine learning model to predict flight prices based on historical data. The model aims to provide accurate price estimates for different flights, helping users plan and book their travel efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Contributing](#contributing)


## Introduction

Travel planning often involves uncertainty in flight prices. This project addresses this issue by leveraging machine learning to predict flight prices. The model is trained on a dataset containing historical flight information, including features like departure and arrival locations, airline, departure time, etc.

## Dataset

The dataset used for training and testing the model can be found in the `data` directory. It includes various attributes such as:

- `Airline`
- `Source` (Departure location)
- `Destination` (Arrival location)
- `Departure Time`
- `Arrival Time`
- `Duration`
- `Total Stops`
- `Price` (Target variable)

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- Jupyter Notebook (for model training and evaluation)
- Pandas, NumPy, Scikit-learn (for data processing and machine learning)
- Matplotlib, Seaborn (for data visualization)

You can install the required packages using the following command:


`pip install -r requirements.txt`

## Clone repository
`git clone https://github.com/Mosee007/flight-prediction-model.git`

## Navigate to the project
`cd flight-prediction-model`

## Run Jupyter Notebook for model training
`Jupyter notebook fare_prediction_model.ipynb`

## Model Training
The fare_prediction_model.ipynb Jupyter Notebook contains the code for model training. It covers:

- Data loading and exploration
- Data preprocessing and feature engineering
- Model selection and training
- Model evaluation and validation

## Evaluation
- The model's performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. The evaluation results are discussed in the Jupyter Notebook.

## Results
- The trained model achieves a competitive performance in predicting flight prices. Users can input relevant details, and the model will provide an estimated flight price based on the historical patterns learned during training.

## Contributing
- If you would like to contribute to this project, please follow these steps:

##### Fork the repository.
- Create a new branch (git checkout -b feature/improvement).
- Make your changes and commit them (git commit -am 'Add feature/improvement').
- Push the changes to your branch (git push origin feature/improvement).
- Create a new pull request.


