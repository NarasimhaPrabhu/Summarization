#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:28:01 2018

@author: prathibha
"""

filenames = ['/Volumes/Untitled/Files/Topics1.txt', '/Volumes/Untitled/Files/Topics2.txt','/Volumes/Untitled/Files/Topics3.txt' ]
with open('/Volumes/Untitled/Files/output1.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                 outfile.write(line)
        