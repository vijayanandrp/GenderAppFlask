import pandas as pd

file_name = 'NationalNames.csv'

# Read the excel file and converting all details into a data frames
df = pd.read_csv(file_name)

for i in df:
    print(i)
print(df.columns)

df[['Name','Gender', 'Count']].to_csv('National_names.txt', sep=',', index=False, header=0,)

