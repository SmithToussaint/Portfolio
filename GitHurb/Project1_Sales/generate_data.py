import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_rows = 1000
products = ['Product A', 'Product B', 'Product C', 'Product D']
categories = ['Electronics', 'Furniture', 'Clothing', 'Groceries']
regions = ['North', 'South', 'East', 'West']

# Generate data
data = {
    'OrderID': range(1001, 1001 + n_rows),
    'Date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)],
    'Product': np.random.choice(products, n_rows),
    'Category': np.random.choice(categories, n_rows),
    'Region': np.random.choice(regions, n_rows),
    'Quantity': np.random.randint(1, 11, n_rows),
    'UnitPrice': np.round(np.random.uniform(10.0, 500.0, n_rows), 2)
}

df = pd.DataFrame(data)
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Cost'] = df['TotalSales'] * np.random.uniform(0.5, 0.8, n_rows)
df['Profit'] = df['TotalSales'] - df['Cost']

# Save to CSV
df.to_csv('c:/Users/touss/Desktop/GitHurb/Project1_Sales/sales_data.csv', index=False)
print("Data generated successfully at Project1_Sales/sales_data.csv")
