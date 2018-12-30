# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:42:49 2018

@author: Sruthi Pasumarthy

Update 1: 19 Dec 2018, Removing duplicate rows from the dataframe
Update 2: 30 Dec 2018, fETCHING TOP 60000 topics
"""
import pandas as pd

topicsDF = pd.read_csv("D://Merged.txt", delimiter='\n')
s = topicsDF['Topics'].value_counts().rename('Count')
topicsDF = topicsDF.join(s, on='Topics')
topicsDF = topicsDF.drop_duplicates()
topicsDF = topicsDF.sort_values(by='Count', ascending=False)
df = topicsDF.head(60000)
df.to_csv("D://Topics_All.csv", index=False)
print(len(topicsDF.index))