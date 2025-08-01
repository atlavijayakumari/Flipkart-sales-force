#step3
#EDA
import pandas as pd

# Example CSV loading (you must also load JSON and Excel in full script)
df_csv = pd.read_csv('sample_sales_data.csv')
df_csv['Date'] = pd.to_datetime(df_csv['Date'], errors='coerce')

# Optional: load JSON and Excel if you have them
df_json = pd.DataFrame()  # Empty placeholder
df_excel = pd.DataFrame()  # Empty placeholder

# Combine
df_combined = pd.concat([df_csv, df_json, df_excel], ignore_index=True)

# Now add 'Month' column and do monthly revenue analysis
df_combined['Month'] = df_combined['Date'].dt.to_period('M')
monthly_revenue = df_combined.groupby('Month')['Revenue'].sum()

print(monthly_revenue)
