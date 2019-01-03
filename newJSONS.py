# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:51:35 2018

@author: Sruthi Pasumarthy
@Update 1: Reading csv with pandas, changed the checking condition

"""
import json
import pandas as pd
from os import listdir

dirPath = "H://DataSet//json//"

csFile = "H://DataSet//Topics//CS.csv"
enggFile = "H://DataSet//Topics//Engg.csv"
econFile = "H://DataSet//Topics//Econ.csv"
lawFile = "H://DataSet//Topics//Law.csv"
mathFile = "H://DataSet//Topics//Math.csv"
socialFile = "H://DataSet//Topics//Social.csv"

cs = pd.read_csv(csFile, header = None)
engg = pd.read_csv(enggFile, header = None)
econ = pd.read_csv(econFile, header = None)
law = pd.read_csv(lawFile, header = None)
math = pd.read_csv(mathFile, header = None)
social = pd.read_csv(socialFile, header = None)

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
                    
                    if (cs[0] == it).any():
                        #print(it)
                        with open(csJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
                    if (engg[0] == it).any():
                        #print(it)
                        with open(enggJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
                    if (econ[0] == it).any():
                        #print(it)
                        with open(econJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
                    if (law[0] == it).any():
                        #print(it)
                        with open(lawJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
                    if (math[0] == it).any():
                        #print(it)
                        with open(mathJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
                    if (social[0] == it).any():
                        #print(it)
                        with open(socialJSON, "a+", encoding="utf-8") as fout:
                            fout.write(line)
    
    print(file + " Completed parsing")