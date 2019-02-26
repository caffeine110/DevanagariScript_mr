#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 21:24:31 2018

@author: gaurav

"""


################################################################################
import csv

filePath = 'sample_case_domain/stem_domain.csv'

Dict_of_Domain = dict()

with open(filePath, newline='') as fp:
    reader = csv.DictReader(fp)
    
    for row in reader:
        word = row["word"]
        main_word = row["main_word"]
        print(word,main_word)
        Dict_of_Domain[word] = main_word
        
        



###################################################################################
        
fieldNames = ['word', 'main_word', 'stem']

filePath_w = 'word_mainword_stem/word_mainword_stem.csv'
file_w = open(filePath_w, 'w')
writer = csv.DictWriter(file_w, fieldnames= fieldNames)
writer.writeheader()



### in file
for sample_word in Dict_of_Domain:    
    
    sample_main_word = Dict_of_Domain[sample_word]

    sample_word = sample_word.strip()
    sample_main_word = sample_main_word.strip()
    print(sample_main_word)

    len_of_sample_main_word = len(sample_main_word)
    print(len_of_sample_main_word)
    
    filePath = 'mainfile/dict_of_word_stem.csv'
    with open(filePath, newline='') as fp:
        reader = csv.DictReader(fp)
        
        for row in reader:
            word = row['word']
            
            len_of_word = len(word)
            
            if sample_main_word in word:
                w = word.split(sample_main_word)
                stem = w[1]
                #stem = word - sample_main_word
                print(word,sample_main_word,stem)
                row_w = {'word':word, 'main_word':sample_main_word, 'stem':stem,}
                writer.writerow(row_w)
            else :
                pass
                
            
            