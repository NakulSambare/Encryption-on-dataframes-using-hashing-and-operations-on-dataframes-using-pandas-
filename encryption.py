# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:02:42 2019

@author: user
"""

import pandas as pd
df=pd.read_csv("student.csv")
def encrypt():
    a=0
    i=0
    j=0
    age1=0
    shift1=0
    agecount=0
    shiftcount=0
    k=0
    l=0
    o=0
    while(j<10):
     i=df.loc[a, 'RollNo']
     age1=df.loc[agecount,'Age']
     shift1=df.loc[shiftcount,'Shift']
     name=df.loc[l,'Name']
     g=df.loc[o,'Result']
 
     d=i%5+2
     e=age1%5+2
     f=shift1%5+2
     print(d,' ',end='')
     print(name,' ',end='')
     print(e,' ',end='')
     print(f,' ',end='')
     print(g,' ',end='')
     print('')
     a=a+1
     agecount=agecount+1
     shiftcount=shiftcount+1
     j=j+1
     k=k+1
     l=l+1
     o=o+1