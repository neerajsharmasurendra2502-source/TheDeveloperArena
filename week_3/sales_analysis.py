import pandas as pd

# 1. Load the dataset
df = pd.read_csv("sales_data.csv")

# 2. Display first few rows
print("----- FIRST 5 ROWS -----")
print(df.head())

# 3. Basic information
print("\n----- NUMBER OF ROWS AND COLUMNS -----")
print(df.shape)

print("\n----- DATA TYPES -----")
print(df.dtypes)

print("\n----- BASIC INFORMATION -----")
df.info()

# 4. Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# 5. Handle missing values
# For numerical columns, fill missing values with the mean
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

print("\n----- MISSING VALUES AFTER HANDLING -----")
print(df.isnull().sum())

# 6. Calculate average, highest and lowest values
print("\n----- NUMERICAL COLUMN STATISTICS -----")

for column in numeric_columns:
    print("\nColumn:", column)
    print("Average:", df[column].mean())
    print("Highest:", df[column].max())
    print("Lowest:", df[column].min())