import pandas as pd
from datetime import datetime

current_date = datetime.now().strftime('%Y/%m/%d')
current_date = datetime.strptime(current_date, "%Y/%m/%d")

# df = pd.read_csv('read.csv')
df = pd.read_csv(input("Enter file path"))

try:
    for i in range(len(df)):
        birth_date = datetime.strptime(df.loc[i].at["Birthdate"], '%m-%d-%Y').strftime('%Y/%m/%d')
        birth_date = datetime.strptime(birth_date, "%Y/%m/%d")
        age = current_date.year - birth_date.year
        if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1
        df.loc[i, 'Age'] = age
except:
    print("Birtdate format should be in '%m-%d-%Y' format")

print(df)
