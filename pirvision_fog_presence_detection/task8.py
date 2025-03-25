import pandas as pd

# Load the dataset
file_path = "pirvision_office_dataset1.csv"
df = pd.read_csv(file_path)

# Compute standard deviation only for numeric columns
std_dev_values = df.select_dtypes(include=['number']).std()

# Display the standard deviations
print(std_dev_values)
