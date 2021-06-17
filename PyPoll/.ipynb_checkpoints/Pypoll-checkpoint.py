# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:03:14 2021

@author: 12103
"""

import os 
import csv

csvpath = os.path.join("Resources", "election_data.csv") 

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        print(row)
        