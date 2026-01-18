import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('c:/Users/touss/Desktop/GitHurb/Project4_NGO/health_data.csv')

# 1. Correlation between Distance and Vaccination
correlation = df['DistanceToHealthCenter_km'].corr(df['VaccinationRate'])

# 2. Impact of Clean Water on Malnutrition
water_impact = df.groupby('CleanWaterAccess')['MalnutritionRate'].mean()

# Visualizations
sns.set_theme(style="white")

# Plot 1: Distance vs Vaccination Rate
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='DistanceToHealthCenter_km', y='VaccinationRate', color='teal')
plt.title(f'Distance to Health Center vs Vaccination Rate (Corr: {correlation:.2f})')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project4_NGO/distance_vs_vaccination.png')

# Plot 2: Clean Water Access vs Malnutrition
plt.figure(figsize=(10, 6))
sns.barplot(x=water_impact.index, y=water_impact.values, palette='Blues_d')
plt.title('Clean Water Access vs Average Malnutrition Rate')
plt.ylabel('Malnutrition Rate (%)')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project4_NGO/water_vs_malnutrition.png')

# Plot 3: Distribution of Vaccination Rates
plt.figure(figsize=(10, 6))
sns.histplot(df['VaccinationRate'], kde=True, color='purple')
plt.title('Distribution of Village Vaccination Rates')
plt.savefig('c:/Users/touss/Desktop/GitHurb/Project4_NGO/vaccination_dist.png')

print("EDA complete. Charts saved in Project4_NGO/")
print("\nInsights:")
print(f"Average Vaccination Rate: {df['VaccinationRate'].mean():.2f}%")
print(f"Average Malnutrition Rate: {df['MalnutritionRate'].mean():.2f}%")
