import pandas as pd
import numpy as np

# Set seed
np.random.seed(99)

# Parameters
n_villages = 100
villages = [f'Village_{i}' for i in range(1, n_villages + 1)]

# Generate data
data = {
    'VillageID': villages,
    'Population': np.random.randint(500, 5000, n_villages),
    'VaccinationRate': np.random.uniform(30.0, 95.0, n_villages),
    'MalnutritionRate': np.random.uniform(5.0, 25.0, n_villages),
    'DistanceToHealthCenter_km': np.random.uniform(0.5, 20.0, n_villages),
    'CleanWaterAccess': np.random.choice(['Yes', 'No'], n_villages, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('c:/Users/touss/Desktop/GitHurb/Project4_NGO/health_data.csv', index=False)
print("Health impact data generated at Project4_NGO/health_data.csv")
