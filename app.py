
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cleaned_file = os.path.join(
    BASE_DIR, "supermarket_cleaned_dataset.csv"
)

original_file = os.path.join(
    BASE_DIR, "supermarket_large_dataset.csv"
)

CSV_FILE = (
    cleaned_file
    if os.path.exists(cleaned_file)
    else original_file
)


@app.route("/")
def home():
    try:
        # Load dataset
        df = pd.read_csv(CSV_FILE)

        # Check required columns
        required_columns = [
            "sales_revenue",
            "units_sold",
            "profit_per_unit",
            "product_category",
            "basket_id",
            "transaction_date"
        ]

        missing = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing:
            return (
                "Missing CSV columns: " + ", ".join(missing),
                500
            )

        # Convert numeric columns
        numeric_columns = [
            "sales_revenue",
            "units_sold",
            "profit_per_unit"
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(
                df[col], errors="coerce"
            )

        # Clean required data
        df = df.dropna(
            subset=[
                "sales_revenue",
                "units_sold",
                "profit_per_unit",
                "product_category",
                "basket_id"
            ]
        ).copy()

        # Calculate gross profit
        if "gross_profit" in df.columns:
            df["gross_profit"] = pd.to_numeric(
                df["gross_profit"], errors="coerce"
            )
        else:
            df["gross_profit"] = (
                df["profit_per_unit"] * df["units_sold"]
            )

        df = df.dropna(subset=["gross_profit"]).copy()

        # --------------------------------
        # SALES OVERVIEW
        # --------------------------------

        total_sales = round(
            float(df["sales_revenue"].sum()), 2
        )

        total_units = int(df["units_sold"].sum())

        total_profit = round(
            float(df["gross_profit"].sum()), 2
        )

        total_records = int(len(df))

        total_orders = int(
            df["basket_id"].nunique()
        )

        profit_margin = (
            round((total_profit / total_sales) * 100, 2)
            if total_sales != 0 else 0
        )

        # --------------------------------
        # CATEGORY-WISE SALES
        # --------------------------------

        category_sales = (
            df.groupby("product_category")["sales_revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        chart_labels = category_sales.index.tolist()

        chart_values = [
            round(float(value), 2)
            for value in category_sales.values
        ]

        # --------------------------------
        # CATEGORY-WISE PROFIT
        # --------------------------------

        category_profit = (
            df.groupby("product_category")["gross_profit"]
            .sum()
            .reindex(category_sales.index)
        )

        profit_values = [
            round(float(value), 2)
            for value in category_profit.values
        ]

        # --------------------------------
        # MONTHLY SALES ANALYSIS
        # --------------------------------

        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"],
            errors="coerce"
        )

        monthly_sales = (
            df.dropna(subset=["transaction_date"])
            .set_index("transaction_date")
            .resample("ME")["sales_revenue"]
            .sum()
        )

        monthly_labels = (
            monthly_sales.index.strftime("%b %Y").tolist()
        )

        monthly_values = [
            round(float(value), 2)
            for value in monthly_sales.values
        ]

        # --------------------------------
        # CUSTOMER ANALYSIS
        # --------------------------------

        total_customers = 0

        gender_labels = []
        gender_values = []

        age_labels = []
        age_values = []

        segment_labels = []
        segment_values = []

        top_customer_labels = []
        top_customer_values = []

        # Check customer ID column
        if "customer_id" in df.columns:

            customer_data = df.dropna(
                subset=["customer_id"]
            ).copy()

            total_customers = int(
                customer_data["customer_id"].nunique()
            )

            # One row per customer for demographic analysis
            unique_customers = (
                customer_data
                .drop_duplicates(subset=["customer_id"])
                .copy()
            )

            # --------------------------------
            # GENDER-WISE CUSTOMER ANALYSIS
            # --------------------------------

            if "customer_gender" in unique_customers.columns:

                gender_data = unique_customers.dropna(
                    subset=["customer_gender"]
                )

                gender_summary = (
                    gender_data
                    .groupby("customer_gender")["customer_id"]
                    .nunique()
                    .sort_values(ascending=False)
                )

                gender_labels = [
                    str(value)
                    for value in gender_summary.index.tolist()
                ]

                gender_values = [
                    int(value)
                    for value in gender_summary.values
                ]

            # --------------------------------
            # AGE GROUP-WISE CUSTOMER ANALYSIS
            # --------------------------------

            if "customer_age" in unique_customers.columns:

                unique_customers["customer_age"] = pd.to_numeric(
                    unique_customers["customer_age"],
                    errors="coerce"
                )

                age_data = unique_customers.dropna(
                    subset=["customer_age"]
                ).copy()

                age_data = age_data[
                    age_data["customer_age"] >= 18
                ]

                age_data["age_group"] = pd.cut(
                    age_data["customer_age"],
                    bins=[17, 25, 35, 45, 55, 65, float("inf")],
                    labels=[
                        "18-25",
                        "26-35",
                        "36-45",
                        "46-55",
                        "56-65",
                        "66+"
                    ]
                )

                age_summary = (
                    age_data["age_group"]
                    .value_counts(sort=False)
                )

                age_labels = [
                    str(value)
                    for value in age_summary.index.tolist()
                ]

                age_values = [
                    int(value)
                    for value in age_summary.values
                ]

            # --------------------------------
            # CUSTOMER SEGMENT ANALYSIS
            # --------------------------------

            if "customer_segment" in unique_customers.columns:

                segment_data = unique_customers.dropna(
                    subset=["customer_segment"]
                )

                segment_summary = (
                    segment_data
                    .groupby("customer_segment")["customer_id"]
                    .nunique()
                    .sort_values(ascending=False)
                )

                segment_labels = [
                    str(value)
                    for value in segment_summary.index.tolist()
                ]

                segment_values = [
                    int(value)
                    for value in segment_summary.values
                ]

            # --------------------------------
            # TOP 10 CUSTOMERS BY SALES
            # --------------------------------

            top_customers = (
                customer_data
                .groupby("customer_id")["sales_revenue"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
            )

            top_customer_labels = [
                str(value)
                for value in top_customers.index.tolist()
            ]

            top_customer_values = [
                round(float(value), 2)
                for value in top_customers.values
            ]

        # --------------------------------
        # SEND DATA TO DASHBOARD
        # --------------------------------

        return render_template(
            "index.html",

            # Sales overview
            total_sales=total_sales,
            total_units=total_units,
            total_profit=total_profit,
            total_records=total_records,
            total_orders=total_orders,
            profit_margin=profit_margin,

            # Category analysis
            chart_labels=chart_labels,
            chart_values=chart_values,
            profit_values=profit_values,

            # Monthly analysis
            monthly_labels=monthly_labels,
            monthly_values=monthly_values,

            # Customer analysis
            total_customers=total_customers,
            gender_labels=gender_labels,
            gender_values=gender_values,
            age_labels=age_labels,
            age_values=age_values,
            segment_labels=segment_labels,
            segment_values=segment_values,
            top_customer_labels=top_customer_labels,
            top_customer_values=top_customer_values
        )

    except FileNotFoundError:
        return (
            "CSV file not found. Check the dataset file name.",
            404
        )

    except Exception as error:
        return f"Error loading dashboard: {error}", 500


if __name__ == "__main__":
    app.run(debug=True)
