# Flight Price Prediction Model

This project implements a machine learning model to predict flight prices based on historical data. The model aims to provide accurate price estimates for different flights, helping users plan and book their travel efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)


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

```bash
pip install -r requirements.txt

