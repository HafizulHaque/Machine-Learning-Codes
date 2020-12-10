import pandas as pd

fname="G:\\python\\pycharmcodes\\mllab1\\groceries.csv"

platype=open(fname,'r')
count={}
z=platype.read().split('\n')
for x in z:
    y=x.split(',')
    for a in y:
        if a in count:
            count[a]+=1
        else:
            count[a]=1
    
for keys,values in count.items():
    print(keys,values)
