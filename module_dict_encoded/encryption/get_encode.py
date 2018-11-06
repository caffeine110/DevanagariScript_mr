#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:43:02 2018

@author: gaurav
"""

# get alphabets from encodes
from encodes import List_of_DEV_C
from encodes import List_of_ISO_C
from encodes import DIGITS, ISO_DIGITS
from encodes import DEV_VOWELS,ISO_DEV_VOWELS
#from encodes import VOWELS, ISO_VOWELS


#####################################################################

for i,j in zip( List_of_DEV_C, List_of_ISO_C):
    for l,m in zip( i,j ):
        print(l +  "     "+ m)
    print()


print(len(List_of_DEV_C), List_of_DEV_C)
print(len(List_of_ISO_C), List_of_ISO_C)

print(len(DIGITS), DIGITS)

print(len(ISO_DIGITS), ISO_DIGITS)

print(len(DEV_VOWELS), DEV_VOWELS)

print(len(ISO_DEV_VOWELS), ISO_DEV_VOWELS)
######################################################################

##
## ENcryption

var = "सातासमुद्रांपलीकड्ल्या"


for i in var:
    print(i)
enc = ''

for pattern in var:
    for L1, L2 in zip((List_of_DEV_C), (List_of_ISO_C) ):
        for C1,C2 in zip(L1,L2):
            if pattern == C1:
                enc = enc+C2+';'


    for V1,V2 in zip(DEV_VOWELS, ISO_DEV_VOWELS):
        if pattern == V1:
            enc = enc+V2+';'




print(enc)


enc_text = enc
######################################################################
##
## Decryption

enc_li = enc_text.split(';')
print(enc_li)

ori_dev_word =''
for pattern in enc_li:
    for L1, L2 in zip((List_of_ISO_C), (List_of_DEV_C) ):
        for C1,C2 in zip(L1,L2):
            if pattern == C1:
                ori_dev_word = ori_dev_word+C2


    for V1,V2 in zip(ISO_DEV_VOWELS, DEV_VOWELS):
        if pattern == V1:
            ori_dev_word = ori_dev_word+V2

print(ori_dev_word)


#####################################################################
###
##
l = list()
var = "सातासमुद्रांपलीकड्ल्या"
for i in var:
    print(i)
    l.append(i)

print(l)


der = ''
for i in l:
    der += i

print(der)




