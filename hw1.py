import pandas as pd

df = pd.read_csv('Student Attitude and Behavior.csv')

print(df.head())
print('---------------')
print(df.info())
print('---------------')
print(df.describe())
print('---------------')
print('---------------')

df = pd.read_csv('dz.csv')

print(df.groupby('City')['Salary'].mean())
