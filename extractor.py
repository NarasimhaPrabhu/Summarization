# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:36:01 2019

@author: Sruthi Pasumarthy
"""
import pandas as pd
import json

markerExcel = "D://StartEndMarkers.xlsx"    
#currentFile = "D://sampleExtract.txt"
jsonFile = "D://sample.json"
with open(jsonFile, "r", encoding="utf-8") as fin:
    jsonlines = list(fin.readlines())
    print(jsonFile + " Reading successful")
    for l in jsonlines:
        temp = json.loads(l)
        content = temp["fullText"]
        lines = []
        oneWordLines = []
        '''content = ""
        with open(currentFile, 'r') as fin:
            content = fin.read()'''
        
        lines = content.split("\n")
        
        print("Number of lines: ",str(len(lines)))
        #print(lines)
        for i in range(len(lines)):
            lines[i] =lines[i].strip()
            
        
        def extractHeaders(tmpList):
            headers = []
            for i in tmpList:
                i = i.strip()
                if i == '':
                    continue
                elif i.count(' ') > 1:
                    continue
                elif i.count(' ') == 1:
                    t = i.split(' ')[0]
                    iNumFlag = t.isdigit()
                    if iNumFlag:
                        headers.append(i)
                    else:
                        if t.count('.') == 1:
                            tNumFlag = t.split('.')[0].isdigit()
                            if tNumFlag:
                                headers.append(i)
                            else:
                                continue
                        else:
                            continue
                elif i.count(' ') == 0:
                    if i[-1] == '.':
                        continue
                    elif  i[-1] == ',':
                        continue
                    else:
                        headers.append(i)
            
            print("Length of headers list: ", str(len(headers)))
            return headers;
        
        oneWordLines = extractHeaders(lines)
        print(oneWordLines)
        extractedDict = {}
        extractedDict["id"] = temp["id"] 
        def extractContent(fromMarker, toMarker):
        
             requiredContent = lines[lines.index(fromMarker) + 1 : lines.index(toMarker)]
             extractedDict[fromMarker] = ''.join(requiredContent)
             return;
                    
        df = pd.read_excel(markerExcel)
        
        toCompare = df['Start'].unique()
        print(toCompare)
        matches = []
        
        for item in oneWordLines:
            if item.lower() in toCompare:
                matches.append(item)
                print("Match -- ",item)
            elif item.count(' ') == 1:
                tmp = item.split(' ')[1]
                if tmp.lower() in toCompare:
                    print("Match -- "+tmp+"   "+item)
                    matches.append(item)
                
        for i in range(len(matches)):
            if i == len(matches)- 1:
                break
            else:
                extractContent(matches[i], matches[i+1])
            
        #print(extractedDict)
        
        with open('D://extractData_2.json', 'a+') as fp:
            json.dump(extractedDict, fp)
        
        print(temp["id"]+"   --- Extraction done.")



















