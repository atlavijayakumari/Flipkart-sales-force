#step2
#integration
import os
import pandas as pd

# Define file paths
csv_file = 'sample_sales_data.csv'
json_file = 'sample_sales_data.json'
excel_file = 'sample_sales_data.xlsx'

# Function to safely load files
def load_data(file_path, loader_func):
    if os.path.exists(file_path):
        print(f"✅ Loaded: {file_path}")
        return loader_func(file_path)
    else:
        print(f"⚠️ File not found: {file_path}")
        return pd.DataFrame()  # return empty DataFrame if file not found

# Load each file format
df_csv = load_data(csv_file, pd.read_csv)
df_json = load_data(json_file, pd.read_json)
df_excel = load_data(excel_file, pd.read_excel)

# Clean data: function to clean any DataFrame
def clean(df):
    if df.empty:
        return df
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Product'] = df['Product'].astype(str).str.strip().str.title()
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

# Clean all loaded data
df_csv = clean(df_csv)
df_json = clean(df_json)
df_excel = clean(df_excel)

# Combine all datasets into one
df_combined = pd.concat([df_csv, df_json, df_excel], ignore_index=True)

# Final combined check
print("\n✅ Combined Data Preview:")
print(df_combined.head())

print("\n📊 Total rows:", len(df_combined))
print("📦 Total Units Sold:", df_combined['Units Sold'].sum())
print("💰 Total Revenue:", df_combined['Revenue'].sum())
print("\n📈 Revenue by Product:")
print(df_combined.groupby('Product')['Revenue'].sum())
