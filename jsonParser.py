# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 16:28:18 2018

@author: Sruthi Pasumarthy

Update 1: 14 Dec 2018, Optimized code
"""
import json

inputFile = "H://DataSet//1.json" #Name of the json input file
topicsFile = "H://DataSet//Outputs//1_Topics.txt" #Name of the text file-- for topics
newJSONFile = "H://DataSet//Outputs//1_New.json" #Name of the json file-- for updatedJSON
topicsList = []

lines = []

with open(inputFile, "r", encoding="utf-8") as fin:
    lines = list(fin.readlines())
    print("Reading successful")
    for line in lines:
        newJSON = ""
        temp = json.loads(line)
        if temp["fullText"]:
            topicsList.extend(temp["topics"])
            newJSON += str(temp) + "\n"
        
    if topicsList:
        with open(topicsFile, "w", encoding="utf-8") as fout:
            for topic in topicsList:
                fout.write(topic + "\n")
        
        with open(newJSONFile, "w", encoding="utf-8") as writer:
            writer.write(newJSON)    
        
        print("Writing successful - topics file & updated JSON")
    
    else:
        print("No topics from this json")