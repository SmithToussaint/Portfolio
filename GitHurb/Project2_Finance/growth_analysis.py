import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('c:/Users/touss/Desktop/GitHurb/Project2_Finance/financial_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Calculate YoY Growth
df['Year'] = df['Date'].dt.year
yearly_stats = df.groupby('Year')[['Revenue', 'Profit']].sum()
yearly_stats['Revenue_Growth'] = yearly_stats['Revenue'].pct_change() * 100

# Budget vs Actual
df['Variance'] = df['Revenue'] - df['Budget']

# Visualizations
sns.set_theme(style="darkgrid")

# 1. Revenue vs Expenses vs Budget
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Revenue'], label='Actual Revenue', marker='o')
plt.plot(df['Date'], df['Expenses'], label='Actual Expenses', marker='s')
plt.plot(df['Date'], df['Budget'], label='Budgeted Revenue', linestyle='--')
plt.title('Monthly Financial Performance (2022-2023)')
plt.legend()
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project2_Finance/performance_chart.png')

# 2. Profit Margin over Time
plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='Date', y='ProfitMargin', color='green')
plt.title('Profit Margin Trend (%)')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project2_Finance/profit_margin_trend.png')

print("Financial analysis completed. Charts saved in Project2_Finance/")
print("\nYearly Revenue Growth:")
print(yearly_stats[['Revenue', 'Revenue_Growth']])
