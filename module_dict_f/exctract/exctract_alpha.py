#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:36:39 2018

@author: gaurav
"""

"""
### dictionary for combinations of alphabets

combine_dict_alpha = [dict_ka, dict_kha, dict_ga, dict_gha, dict_ca, dict_cha, dict_ja, dict_jha, 
                      dict_ta, dict_tha, dict_da, dict_dha, dict_na, dict_taa, dict_thaa, dict_dhaa, dict_naa,
                      dict_pa, dict_pha, dict_ba, dict_bha, dict_ma, dict_ya, dict_ra, dict_la, dict_va,
                      dict_sha, dict_shaa, dict_sa, dict_ha, dict_lha]

"""

dict_a = ['अ' , 'आ' ,'अॅ',  'ऑ',  'ऒ', 'ओ', 'औ', 'अं', 'अः']
dict_i = ['इ',  'ई' ]
dict_u = [ 'उ' , 'ऊ' ]
dict_e = ['ऎ',  'ए', 'ऐ' ]
dict_ru = ['ऋ', 'ॠ' ]



### part - 1
import  csv
#from combinations import combine_dict_alpha
from combinations import dict_ka, dict_kha, dict_ga, dict_gha, dict_ca, dict_cha, dict_ja, dict_jha, dict_ta, dict_tha, dict_da, dict_dha, dict_na, dict_taa, dict_thaa, dict_daa, dict_dhaa, dict_naa,dict_pa, dict_pha, dict_ba, dict_bha, dict_ma, dict_ya, dict_ra, dict_la, dict_va,dict_sha, dict_shaa, dict_sa, dict_ha, dict_lha
#from combinations import dict_a, dict_i, dict_e, dict_u, dict_ru

### filednames
field_Names = ['word','stemed']

####
#### all dictionary writers
file_ka = open('alpha/ka.csv', 'w')
writer_ka = csv.DictWriter(file_ka, fieldnames=field_Names)
writer_ka.writeheader()

file_kha = open('alpha/kha.csv', 'w')
writer_kha = csv.DictWriter(file_kha, fieldnames=field_Names)
writer_kha.writeheader()

file_ga = open('alpha/ga.csv', 'w')
writer_ga = csv.DictWriter(file_ga, fieldnames=field_Names)
writer_ga.writeheader()

file_gha = open('alpha/gha.csv', 'w')
writer_gha = csv.DictWriter(file_gha, fieldnames=field_Names)
writer_gha.writeheader()

## cha
file_ca = open('alpha/ca.csv', 'w')
writer_ca = csv.DictWriter(file_ca, fieldnames=field_Names)
writer_ca.writeheader()

file_cha = open('alpha/cha.csv', 'w')
writer_cha = csv.DictWriter(file_cha, fieldnames=field_Names)
writer_cha.writeheader()

file_ja = open('alpha/ja.csv', 'w')
writer_ja = csv.DictWriter(file_ja, fieldnames=field_Names)
writer_ja.writeheader()

file_jha = open('alpha/jha.csv', 'w')
writer_jha = csv.DictWriter(file_jha, fieldnames=field_Names)
writer_jha.writeheader()

### 
file_ta = open('alpha/ta.csv', 'w')
writer_ta = csv.DictWriter(file_ta, fieldnames=field_Names)
writer_ta.writeheader()

file_tha = open('alpha/tha.csv', 'w')
writer_tha = csv.DictWriter(file_tha, fieldnames=field_Names)
writer_tha.writeheader()


file_da = open('alpha/da.csv', 'w')
writer_da = csv.DictWriter(file_da, fieldnames=field_Names)
writer_da.writeheader()

file_dha = open('alpha/dha.csv', 'w')
writer_dha = csv.DictWriter(file_dha, fieldnames=field_Names)
writer_dha.writeheader()

file_na = open('alpha/na.csv', 'w')
writer_na = csv.DictWriter(file_na, fieldnames=field_Names)
writer_na.writeheader()


### taa
file_taa = open('alpha/taa.csv', 'w')
writer_taa = csv.DictWriter(file_taa, fieldnames=field_Names)
writer_taa.writeheader()

file_thaa = open('alpha/thaa.csv', 'w')
writer_thaa = csv.DictWriter(file_thaa, fieldnames=field_Names)
writer_thaa.writeheader()

file_daa = open('alpha/daa.csv', 'w')
writer_daa = csv.DictWriter(file_daa, fieldnames=field_Names)
writer_daa.writeheader()

file_dhaa = open('alpha/dhaa.csv', 'w')
writer_dhaa = csv.DictWriter(file_dhaa, fieldnames=field_Names)
writer_dhaa.writeheader()

file_naa = open('alpha/naa.csv', 'w')
writer_naa = csv.DictWriter(file_naa, fieldnames=field_Names)
writer_naa.writeheader()

## pa
file_pa = open('alpha/pa.csv', 'w')
writer_pa = csv.DictWriter(file_pa, fieldnames=field_Names)
writer_pa.writeheader()

file_pha = open('alpha/pha.csv', 'w')
writer_pha = csv.DictWriter(file_pha, fieldnames=field_Names)
writer_pha.writeheader()

file_ba = open('alpha/ba.csv', 'w')
writer_ba = csv.DictWriter(file_ba, fieldnames=field_Names)
writer_ba.writeheader()

file_bha = open('alpha/bha.csv', 'w')
writer_bha = csv.DictWriter(file_bha, fieldnames=field_Names)
writer_bha.writeheader()

file_ma = open('alpha/ma.csv', 'w')
writer_ma = csv.DictWriter(file_ma, fieldnames=field_Names)
writer_ma.writeheader()


### ya
file_ya = open('alpha/ya.csv', 'w')
writer_ya = csv.DictWriter(file_ya, fieldnames=field_Names)
writer_ya.writeheader()

file_ra = open('alpha/ra.csv', 'w')
writer_ra = csv.DictWriter(file_ra, fieldnames=field_Names)
writer_ra.writeheader()

file_la = open('alpha/la.csv', 'w')
writer_la = csv.DictWriter(file_la, fieldnames=field_Names)
writer_la.writeheader()

file_va = open('alpha/va.csv', 'w')
writer_va = csv.DictWriter(file_va, fieldnames=field_Names)
writer_va.writeheader()

### sha
file_sha = open('alpha/sha.csv', 'w')
writer_sha = csv.DictWriter(file_sha, fieldnames=field_Names)
writer_sha.writeheader()

file_shaa = open('alpha/shaa.csv', 'w')
writer_shaa = csv.DictWriter(file_shaa, fieldnames=field_Names)
writer_shaa.writeheader()

file_sa = open('alpha/sa.csv', 'w')
writer_sa = csv.DictWriter(file_sa, fieldnames=field_Names)
writer_sa.writeheader()

## ha
file_ha = open('alpha/ha.csv', 'w')
writer_ha = csv.DictWriter(file_ha, fieldnames=field_Names)
writer_ha.writeheader()

file_lha = open('alpha/lha.csv', 'w')
writer_lha = csv.DictWriter(file_lha, fieldnames=field_Names)
writer_lha.writeheader()

############
## a
file_a = open('alpha/a.csv', 'w')
writer_a = csv.DictWriter(file_a, fieldnames=field_Names)
writer_a.writeheader()

file_i = open('alpha/i.csv', 'w')
writer_i = csv.DictWriter(file_i, fieldnames=field_Names)
writer_i.writeheader()

file_u = open('alpha/u.csv', 'w')
writer_u = csv.DictWriter(file_u, fieldnames=field_Names)
writer_u.writeheader()

file_e = open('alpha/e.csv', 'w')
writer_e = csv.DictWriter(file_e, fieldnames=field_Names)
writer_e.writeheader()

file_ru = open('alpha/ru.csv', 'w')
writer_ru = csv.DictWriter(file_ru, fieldnames=field_Names)
writer_ru.writeheader()



with open('Dict.csv', newline='') as dict_File:
    reader_d = csv.DictReader(dict_File)
    
    for row in reader_d:
        word = row['word']
        stemed = ""

        ### ka
        for i in dict_ka:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ka.writerow(new_row)

        for i in dict_kha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_kha.writerow(new_row)

        for i in dict_ga:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ga.writerow(new_row)

        for i in dict_gha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_gha.writerow(new_row)

        ### cha
        for i in dict_ca:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ca.writerow(new_row)

        for i in dict_cha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_cha.writerow(new_row)

        for i in dict_ja:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ja.writerow(new_row)

        for i in dict_jha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_jha.writerow(new_row)



        ### ta
        for i in dict_ta:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ta.writerow(new_row)

        for i in dict_tha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_tha.writerow(new_row)

        for i in dict_da:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_da.writerow(new_row)

        for i in dict_dha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_dha.writerow(new_row)

        for i in dict_na:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_na.writerow(new_row)


        ### taa
        for i in dict_taa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_taa.writerow(new_row)

        for i in dict_thaa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                print(new_row)
                writer_thaa.writerow(new_row)

        for i in dict_daa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_daa.writerow(new_row)

        for i in dict_dhaa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_dhaa.writerow(new_row)

        for i in dict_naa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_naa.writerow(new_row)

        ### pa
        for i in dict_pa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_pa.writerow(new_row)

        for i in dict_pha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_pha.writerow(new_row)

        for i in dict_ba:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ba.writerow(new_row)

        for i in dict_bha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_bha.writerow(new_row)

        for i in dict_ma:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ma.writerow(new_row)

        ###
        for i in dict_ya:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ya.writerow(new_row)

        for i in dict_ra:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ra.writerow(new_row)

        for i in dict_la:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_la.writerow(new_row)

        for i in dict_va:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_va.writerow(new_row)

        ### sha
        for i in dict_sha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_sha.writerow(new_row)

        for i in dict_shaa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_shaa.writerow(new_row)

        for i in dict_sa:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_sa.writerow(new_row)

        ## ha lha
        for i in dict_ha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ha.writerow(new_row)

        for i in dict_lha:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_lha.writerow(new_row)
                
        ######## a, i , u , e, ru
        for i in dict_a:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_a.writerow(new_row)

        for i in dict_i:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_i.writerow(new_row)
                
        for i in dict_u:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_u.writerow(new_row)

        for i in dict_e:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_e.writerow(new_row)

        for i in dict_ru:
            if i==word[0]:
                new_row = {'word':word, 'stemed':stemed}
                writer_ru.writerow(new_row)
