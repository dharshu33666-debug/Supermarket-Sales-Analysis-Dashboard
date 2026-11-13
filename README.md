# Supermarket Sales Analysis Dashboard

## 📌 Project Overview

The **Supermarket Sales Analysis Dashboard** is a data analysis and visualization project developed using Python, Pandas, Flask, HTML, CSS, JavaScript, and Chart.js.

This project uses a supermarket sales dataset downloaded from Kaggle. The dataset is cleaned, processed, and analyzed to identify important business metrics, including sales revenue, gross profit, orders, customers, and product category performance.

An interactive web dashboard presents the analysis results through summary cards and graphical visualizations, helping users understand supermarket business performance.

## 🎯 Project Objectives

- Analyze supermarket sales data.
- Calculate total sales revenue and gross profit.
- Identify the total number of orders and customers.
- Analyze product category sales performance.
- Visualize monthly sales and profit trends.
- Present key business metrics through an interactive dashboard.
- Generate meaningful business insights from the dataset.

## 📊 Dataset

- **Dataset Source:** [Kaggle – Supermarket Dataset](https://www.kaggle.com/datasets/datascikhan/supermarket)
- **Dataset File:** `supermarket_large_dataset.csv`
- **File Format:** CSV

The dataset contains detailed supermarket information, including customer details, products, transactions, sales, profit, inventory, and other business-related attributes.

**Note:** The original and cleaned CSV files are not included in this GitHub repository because of their large file sizes. Download the dataset from Kaggle and place the required CSV files in the project folder before running the application.

## 🛠️ Technologies Used

- **Python** – Programming and data processing
- **Pandas** – Data cleaning and analysis
- **Flask** – Web application framework
- **Matplotlib** – Data visualization
- **HTML** – Dashboard structure
- **CSS** – Dashboard styling
- **JavaScript** – Interactive functionality
- **Chart.js** – Interactive charts
- **CSV** – Dataset storage

## ✨ Key Features

1. **Total Sales Revenue** – Displays the total sales revenue.
2. **Total Gross Profit** – Shows the total gross profit generated.
3. **Total Orders** – Displays the total number of orders.
4. **Total Customers** – Shows the number of customers.
5. **Product Category Analysis** – Compares sales across product categories.
6. **Monthly Sales Analysis** – Visualizes monthly sales performance.
7. **Profit Analysis** – Presents profit information through charts.
8. **Top Products Analysis** – Highlights top-performing products.
9. **Interactive Dashboard** – Displays business metrics and visualizations in a user-friendly interface.

## 📈 Key Business Insights

The analysis generated the following results:

| Business Metric | Result |
|---|---:|
| Total Sales Revenue | ₹9,995,644.58 |
| Total Gross Profit | ₹3,770,441.83 |
| Total Orders | 45,500 |
| Total Customers | 75,799 |
| Units Sold | 1,021,188 |

**Top Sales Category:** Grocery – ₹506,229.87

*Note: These are results from the dataset used in this project.*

## 📂 Project Structure

```text
Supermarket-Sales-Analysis/
│
├── app.py
├── data_cleaning.py
├── sales_analysis.py
├── sales_summary.csv
├── README.md
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── category_sales_chart.png
    ├── monthly_sales_chart.png
    ├── profit_chart.png
    ├── sales_revenue_chart.png
    └── top_products_chart.png
```

**Note:** The large original and cleaned dataset CSV files are stored locally and excluded from GitHub using `.gitignore`.

## ⚙️ Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the Repository

```bash
git clone https://github.com/dharshu33666-debug/Supermarket-Sales-Analysis.git
```

Navigate to the project directory:

```bash
cd Supermarket-Sales-Analysis
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Download the Dataset

Download the dataset from:

[https://www.kaggle.com/datasets/datascikhan/supermarket](https://www.kaggle.com/datasets/datascikhan/supermarket)

Place the required CSV files in the project directory. Use the filenames expected by the Python scripts:

- `supermarket_large_dataset.csv`
- `supermarket_cleaned_dataset.csv`

Run the data cleaning script if you need to generate the cleaned dataset:

```bash
python data_cleaning.py
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open the Dashboard

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 📊 Data Analysis Process

1. Import the supermarket dataset using Pandas.
2. Inspect the dataset and understand its columns.
3. Clean and prepare the data.
4. Analyze sales and profit information.
5. Calculate total revenue, gross profit, and orders.
6. Analyze product category performance.
7. Generate monthly sales and profit visualizations.
8. Identify important business insights.
9. Display the results through a Flask dashboard.

## 💡 Project Benefits

- Makes supermarket sales data easier to understand.
- Helps analyze sales and profit performance.
- Identifies top-performing product categories.
- Presents key business metrics in one dashboard.
- Demonstrates practical data analysis skills.
- Provides experience in Python-based dashboard development.

## 🎓 Skills Demonstrated

- Python Programming
- Data Analysis
- Data Cleaning
- Pandas
- Exploratory Data Analysis (EDA)
- Data Visualization
- Flask Web Development
- HTML and CSS
- JavaScript
- Chart.js
- Working with CSV Datasets
- Git and GitHub

## 🚀 Future Enhancements

- Add interactive date filters.
- Introduce product category comparisons.
- Add monthly and yearly sales analysis.
- Include customer segmentation analysis.
- Add downloadable reports.
- Improve dashboard responsiveness.
- Deploy the application online.

## 🏁 Conclusion

The Supermarket Sales Analysis Dashboard demonstrates how Python, Pandas, and visualization tools can be used to analyze supermarket sales data and present meaningful business insights through an interactive web application.

This project provides practical experience in data cleaning, exploratory data analysis, visualization, and dashboard development.

## 👩‍💻 Author

Developed as a **Supermarket Sales Analysis** project.

**GitHub Repository:**  
https://github.com/dharshu33666-debug/Supermarket-Sales-Analysis

**Dataset Source:**  
https://www.kaggle.com/datasets/datascikhan/supermarket
