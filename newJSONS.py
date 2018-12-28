# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:51:35 2018

@author: Sruthi Pasumarthy
"""
import json
from os import listdir

dirPath = "H://DataSet//json//"

csFile = "H://DataSet//Topics//CS.txt"
enggFile = "H://DataSet//Topics//Engg.txt"
econFile = "H://DataSet//Topics//Econ.txt"
lawFile = "H://DataSet//Topics//Law.txt"
mathFile = "H://DataSet//Topics//Math.txt"
socialFile = "H://DataSet//Topics//Social.txt"

cs = []
engg = []
econ = []
law = []
math = []
social = []

with open(csFile, "r", encoding="utf-8") as f:
    cs = f.readlines()

with open(enggFile, "r", encoding="utf-8") as f:
    engg = f.readlines()

with open(econFile, "r", encoding="utf-8") as f:
    econ = f.readlines()

with open(lawFile, "r", encoding="utf-8") as f:
    law = f.readlines()

with open(mathFile, "r", encoding="utf-8") as f:
    math = f.readlines()

with open(socialFile, "r", encoding="utf-8") as f:
    social = f.readlines()

csJSON = "H://DataSet//newJSON//CS.json"
enggJSON = "H://DataSet//newJSON//Engg.json"
econJSON = "H://DataSet//newJSON//Econ.json"
lawJSON = "H://DataSet//newJSON//Law.json"
mathJSON = "H://DataSet//newJSON//Math.json"
socialJSON = "H://DataSet//newJSON//Social.json"

inputDirFiles = list(listdir(dirPath))
print(inputDirFiles)

print(str(len(cs)) + "    " + str(len(engg))+ "  " +str(len(econ)) + "    " + str(len(law))+ "  " +str(len(math)) + "    " + str(len(social)))

for file in inputDirFiles:
    
    inputFile = dirPath + file 
    lines = []
    
    with open(inputFile, "r", encoding="utf-8") as fin:
        lines = list(fin.readlines())
        print(file + " Reading successful")
        for line in lines:
            temp = json.loads(line)
            if temp["fullText"]:
                for it in temp["topics"]:
                    if cs.__contains__(it):
                        print(it)
                        with open(csJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
                    if engg.__contains__(it):
                        print(it)
                        with open(enggJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
                    if econ.__contains__(it):
                        print(it)
                        with open(econJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
                    if law.__contains__(it):
                        print(it)
                        with open(lawJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
                    if math.__contains__(it):
                        print(it)
                        with open(mathJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
                    if social.__contains__(it):
                        print(it)
                        with open(socialJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line + "\n")
    
    print(file + " Completed parsing")

        

