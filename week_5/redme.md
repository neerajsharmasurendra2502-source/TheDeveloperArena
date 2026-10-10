# Customer Sales Analysis

**Week 5 Internship Project — The Developers Arena**

## Project Overview
This project uses Python and Pandas to explore sales transactions and customer churn data. It covers data cleaning, aggregation, filtering, date processing, pivot tables, visualizations, and reporting.

## Objectives
- Load and explore CSV datasets.
- Check missing values and duplicate records.
- Calculate sales summaries and group data by product, region, and month.
- Filter records using multiple conditions.
- Clean text and extract date parts.
- Create pivot tables and professional charts.
- Explore customer churn distribution.
- Document findings and business recommendations.

## Datasets

### `sales_data.csv`
Visible columns: `Date`, `Product`, `Quantity`, `Price`, `Customer_ID`, `Region`, `Total_Sales`.

### `customer_churn.csv`
Visible columns: `CustomerID`, `Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `PaperlessBilling`, `SeniorCitizen`, `Churn`.

**Data note:** Verify that the customer identifiers correspond to the same population before merging. Do not assume `Customer_ID` and `CustomerID` are equivalent.

## Tools
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure
```text
week_5/
├── customer_analysis.ipynb
├── sales_data.csv
├── customer_churn.csv
├── README.md
├── requirements.txt
├── analysis_report.pdf
└── charts/
    ├── 01_monthly_sales_trend.png
    ├── 02_revenue_by_product.png
    ├── 03_sales_by_region.png
    ├── 04_quantity_by_product.png
    └── 05_customer_churn_distribution.png
```
The `charts/` images appear after the notebook chart cells run successfully.

## Installation
Run in the project terminal:
```bash
python -m pip install -r requirements.txt
```

## How to Run
1. Open `customer_analysis.ipynb` in VS Code.
2. Select the Python/Jupyter kernel.
3. Keep the required CSV files in the notebook's project folder.
4. Run the cells in order.
5. Review the outputs and generated charts.
6. Update `analysis_report.pdf` with actual findings before submission.

## Planned Charts
1. Monthly Sales Performance
2. Revenue by Product
3. Regional Sales Performance
4. Product Demand Analysis
5. Customer Churn Distribution

## Reporting Guidelines
Use values calculated from the supplied datasets. Do not present sample numbers from the internship website as actual findings. Verify the meaning of churn values before interpreting them. Product-pair analysis requires order-level and item-level data.

## Deliverables
- `customer_analysis.ipynb`
- Required CSV datasets
- `requirements.txt`
- `README.md`
- `analysis_report.pdf`
- Charts, if required by the internship submission instructions
