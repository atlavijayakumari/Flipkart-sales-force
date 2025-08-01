#step3
#EDA
import pandas as pd
import os
import matplotlib.pyplot as plt

# Load CSV data
df_csv = pd.read_csv('sample_sales_data.csv')
df_csv['Date'] = pd.to_datetime(df_csv['Date'], errors='coerce')

# Load JSON and Excel if files exist
df_json = pd.read_json('sample_sales_data.json') if os.path.exists('sample_sales_data.json') else pd.DataFrame()
df_excel = pd.read_excel('sample_sales_data.xlsx') if os.path.exists('sample_sales_data.xlsx') else pd.DataFrame()

# Convert 'Date' columns for JSON and Excel if present
for df in [df_json, df_excel]:
    if not df.empty and 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Combine all data
df_combined = pd.concat([df_csv, df_json, df_excel], ignore_index=True)

# Drop rows with missing Date or Revenue
df_combined = df_combined.dropna(subset=['Date', 'Revenue'])

# Add 'Month' column for monthly grouping
df_combined['Month'] = df_combined['Date'].dt.to_period('M')

# Monthly revenue aggregation
monthly_revenue = df_combined.groupby('Month')['Revenue'].sum()
print("Monthly Revenue:\n", monthly_revenue)

# Revenue by product
revenue_by_product = df_combined.groupby('Product')['Revenue'].sum()
print("\nRevenue by Product:\n", revenue_by_product)

# Units sold by product
units_by_product = df_combined.groupby('Product')['Units Sold'].sum()
print("\nUnits Sold by Product:\n", units_by_product)

# Plot monthly revenue
plt.figure(figsize=(8, 4))
monthly_revenue.plot(kind='bar', title='Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
