import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori 

fname="G:\\python\\pycharmcodes\\mllab1\\groceries.csv"
platype=open(fname,'r')
data=pd.read_csv(platype,header=None)
#print(data.head())

record = []

for i in range(0,9835):
    record.append([str(data.values[i,j]) for j in range (0,32)])
association_rules = apriori(record, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)  
association_results = list(association_rules)  
print(len(association_results)) 
#print(association_results[0])

for item in association_results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

