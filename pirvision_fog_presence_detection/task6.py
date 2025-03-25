import pandas as pd

# Load the dataset
file_path = "pirvision_office_dataset1.csv"
df = pd.read_csv(file_path)

# Compute the median only for numeric columns
median_values = df.select_dtypes(include=['number']).median()

# Display the medians
print(median_values)
