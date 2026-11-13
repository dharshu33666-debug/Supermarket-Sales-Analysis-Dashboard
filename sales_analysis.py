
import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================
# 1. PROJECT PATH
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

os.makedirs(STATIC_DIR, exist_ok=True)

# =====================================
# 2. LOAD CLEANED DATASET
# =====================================

cleaned_file = os.path.join(
    BASE_DIR, "supermarket_cleaned_dataset.csv"
)

original_file = os.path.join(
    BASE_DIR, "supermarket_large_dataset.csv"
)

file_path = cleaned_file if os.path.exists(cleaned_file) else original_file

df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# =====================================
# 3. DATA VALIDATION
# =====================================

required_columns = [
    "transaction_id",
    "basket_id",
    "product_id",
    "product_name",
    "product_category",
    "transaction_date",
    "sales_revenue",
    "units_sold",
    "gross_profit"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

df = df.drop_duplicates()

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"], errors="coerce"
)

# =====================================
# 4. SALES CALCULATIONS
# =====================================

total_revenue = df["sales_revenue"].sum()
total_profit = df["gross_profit"].sum()
total_units = df["units_sold"].sum()

total_orders = df["basket_id"].nunique()
total_customers = df["customer_id"].nunique()

average_order_value = (
    total_revenue / total_orders if total_orders else 0
)

print("\n===== SALES SUMMARY =====")

print("Total Sales Revenue:", round(total_revenue, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Units Sold:", total_units)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))

# =====================================
# 5. CATEGORY SALES ANALYSIS
# =====================================

category_sales = (
    df.groupby("product_category")["sales_revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== CATEGORY SALES =====")
print(category_sales)

plt.figure(figsize=(12, 6))
category_sales.plot(kind="bar")

plt.title("Sales Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(STATIC_DIR, "category_sales_chart.png")
)
plt.close()

# =====================================
# 6. MONTHLY SALES ANALYSIS
# =====================================

monthly_sales = (
    df.dropna(subset=["transaction_date"])
    .set_index("transaction_date")
    .resample("ME")["sales_revenue"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Revenue")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(STATIC_DIR, "monthly_sales_chart.png")
)
plt.close()

# =====================================
# 7. TOP 10 PRODUCTS ANALYSIS
# =====================================

top_products = (
    df.groupby(["product_id", "product_name"])["sales_revenue"]
    .sum()
    .reset_index()
    .sort_values("sales_revenue", ascending=False)
    .head(10)
)

print("\n===== TOP 10 PRODUCTS =====")
print(top_products)

plt.figure(figsize=(12, 6))

plt.bar(
    top_products["product_name"],
    top_products["sales_revenue"]
)

plt.title("Top 10 Products by Sales Revenue")
plt.xlabel("Product")
plt.ylabel("Sales Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(STATIC_DIR, "top_products_chart.png")
)
plt.close()

# =====================================
# 8. PROFIT ANALYSIS
# =====================================

category_profit = (
    df.groupby("product_category")["gross_profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
category_profit.plot(kind="bar")

plt.title("Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(STATIC_DIR, "profit_chart.png")
)
plt.close()

# =====================================
# 9. SALES REVENUE DISTRIBUTION
# =====================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["sales_revenue"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Sales Revenue Distribution")
plt.xlabel("Sales Revenue")
plt.ylabel("Number of Transactions")
plt.tight_layout()

plt.savefig(
    os.path.join(STATIC_DIR, "sales_revenue_chart.png")
)
plt.close()

# =====================================
# 10. EXPORT SALES SUMMARY
# =====================================

summary = pd.DataFrame({
    "Metric": [
        "Total Sales Revenue",
        "Total Profit",
        "Total Units Sold",
        "Total Orders",
        "Total Customers",
        "Average Order Value"
    ],
    "Value": [
        total_revenue,
        total_profit,
        total_units,
        total_orders,
        total_customers,
        average_order_value
    ]
})

summary.to_csv(
    os.path.join(BASE_DIR, "sales_summary.csv"),
    index=False
)

# =====================================
# 11. FINAL RESULT
# =====================================

print("\n================================")
print("SALES ANALYSIS COMPLETED")
print("================================")

print("Total Revenue:", round(total_revenue, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)

print("\nAll charts saved in static folder.")
print("Sales summary exported successfully.")
