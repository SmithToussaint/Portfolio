import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('c:/Users/touss/Desktop/GitHurb/Project3_HR/hr_data.csv')

# 1. Attrition Rate by Department
attrition_rate = df.groupby('Department')['Attrition'].mean() * 100

# 2. Average Salary by Department
avg_salary = df.groupby('Department')['Salary'].mean()

# 3. Diversity (Gender Distribution)
gender_dist = df['Gender'].value_counts()

# Visualizations
sns.set_theme(style="whitegrid")

# Plot 1: Attrition Rate
plt.figure(figsize=(10, 6))
sns.barplot(x=attrition_rate.index, y=attrition_rate.values, palette='Reds_d')
plt.title('Attrition Rate by Department (%)')
plt.ylabel('Rate (%)')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project3_HR/attrition_by_dept.png')

# Plot 2: Salary Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Department', y='Salary', palette='Set2')
plt.title('Salary Distribution by Department')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project3_HR/salary_distribution.png')

# Plot 3: Performance vs Turnover
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Performance_Rating', hue='Attrition', palette='coolwarm')
plt.title('Performance Rating vs Turnover')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project3_HR/performance_vs_attrition.png')

print("HR Analysis complete. Charts saved in Project3_HR/")
print("\nKey Metrics:")
print(f"Overall Attrition Rate: {df['Attrition'].mean()*100:.2f}%")
print(f"Average Tenure: {df['Tenure_Years'].mean():.2f} years")
