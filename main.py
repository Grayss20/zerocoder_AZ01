import pandas as pd

data = [1, 2, 3, 4, 5]

series = pd.Series(data)

print(series)

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)

print(df)

df = pd.read_csv('World-happiness-report-2024.csv')

print(df[df['Healthy life expectancy'] > 0.7])
