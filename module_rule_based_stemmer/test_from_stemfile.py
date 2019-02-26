#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 21:24:31 2018

@author: gaurav gahukar

"""

############################################################################
import csv


### STEMS is a Dictionary of stems
STEMS = dict()

### open file word_mainword_stem.csv
fileName = 'data/word_mainword_stem/word_mainword_stem.csv'

### read only stems from fileName
with open(fileName, 'r') as main_file:
    reader = csv.DictReader(main_file)
    
    for row in reader:
        stem = row['stem']
        stem = stem.strip()
        #print(stem)
        STEMS[stem] = len(stem)




############################################################################
### function to get len_of_stem
def get_stem_len(word):
    max_len_of_stem = 0
    for i in STEMS:
        if i in word:
            l = len(i)
            if l > max_len_of_stem :
                max_len_of_stem = l
    
    #print(max_len_of_stem)
    return max_len_of_stem


### function to get stem of word
def get_stem(word):
    max_len_of_stem = get_stem_len(word)
    main_word = word[0:-max_len_of_stem]
    len_of_main_word = len(main_word)
    stem = word[len_of_main_word:]
    #print(main_word)
    return main_word,stem


### function to read data from file if needed
def read_Data(filePath):
    with open(filePath, newline='') as dict_File:
        reader_d = csv.DictReader(dict_File)

        for row in reader_d:
            word = row["word"]

            #print(word)
            main_word = get_stem(word)
            print(main_word)



############################################################################
### main method
def main():

    #filePath = 'test.csv'
    #read_Data(filePath)

    ### test cases
    word = "आईकडे"
    word = "आईकडून"
    word = 'आईसाठी'
    word = "आईकडून"

    word = input("Enter the word to find its Stem : ")
    word  = word.strip()

    main_word,stem = get_stem(word)

    print("STEM Words Present in the Entered word is : ",main_word)
    print("Suffix Words Present in theh Entered word is : ",stem)


############################################################################
### check
if __name__ == "__main__":
    main()