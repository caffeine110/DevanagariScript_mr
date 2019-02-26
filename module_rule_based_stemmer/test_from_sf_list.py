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
    list_of_stem_len = list()

    for i in STEMS:
        if i in word:
            l = len(i)
            list_of_stem_len.append(l)

    #print(max_len_of_stem)
    return list_of_stem_len


### function to get stem of word
def get_stem(word):
    list_of_suffix_words = list()
    list_of_main_words = list()
    list_of_stem_len = get_stem_len(word)

    for j in list_of_stem_len:
        j = int(j)
        main_word = word[0:-j]

        len_of_word = len(word)
        len_of_suffix = len_of_word-j
        suffix = word[len_of_suffix:]

        list_of_main_words.append(main_word)
        list_of_suffix_words.append(suffix)

    return list_of_main_words, list_of_suffix_words



### function to read data from file if needed
def read_Data(filePath):
    with open(filePath, newline='') as dict_File:
        reader_d = csv.DictReader(dict_File)

        for row in reader_d:
            word = row["word"]

            #print(word)
            list_of_main_words, list_of_suffix_words = get_stem(word)
            print(list_of_main_words)



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

    list_of_main_words, list_of_suffix_words = get_stem(word)

    print("STEM Words Present in the Entered word are : ",list_of_main_words)
    print("Suffix Words Present in the Entered word are : ",list_of_suffix_words)


############################################################################
### check
if __name__ == "__main__":
    main()