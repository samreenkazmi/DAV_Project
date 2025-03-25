import pandas as pd
all_files_data=pd.read_csv(r'pirvision_office_dataset1.csv')
print(all_files_data.isna().sum())