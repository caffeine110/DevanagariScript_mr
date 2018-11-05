#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:14:03 2018

AIM : Generate Suggestions

"""


dict_of_files = dict(dict_ka='alpha/ka.csv', dict_kha='alpha/kha.csv', dict_ga='alpha/ga.csv', 
                     dict_gha='alpha/gha.csv', dict_ca='alpha/ca.csv', dict_cha='alpha/cha.csv',
                     dict_ja='alpha/ja.csv', dict_jha='alpha/jha.csv', dict_ta='alpha/ta.csv',
                     dict_tha='alpha/tha.csv', dict_da='alpha/da.csv', dict_dha='alpha/dha.csv',
                     dict_na='alpha/na.csv', dict_taa='alpha/taa.csv', dict_thaa='alpha/thaa.csv',
                     dict_daa='alpha/daa.csv', dict_dhaa='alpha/dhaa.csv', dict_naa='alpha/naa.csv',
                     dict_pa='alpha/pa.csv', dict_pha='alpha/pha.csv', dict_ba='alpha/ba.csv',
                     dict_bha='alpha/bha.csv', dict_ma='alpha/ma.csv', dict_ya='alpha/ya.csv',
                     dict_ra='alpha/ra.csv', dict_la='alpha/la.csv', dict_va='alpha/va.csv',
                     dict_sha='alpha/sha.csv', dict_shaa='alpha/shaa.csv', dict_sa='alpha/sa.csv',
                     dict_ha='alpha/ha.csv', dict_lha='alpha/lha.csv' )


print(dict_of_files['dict_ka'])

#####################################################




from combinations import combine_dict_alpha
dict_a = ['अ' , 'आ' ,'अॅ',  'ऑ',  'ऒ', 'ओ', 'औ', 'अं', 'अः']

w3 = 'आईवडिलांसम्वेत'
pattern = w3[0:3]
print(pattern)

import csv

for dict_alpha in combine_dict_alpha:
    dict_alpha_index = combine_dict_alpha.index(dict_alpha)
    print(dict_alpha_index)
    for alpha in dict_alpha:
        if alpha == pattern[0]:
            print(alpha)
            print(dict_of_files[dict_alpha_index])
            key = dict_of_files[dict_alpha_index]
            FilePath = dict_of_files[dict_alpha_index]
            with open(FilePath, newline='') as dict_File:
                reader_d = csv.DictReader(dict_File)
                for row in reader_d:
                    if pattern in row['word']:
                        print(row)
            


print(combine_dict_alpha)

key = dict_a




word = 'आभ्यासामध्येही'
w0 = 'आघाडीवर्'
w2 ='आईशी'
w4 = 'आईविषयी'
w5 = 'आखीव'

dict_a = ['अ' , 'आ' ,'अॅ',  'ऑ',  'ऒ', 'ओ', 'औ', 'अं', 'अः']
dict_i = ['इ',  'ई' ]
dict_u = [ 'उ' , 'ऊ' ]
dict_e = ['ऎ',  'ए', 'ऐ' ]
dict_ru = ['ऋ', 'ॠ' ]



import csv
w3 = 'आईवडिलांसम्वेत'
pattern = w3[0:5]
print(pattern)


for i in dict_a:
    if i == w3[0]:
        with open('alpha/a.csv', newline='') as dict_File:
            reader_d = csv.DictReader(dict_File)
            for row in reader_d:
                if pattern in row['word']:
                    print(row)




for i in dict_a:
    if i == word[0]:
        with open('alpha/a.csv', newline='') as dict_File:
            reader_d = csv.DictReader(dict_File)
            for row in reader_d:
                if pattern in row['word']:
                    print(row)



