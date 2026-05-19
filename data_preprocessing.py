import pandas as pd

df = pd.read_csv('traffic_management_dataset.csv')

# print(f'data has {df.shape[0]} rows and {df.shape[1]} columns')
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.columns)

print('NULL Values')
print(df.isnull())