import pandas as pd
import numpy as np

# Set seed
np.random.seed(42)

# Parameters
n_employees = 500
departments = ['Sales', 'Engineering', 'HR', 'Marketing', 'Finance']
locations = ['New York', 'London', 'Berlin', 'Paris', 'Tokyo']
genders = ['Male', 'Female', 'Non-Binary']

# Generate data
data = {
    'EmployeeID': range(1001, 1001 + n_employees),
    'Age': np.random.randint(22, 60, n_employees),
    'Gender': np.random.choice(genders, n_employees),
    'Department': np.random.choice(departments, n_employees),
    'Location': np.random.choice(locations, n_employees),
    'Tenure_Years': np.random.randint(0, 15, n_employees),
    'Salary': np.random.randint(40000, 150000, n_employees),
    'Performance_Rating': np.random.randint(1, 6, n_employees),
    'Attrition': np.random.choice([0, 1], n_employees, p=[0.85, 0.15]) # 15% attrition rate
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('c:/Users/touss/Desktop/GitHurb/Project3_HR/hr_data.csv', index=False)
print("HR data generated at Project3_HR/hr_data.csv")
