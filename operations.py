# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:10:53 2019

@author: user
"""

import pandas as pd
df=pd.read_csv("student.csv")
from encryption import encrypt
print('The data frame in Encrypted form')     
encrypt()     


print()
print('Operations On dataframe')
print()
print('No of rows and columns in data frame')
rows,columns=df.shape
print('Rows=',rows)
print('Columns=',columns)
print()
print('Head and Tail of DataFrame')
print('Enter no of rows you want to print from above')
h=int(input())
print(df.head(h))
print('Enter no of rows you want to print from below')
t=int(input())
print(df.tail(t))
print()
print('Enter the positions from where you want data and upto what position')
p1=int(input())
p2=int(input())
print(df[2:6])
print()
print('Printing only two columns')
print(df[['RollNo','Name']])
print()
print('Datatypes in dataframe')
print(df.dtypes)
print()
print('Printing maximum age ')
print(df["Age"].max())
print('Sorting operation on dataframe')

df1 = pd.DataFrame({'one': [2, 1, 1, 1],
                    'two': [1, 3, 2, 4],
                     'three': [5, 4, 3, 2]})
df1.sort_values(by='two')
print(df1)

print('nlargest method to print  largest values from a column')
df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],
                    'b': list('abdceff'),
                      'c': [1.0, 2.0, 4.0, 3.2, 2.4, 3.0, 4.0]})
print(df.nlargest(3, 'a'))    
print('n smallest method to print no of smallest values')
print(df.nsmallest(5, ['a', 'c']))    