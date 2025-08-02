Vijaya kumari Atla
Sat, Aug 2, 10:28 AM 
to me

📝 Final Report – Flipkart Sales Data Analysis Project


---

🛒 Project Title:

Multi-Source Sales Data Pipeline & Business Insights Dashboard


---

🎯 Objective:

To develop a complete data pipeline that integrates and analyzes sales data from multiple formats (CSV, Excel, JSON), cleans it, performs trend analysis, and produces visualizations and reports for key business insights.


---

🧰 Tools & Libraries Used:

Python: Data handling and scripting

pandas: Data cleaning, merging, aggregation

numpy: Numerical operations

matplotlib & seaborn: Data visualizations

pdfkit, tabulate (optional): Exporting reports

Jupyter Notebook / VS Code: Code development environment

Git & GitHub: Version control and submission



---

📂 Data Sources Used:

sample_sales_data.csv: Provided by Flipkart

---


🧹 Data Cleaning Summary:

Converted Date column to proper datetime format.

Filled or removed missing values.

Standardized column names and product strings.

Added new columns for Month and Revenue analysis.



---


🔗 Data Integration:

Merged and combined files from different formats (if applicable).

Unified schema across all data files.

Created a master dataframe for analysis.



---

📊 Exploratory Data Analysis (EDA):

Total Revenue Generated: ₹255 (based on example)

Monthly Revenue Trends

Top Performing Products

Sales Volume vs. Revenue


Sample Code Used:

df.groupby('Product')['Revenue'].sum()
df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()


---


📈 Visualizations Created:

📊 Bar Chart: Revenue by Product

📉 Line Plot: Monthly Revenue Trend

All visualizations saved in the outputs/ folder


---


🧾 Reports Generated:

Report File Description

product_revenue.csv Revenue by product
monthly_revenue.csv Monthly revenue


---

💻 How to Run This Project:

1. Install required libraries:

pip install pandas matplotlib seaborn


2. Run the script in terminal or Jupyter:

python sales_analysis.py


3. Outputs will be saved inside the outputs/ folder



---


📷 Screenshots:

Include your graphs

Show your CSV file previews

Optional: include your df.head() output



---


📌 Key Business Insights:

Widget A generated the highest revenue in January 2025.

Revenue growth trend can be analyzed monthly.

Useful for inventory or marketing decisions.



---

👩‍💻 Author & Internship Info:

Atla Vijaya Kumari
Flipkart Data Science Intern – 2025

