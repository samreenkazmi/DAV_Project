import pandas as pd

# Load the dataset
file_path = "pirvision_office_dataset1.csv"
df = pd.read_csv(file_path)

# Compute variance only for numeric columns
variance_values = df.select_dtypes(include=['number']).var()

# Display the variances
print(variance_values)
