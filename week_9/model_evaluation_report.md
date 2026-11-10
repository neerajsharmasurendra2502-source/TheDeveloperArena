# House Price Prediction – Model Evaluation Report

## 1. Introduction

The objective of this project is to develop a machine learning model that predicts house prices based on property characteristics such as area, bedrooms, bathrooms, age, location and property type.

## 2. Dataset Description

- Total records: 300
- Total columns: 8
- Missing values: 0
- Target variable: Price
- Input features: Area, Bedrooms, Bathrooms, Age, Location and Property_Type

Property_ID was excluded from model training because it is a unique identifier.

## 3. Data Preprocessing

- Checked missing values and duplicate records.
- Separated input features and target variable.
- Encoded categorical features using One-Hot Encoding.
- Divided the dataset into 80% training and 20% testing data.

## 4. Algorithms Used

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

## 5. Model Evaluation

| Model | MAE | R² Score |
|---|---:|---:|
| Linear Regression | 2,188,736.34 | 0.9406 |
| Decision Tree | 2,194,416.67 | 0.9424 |
| Random Forest | 1,482,103.13 | 0.9727 |

The Random Forest model achieved the best performance among the three tested models.

## 6. Evaluation Metrics

- MAE measures the average absolute difference between actual and predicted prices.
- MSE measures the average squared prediction error.
- RMSE measures prediction error in the same units as the target.
- R² measures the proportion of price variation explained by the model.

## 7. Results and Interpretation

The Random Forest Regressor achieved an R² score of approximately 0.9727 on the test dataset. It performed better than Linear Regression and Decision Tree in this experiment.

The actual-versus-predicted visualization helps assess how closely the model predictions match actual prices.

## 8. Conclusion

This project demonstrates how machine learning can be applied to house price prediction. Different regression algorithms were trained and evaluated. Random Forest produced the best test performance in this experiment.

## 9. Tools and Technologies

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn and Jupyter Notebook.
:::Important: The report figures above correspond to the results from your supplied CSV and the specified settings. If your own notebook produces different numbers, update the report to match your actual notebook output.