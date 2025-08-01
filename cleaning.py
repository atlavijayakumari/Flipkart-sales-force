#step1
#to cleaning
#to check the duplicates
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sample_sales_data.csv')

# Step 1: Clean the data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Product'] = df['Product'].str.strip().str.title()
print("Missing values:\n", df.isnull().sum())
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("\nCleaned data preview:")
print(df.head())