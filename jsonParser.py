# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 16:28:18 2018

@author: Sruthi Pasumarthy
"""
import json

inputFile = "H://DataSet//5.json" #Name of the json input file
topicsFile = "H://DataSet//Outputs//5_Topics.txt" #Name of the text file-- for topics
newJSONFile = "H://DataSet//Outputs//5_New.json" #Name of the json file-- for updatedJSON
topicsList = []

lines = []

with open(inputFile, "r", encoding="utf-8") as fin:
    lines = list(fin.readlines())

op = "["
for l in lines:
    op += l+','
    
op = op[:-1] + "]"
print("Reading successful")
newJSON = "["


decoded = list(json.loads(op))
for item in decoded:
    if item["fullText"]:
        temp = item["topics"]
        topicsList.extend(temp)
        newJSON += str(item) + "," +"\n"

newJSON = newJSON[:-2] + "]"
print(len(topicsList))

if(len(topicsList) > 0):
    with open(topicsFile, "w", encoding="utf-8") as fout:
        for topic in topicsList:
            fout.write(topic+"\n")
    
    with open(newJSONFile, "w", encoding="utf-8") as writer:
        writer.write(newJSON)
    
    print("Writing successful - topics file & updated JSON")    
else:
    print("No topics from this json")