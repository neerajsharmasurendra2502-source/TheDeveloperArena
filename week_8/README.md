# Customer Churn Analysis — Week 8 Capstone

## Project overview
This project analyses the supplied customer churn dataset to understand customer attrition patterns and develop practical retention recommendations. It is prepared for the Week 8 Capstone Project: Real World Business Analysis at The Developers Arena.

## Business problem
The business wants to understand which customer groups are more likely to leave and how customer retention can be improved through data-driven actions.

## Dataset
- File: `customer_churn.csv` (place the supplied file in `data/`)
- Records: **500**
- Columns: **9**
- Missing cells detected in the source file: **0**
- Duplicate rows detected in the source file: **0**

### Available fields
- `CustomerID` — object
- `Tenure` — int64
- `MonthlyCharges` — int64
- `TotalCharges` — int64
- `Contract` — object
- `PaymentMethod` — object
- `PaperlessBilling` — object
- `SeniorCitizen` — int64
- `Churn` — int64

## Tools and technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- scikit-learn (optional predictive modelling)

## Project structure
```text
Week8_Customer_Churn_Analysis/
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_exploratory_analysis.ipynb
│   └── 3_advanced_analysis.ipynb
├── visuals/
├── reports/
│   ├── executive_summary.pdf
│   └── technical_report.pdf
├── presentation/
│   └── business_presentation.pptx
├── requirements.txt
└── README.md
```

## Setup
1. Install Python 3.10 or later.
2. Open a terminal in the project directory.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Place the source CSV at `data/raw_data.csv`.
5. Launch Jupyter:

```bash
jupyter notebook
```

6. Run notebooks in order: data cleaning, exploratory analysis, then advanced analysis.

## Analysis plan
1. Inspect data shape, columns, types, missing values and duplicates.
2. Create a separate cleaned dataset while preserving the raw file.
3. Calculate churn and retention metrics.
4. Compare churn across available customer segments.
5. Visualise distributions and relationships.
6. If appropriate, build a logistic-regression baseline and evaluate precision, recall, F1-score and confusion matrix.
7. Translate validated findings into retention recommendations.

## Preliminary result
- Churned customers in the supplied sample: **53**\n- Retained customers in the supplied sample: **447**\n- Observed churn rate: **10.6%**\n
## Business recommendations to validate
- Target customer segments with higher observed churn for tailored outreach.
- Review onboarding and early-tenure experience.
- Investigate contract and payment experiences.
- Run controlled retention pilots and measure incremental impact before scaling.

## Limitations
The dataset is a limited sample. Segment differences are descriptive, not proof of causation. Confirm data definitions, time period, currency and business context with the data owner. Model performance should be assessed using class-specific metrics, not accuracy alone.

## Deliverables
- `reports/executive_summary.pdf`
- `reports/technical_report.pdf`
- `presentation/business_presentation.pptx`
- Analysis notebooks and generated visualisations

## Author
Prepared as an internship capstone project. Add your name, internship details, GitHub URL and project date before publishing.
