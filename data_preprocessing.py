import pandas as pd

df = pd.read_csv('traffic_management_dataset.csv')

print(f'data has {df.shape[0]} rows and {df.shape[1]} columns')
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

print('NULL Values')
print(df.isnull().sum())

#fixing data types
df['Time'] = pd.to_datetime(df['Time'], format= '%H:%M').dt.hour
df['Date'] = pd.to_datetime(df['Date'])
df['Traffic_Signal_Malfunction'] = df['Traffic_Signal_Malfunction'].map({'Yes':1, 'No':0})
df['Accident_Reported'] = df['Accident_Reported'].map({'Yes':1, 'No':0})

#handle missing values
for col in ['Area', 'Road_Type', 'Weather_Condition', 'Congestion_Level']:
    df[col].fillna(df[col].mode()[0], inplace= True)
df['Vehicle_Count'].fillna(df['Vehicle_Count'].mean(), inplace= True)
df['Average_Speed_kmph'].fillna(df['Average_Speed_kmph'].mean(), inplace= True)

#removing dupes
df.drop_duplicates(inplace= True)
print(f'shape after dropping dupe rows {df.shape[0]}')

#fixing outliers
Q1 = df['Vehicle_Count'].quantile(0.25)
Q3 = df['Vehicle_Count'].quantile(0.75)
IQR = Q3 - Q1
df =  df[~((df['Vehicle_Count'] < Q1 - (1.5*IQR)) | (df['Vehicle_Count'] > Q3 + (1.5*IQR)))]

#standardizing column names
for col in ['Area', 'Road_Type', 'Weather_Condition', 'Congestion_Level']:
    df[col] = df[col].str.strip().str.title()

#savung the edited dataset (to disk)
df.to_csv('cleaned_dataset.csv')