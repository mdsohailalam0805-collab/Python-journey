import pandas as pd
import numpy as np
data={
    "name": ['sohail','altamash', 'waseem','azad','farhan'],
    "age": [20,None,25,24,26],
    "salary": [None,20000,25000,30000,None]
}
df=pd.DataFrame(data)
print("original data")
print(df)

# using isnullsum()
print(df.isnull().sum())

# using dropna()
df_drope=df.dropna()
print(df_drope)

# using fillna()

df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())


df.fillna({
    'age': df['age'].mean(),
    'salary': df['salary'].mean()
}, inplace=True)
print(df)

# to check missing data percentage
print(df.isnull().mean()*100)