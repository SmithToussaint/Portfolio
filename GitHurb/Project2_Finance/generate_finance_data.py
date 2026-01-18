import pandas as pd
import numpy as np
import datetime

# Set seed
np.random.seed(88)

# Generate data for 2 years (2022 and 2023)
dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='M')
n_months = len(dates)

data = {
    'Date': dates,
    'Revenue': np.random.uniform(50000, 150000, n_months),
    'Expenses': np.random.uniform(30000, 100000, n_months),
    'Budget': np.random.uniform(45000, 140000, n_months)
}

df = pd.DataFrame(data)

# Add some seasonal variance for "realism" (higher revenue in December)
df.loc[df['Date'].dt.month == 12, 'Revenue'] *= 1.4

df['Profit'] = df['Revenue'] - df['Expenses']
df['ProfitMargin'] = (df['Profit'] / df['Revenue']) * 100

# Save to CSV
df.to_csv('c:/Users/touss/Desktop/GitHurb/Project2_Finance/financial_data.csv', index=False)
print("Financial data generated at Project2_Finance/financial_data.csv")
