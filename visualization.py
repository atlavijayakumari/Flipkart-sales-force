#step4
#Visualization
import pandas as pd
# Load data
df = pd.read_csv('sample_sales_data.csv')

# Display basic info
print("First few rows of the dataset:")
print(df.head())

# Total revenue
print("Total revenue generated:", df['Revenue'].sum())
#📈 Total Units Sold
print("Total units sold:", df['Units Sold'].sum())
# 📊 Revenue by Product
print("Revenue by product:")
print(df.groupby('Product')['Revenue'].sum())

#visualizing the tabular
import matplotlib.pyplot as plt

df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to actual dates
plt.plot(df['Date'], df['Revenue'], marker='o')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()



