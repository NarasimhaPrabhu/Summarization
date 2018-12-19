# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 10:42:49 2018

@author: Sruthi Pasumarthy

Update 1: 19 Dec 2018, Removing duplicate rows from the dataframe
"""
import pandas as pd

topicsDF = pd.read_csv("D://fullmerge.txt", delimiter='\n')
s = topicsDF['Topics'].value_counts().rename('Count')
topicsDF = topicsDF.join(s, on='Topics')
topicsDF = topicsDF.drop_duplicates()
topicsDF.to_csv("D://TopicsWithCount_Sruthi.csv", index=False)