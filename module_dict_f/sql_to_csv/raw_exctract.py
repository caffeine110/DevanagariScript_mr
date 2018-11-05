#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:48:07 2018


@author: gaurav gahukar


AIM     : to create DICT.csv file

        : input  : samoak.sql
        : output : exctracted.csv


"""


import csv

data = open('samoak.sql', 'r')
Lines = data.readlines()

length = len(Lines)
print(length)
counter = 0
c=0

field_Names = ["TEXT1",'word',"TEXT2"]

file_to_write = open('exctracted.csv', 'w')
writer = csv.DictWriter(file_to_write, fieldnames=field_Names)
writer.writeheader()

for line in Lines:
    try:    
        row = line.split("'")
        new_row = { 'TEXT1':row[0], "word":row[1], "TEXT2":row[-1] }
        print(new_row)
        writer.writerow(new_row)
    except:
        pass