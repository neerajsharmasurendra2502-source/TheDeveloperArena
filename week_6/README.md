# Interactive Sales Dashboard

## Project Overview
This project analyzes sales transaction data and presents business insights through statistical visualizations and an interactive Plotly chart.

## Objectives
- Analyze monthly sales trends.
- Compare revenue across products and regions.
- Understand product price distributions.
- Explore correlations between numerical variables.
- Display important sales KPIs.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## Project Structure
```text
week_6/
├── visualizations/
├── dashboard.py
├── dashboard.ipynb
├── requirements.txt
├── README.md
└── sales_data.csv
```

The `visualizations/` folder also contains the generated charts and sales summary CSV files.

## Installation
1. Install Python.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment.
4. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## How to Run
Run the main dashboard:

```bash
python dashboard.py
```

Open `dashboard.ipynb` in VS Code and run its cells to explore the analysis.

## Visualizations
1. Monthly sales trend.
2. Revenue by product.
3. Revenue by region.
4. Product price distribution.
5. Numerical correlation heatmap.
6. Interactive Plotly sales chart.

## Key Performance Indicators
- Total revenue
- Units sold
- Number of transactions
- Unique customers
- Average transaction value

Actual KPI values are generated from the supplied dataset when the program runs.

## Output
The program saves the static dashboard, interactive HTML chart, and product and region sales summaries in the `visualizations/` directory.

## Conclusion
This project demonstrates basic data preparation, exploratory data analysis, statistical visualization, and interactive business reporting using Python.

*Note: Findings and conclusions should be updated after inspecting the actual dataset results.*