import pandas as pd
all_files_data=pd.read_csv(r'pirvision_office_dataset1.csv')
df = pd.DataFrame(all_files_data)
print(df.head(100))
print(df.tail(100))
print(df.dtypes)
print("rows columns = " ,df.shape)