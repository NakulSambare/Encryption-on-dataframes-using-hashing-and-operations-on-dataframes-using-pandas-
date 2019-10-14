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

i=0

def rowsandcol():
  print('No of rows and columns in data frame')
  rows,columns=df.shape
  print('Rows=',rows)
  print('Columns=',columns)
  print()  
  
def headtail():
    print('Head and Tail of DataFrame')
   # print('Enter no of rows you want to print from above')
    #h=int(input())
    h=5
    print(df.head(h))
    #print('Enter no of rows you want to print from below')
    #t=int(input())
    t=4
    print(df.tail(t))
    print()
    
    
def printfrom():
    #print('Enter the positions from where you want data and upto what position')
    #p1=int(input())
    #p2=int(input())
    p1=2
    p2=5
    print(df[p1:p2])
    print()

def printcols():
    print('Printing only two columns')
    print(df[['RollNo','Name']])
    print()
    
def datatypes():
    print('Datatypes in dataframe')
    print(df.dtypes)
    print()
    
def printmax():
    print('Printing maximum age ')
    print(df["Age"].max())
    
    
def sort():
    print('Sorting operation on dataframe')

    df1 = pd.DataFrame({'one': [2, 1, 1, 1],
                    'two': [1, 3, 2, 4],
                     'three': [5, 4, 3, 2]})
    df1.sort_values(by='two')
    print(df1)
    
def largesmall():
    print('nlargest method to print  largest values from a column')
    df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],
                    'b': list('abdceff'),
                      'c': [1.0, 2.0, 4.0, 3.2, 2.4, 3.0, 4.0]})
    print(df.nlargest(3, 'a'))    
    print('n smallest method to print no of smallest values')
    print(df.nsmallest(5, ['a', 'c']))  
    
    
"""    
while(i<=8):
    print("1.rows and columns  2.Head and Tail 3.Print from position 4.Print columns 5.Print Datatypes 6.max age 7.sort 8.largeand small 9.quit")
    j=int(input())
    if(j==1):
        rowsandcol()
    if(j==2):
        headtail()
    if(j==3):
         printfrom()
    if(j==4):
        printcols()
    if(j==5):
        datatypes()
    if(j==6):
        printmax()
    if(j==7):
        sort()
    if(j==8):
        largesmall()
    if(j==9):
        break
    
    i=i+1
 """
rowsandcol()
headtail()    
printfrom()    
printcols()
datatypes()
printmax()        
largesmall()        
        
    
  
            
        
        
        
        
    
    
