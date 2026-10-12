
from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# -------------------------------
# 1. Project configuration
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
OUTPUT_DIR = BASE_DIR / "visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid", palette="deep")

# -------------------------------
# 2. Load and validate data
# -------------------------------
df = pd.read_csv(DATA_FILE)

required_columns = [
    "Date", "Product", "Quantity", "Price",
    "Customer_ID", "Region", "Total_Sales"
]

missing_columns = set(required_columns) - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Missing required columns: {sorted(missing_columns)}"
    )

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for col in ["Quantity", "Price", "Total_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=required_columns).copy()
df = df.sort_values("Date")

if df.empty:
    raise ValueError("No valid rows remain after data cleaning.")

# -------------------------------
# 3. Calculate key metrics
# -------------------------------
total_sales = df["Total_Sales"].sum()
total_units = df["Quantity"].sum()
total_orders = len(df)
unique_customers = df["Customer_ID"].nunique()

print("\n========== SALES SUMMARY ==========")
print(f"Total Sales:      {total_sales:,.2f}")
print(f"Total Units Sold: {total_units:,.0f}")
print(f"Total Records:    {total_orders:,}")
print(f"Unique Customers: {unique_customers:,}")
print("\nSales by Region:")
print(df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False))

# -------------------------------
# 4. Chart 1: Sales by product
# -------------------------------
product_sales = (
    df.groupby("Product", as_index=False)["Total_Sales"]
    .sum()
    .sort_values("Total_Sales", ascending=False)
)

plt.figure(figsize=(10, 6))
sns.barplot(data=product_sales, x="Product", y="Total_Sales")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_sales_by_product.png", dpi=300)
plt.close()

# -------------------------------
# 5. Chart 2: Daily sales trend
# -------------------------------
daily_sales = (
    df.groupby("Date", as_index=False)["Total_Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
sns.lineplot(
    data=daily_sales,
    x="Date",
    y="Total_Sales",
    marker="o"
)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_daily_sales_trend.png", dpi=300)
plt.close()

# -------------------------------
# 6. Chart 3: Sales distribution
# -------------------------------
plt.figure(figsize=(9, 6))
sns.boxplot(data=df, x="Product", y="Total_Sales")
plt.title("Sales Distribution by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_sales_boxplot.png", dpi=300)
plt.close()

# -------------------------------
# 7. Chart 4: Correlation heatmap
# -------------------------------
numeric_data = df[["Quantity", "Price", "Total_Sales"]]
correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Between Sales Variables")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_correlation_heatmap.png", dpi=300)
plt.close()

# -------------------------------
# 8. Chart 5: Interactive regional sales
# -------------------------------
region_sales = (
    df.groupby("Region", as_index=False)
    .agg(
        Total_Sales=("Total_Sales", "sum"),
        Units_Sold=("Quantity", "sum"),
        Customers=("Customer_ID", "nunique")
    )
)

fig = px.bar(
    region_sales,
    x="Region",
    y="Total_Sales",
    color="Region",
    hover_data=["Units_Sold", "Customers"],
    title="Interactive Sales by Region",
    labels={"Total_Sales": "Total Sales"}
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5
)

fig.write_html(
    str(OUTPUT_DIR / "05_interactive_region_sales.html")
)

# -------------------------------
# 9. Interactive product chart
# -------------------------------
fig2 = px.scatter(
    df,
    x="Quantity",
    y="Total_Sales",
    color="Product",
    hover_data=["Date", "Region", "Customer_ID", "Price"],
    title="Interactive Quantity vs Total Sales"
)

fig2.update_layout(template="plotly_white", title_x=0.5)
fig2.write_html(
    str(OUTPUT_DIR / "06_interactive_sales_scatter.html")
)

# -------------------------------
# 10. Save a cleaned dataset
# -------------------------------
df.to_csv(OUTPUT_DIR / "cleaned_sales_data.csv", index=False)

print("\nDashboard charts generated successfully!")
print(f"Saved files in: {OUTPUT_DIR}")
