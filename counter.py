# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:42:49 2018

@author: Sruthi Pasumarthy
"""
import pandas as pd

topicsDF = pd.read_csv("D://Topics.txt", delimiter='\n')
s = topicsDF['Topics'].value_counts().rename('Count')
topicsDF = topicsDF.join(s, on='Topics')
#print(topicsDF)
#newDF = topicsDF.Topics.unique()
#print(newDF)  
topicsDF.to_csv("D://TopicsWithCount.csv", index=False)

