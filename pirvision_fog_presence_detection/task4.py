import pandas as pd

# Load the dataset
file_path = "pirvision_office_dataset1.csv"
df = pd.read_csv(file_path)

# Compute the mean for each numeric column
mean_values = df.select_dtypes(include=['number']).mean()

# Display the means
print(mean_values)