import pandas as pd

# Load the dataset
file_path = "pirvision_office_dataset1.csv"
df = pd.read_csv(file_path)

# Compute the mode for each column
mode_values = df.mode().iloc[0]

# Display the modes
print(mode_values)
