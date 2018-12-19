# -*- coding: utf-8 -*-
"""
Created on Tue Dec 4 16:28:18 2018

@author: Sruthi Pasumarthy

Update 1: 14 Dec 2018, Parsing line by line

Update 2: 14 Dec 2018, Excluding the writing of new json files
"""
import json

inputFile = "H://DataSet//parts//956.json" #Name of the json input file
topicsFile = "H://DataSet//Outputs//956_Topics.txt" #Name of the text file-- for topics
topicsList = []
lines = []

with open(inputFile, "r", encoding="utf-8") as fin:
    lines = list(fin.readlines())
    print("Reading successful")
    for line in lines:
        temp = json.loads(line)
        if temp["fullText"]:
            topicsList.extend(temp["topics"])
        
    if topicsList:
        with open(topicsFile, "w", encoding="utf-8") as fout:
            for topic in topicsList:
                fout.write(topic + "\n")
        print("Writing successful - topics file: ",len(topicsList))
    
    else:
        print("No topics from this json")