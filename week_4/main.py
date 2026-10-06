import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

print(df)

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)

total_sales = df["Total_Sales"].sum() #for check total data in the dataset

print("Total Sales:", total_sales)

total_quantity = df["Quantity"].sum() #for check total quantity in the dataset

print("Total Quantity Sold:", total_quantity)

product_sales = df.groupby("Product")["Total_Sales"].sum() #find best selling product in the dataset

print(product_sales)


product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.show()

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("visualizations/sales_by_region.png")
plt.show()

product_quantity = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))

product_quantity.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity")

plt.tight_layout()
plt.savefig("visualizations/quantity_by_product.png")
plt.show()

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10, 5))

daily_sales.plot()

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("visualizations/daily_sales_trend.png")
plt.show()

