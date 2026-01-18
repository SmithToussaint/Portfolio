import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('c:/Users/touss/Desktop/GitHurb/Project1_Sales/sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 1. Sales by Category
plt.figure()
sns.barplot(data=df.groupby('Category')['TotalSales'].sum().reset_index(), x='Category', y='TotalSales', palette='viridis')
plt.title('Total Sales by Category', fontsize=16)
plt.ylabel('Sales ($)')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project1_Sales/sales_by_category.png')

# 2. Sales Trend Over Time
plt.figure()
monthly_sales = df.resample('M', on='Date')['TotalSales'].sum().reset_index()
sns.lineplot(data=monthly_sales, x='Date', y='TotalSales', marker='o', color='b')
plt.title('Monthly Sales Trend (2023)', fontsize=16)
plt.ylabel('Sales ($)')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project1_Sales/sales_trend.png')

# 3. Regional Distribution (Pie Chart)
plt.figure()
region_sales = df.groupby('Region')['TotalSales'].sum()
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Sales Distribution by Region', fontsize=16)
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project1_Sales/regional_distribution.png')

print("Visualizations saved in Project1_Sales/ directory.")
