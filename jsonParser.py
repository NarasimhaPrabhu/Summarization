# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 16:28:18 2018

@author: Sruthi Pasumarthy
"""
import json

jsonFile = "D://2.json" #Name of the json input file
outputFile = "D://2_Topics.txt" #Name of the text file-- for output
topicsList = []

lines = []

with open(jsonFile, "r", encoding="utf-8") as fin:
    lines = list(fin.readlines())

op = "["
for l in lines:
    op += l+','
    
op = op[:-1] + "]"
print("Done")

decoded = list(json.loads(op))
for item in decoded:
    if item["fullText"]:
        temp = item["topics"]
        topicsList.extend(temp)

print(len(topicsList))

if(len(topicsList) > 0):
    with open(outputFile, "w", encoding="utf-8") as fout:
        for topic in topicsList:
            fout.write(topic+"\n")
    
    print("Writing successful")    
else:
    print("No topics from this json")