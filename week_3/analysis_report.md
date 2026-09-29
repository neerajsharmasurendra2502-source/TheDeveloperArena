# Sales Data Analysis Report

## 1. Introduction

This project analyzes a sales dataset using Python and the Pandas library.

The purpose of this project is to understand basic data analysis operations such as loading data, exploring the dataset, checking missing values, handling missing values, and calculating simple statistics.

## 2. Dataset

The dataset used in this project is:

`sales_data.csv`

The dataset contains the following columns:

- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

## 3. Tools and Technologies

- Python
- Pandas
- VS Code
- CSV Dataset

## 4. Loading the Dataset

The dataset was loaded using Pandas:

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")