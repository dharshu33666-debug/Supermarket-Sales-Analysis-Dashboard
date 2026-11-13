
import pandas as pd
import os

# Project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load original dataset
file_path = os.path.join(
    BASE_DIR,
    "supermarket_large_dataset.csv"
)

df = pd.read_csv(file_path)

print("===== ORIGINAL DATASET =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Remove exact duplicate rows
df = df.drop_duplicates()

# Convert transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Convert important columns to numeric
numeric_columns = [
    "sales_revenue",
    "units_sold",
    "profit_per_unit",
    "profit_margin"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Check important columns
print("\n===== MISSING VALUES =====")
print(df[numeric_columns + ["transaction_date"]].isnull().sum())

# Validate essential sales data
df = df.dropna(
    subset=[
        "transaction_id",
        "basket_id",
        "sales_revenue",
        "units_sold",
        "transaction_date"
    ]
)

# Remove invalid sales records
df = df[
    (df["sales_revenue"] >= 0) &
    (df["units_sold"] > 0)
]

# Save cleaned dataset
output_path = os.path.join(
    BASE_DIR,
    "supermarket_cleaned_dataset.csv"
)

df.to_csv(output_path, index=False)

print("\n===== CLEANING COMPLETED =====")
print("Final Rows:", len(df))
print("Final Columns:", len(df.columns))
print("Saved:", output_path)
