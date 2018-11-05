c1 = 'क'
c2 = 'ख'
c3 = 'ग'
c4 = 'घ'

c5 = 'च'
c6 = 'छ'
c7 = 'ज'
c8 = 'झ'

c9 = 'ट'
c10 = 'ठ'
c11 = 'ड'
c12 = 'ढ'
c13 = 'ण'

c14 = 'त'
c15 = 'थ'
c16 = 'द'
c17 = 'ध'
c18 = 'न'

c19 = 'प'
c20 = 'फ'
c21 = 'ब'
c22 = 'भ'
c23 = 'म'

c24 = 'य'
c25 = 'र'
c26 = 'ल'
c27 = 'व'

c28 = 'श'
c29 = 'ष'
c30 = 'स'

c31 = 'ह'
c32 = 'ळ'


c40 = 'अ'
c41 = 'इ'
c42 = 'उ'
c43 = 'ए'
c44 = 'ऋ'

c45 = 'ङ'
c46 = 'ञ'
c47 = 'ऩ'
c48 = 'ऱ'
c49 = 'ऴ'

consonants = [ c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32,c40,c41,c42,c43,c44 ]


v1 = 'क'
v1[0]

v2 = 'का'
v2[0]
v2[1]

v3 = 'कॅ'
v3[0]
v3[1]

v4 = 'कॉ'
v4[0]
v4[1]

v5 = 'कि'
v5[0]
v5[1]


v6 = 'की'
v6[0]
v6[1]

v7 = 'कु'
v7[0]
v7[1]

v8 = 'कू'
v8[0]
v8[1]

v9 = 'कॆ'
v9[0]
v9[1]

v10 = 'के'
v10[0]
v10[1]

v11 = 'कै'
v11[0]
v11[1]

v12 = 'कॊ'
v12[0]
v12[1]

v13 = 'को'
v13[0]
v13[1]

v14 = 'कौ'
v14[0]
v14[1]

v15 = 'कृ'
v15[0]
v15[1]

v16 = 'कॄ'
v16[0]
v16[1]

v17 = 'कॢ'
v17[0]
v17[1]

v18 = 'कॣ'
v18[0]
v18[1]

v19 = 'कं' 
v19[0]
v19[1]

v20 = 'कः'
v20[0]
v20[1]


D_V = [ v2,v3,v4,v5,v6,v7,v8,v9,v10, v11,v12,v13,v14,v15,v16,v17,v18,v19,v20 ]
DEV_VOWELS = ['ा', 'ॅ', 'ॉ', 'ि', 'ी', 'ु', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः']
ISO_DEV_VOWELS = [ 'ā', 'æ', 'ɒ', 'i', 'ī', 'u', 'ū', 'e','ē', 'ai','o', 'ō', 'au', 'r̥','r̥̄' , 'l̥', 'l̥̄', 'ṁ', 'ḥ']

print(D_V)

len(D_V)
len(DEV_VOWELS)
len(ISO_DEV_VOWELS)

for i,j,k in zip(D_V, DEV_VOWELS, ISO_DEV_VOWELS):
    print(i,j,k)


DEV_VOWELS = list()
DEV_VOWELS =[ v2[1], v3[1] , v4[1], v5[1], v6[1], v7[1], v8[1], v9[1], v10[1], v11[1], v12[1], v13[1], v14[1], v15[1], v16[1], v17[1], v18[1], v19[1], v20[1] ]
print(DEV_VOWELS)


"""
for c in consonants:
    print(c, end= '   ')
    for v in vowels:
        print(c+v, end = '   ')
    print()
"""    

    
def create_dict(c):
    d = [c]
    for v in DEV_VOWELS:
        d.append(c+v)
    
    return d
    

## ka
dict_ka = create_dict(c1)
print(dict_ka)

dict_kha = create_dict(c2)
print(dict_kha)

dict_ga = create_dict(c3)
print(dict_ga)

dict_gha = create_dict(c4)
print(dict_gha)


## cha
dict_ca = create_dict(c5)
print(dict_ca)

dict_cha = create_dict(c6)
print(dict_cha)

dict_ja = create_dict(c7)
print(dict_ja)

dict_jha = create_dict(c8)
print(dict_jha)


## ta
dict_ta = create_dict(c9)
print(dict_ta)

dict_tha = create_dict(c10)
print(dict_tha)

dict_da = create_dict(c11)
print(dict_da)

dict_dha = create_dict(c12)
print(dict_dha)

dict_na = create_dict(c13)
print(dict_na)

## taa, thaa, daa, dhaa, naa
dict_taa = create_dict(c14)
print(dict_taa)

dict_thaa = create_dict(c15)
print(dict_thaa)

dict_daa = create_dict(c16)
print(dict_daa)

dict_dhaa = create_dict(c17)
print(dict_dhaa)

dict_naa = create_dict(c18)
print(dict_naa)


## pa, pah , ba, bha, ma
dict_pa = create_dict(c19)
print(dict_pa)

dict_pha = create_dict(c20)
print(dict_pha)

dict_ba = create_dict(c21)
print(dict_ba)

dict_bha = create_dict(c22)
print(dict_bha)

dict_ma = create_dict(c23)
print(dict_ma)


## ya, ra, la, va
dict_ya = create_dict(c24)
print(dict_ya)

dict_ra = create_dict(c25)
print(dict_ra)

dict_la = create_dict(c26)
print(dict_la)

dict_va = create_dict(c27)
print(dict_va)


## sha, shaa , sa
dict_sha = create_dict(c28)
print(dict_sha)

dict_shaa = create_dict(c29)
print(dict_shaa)

dict_sa = create_dict(c30)
print(dict_sa)

## ha, lha
dict_ha = create_dict(c31)
print(dict_bha)

dict_lha = create_dict(c32)
print(dict_lha)

##############################
dict_a = ['अ' , 'आ' ,'अॅ',  'ऑ',  'ऒ', 'ओ', 'औ', 'अं', 'अः']
dict_i = ['इ',  'ई' ]
dict_u = [ 'उ' , 'ऊ' ]
dict_e = ['ऎ',  'ए', 'ऐ' ]
dict_ru = ['ऋ', 'ॠ' ]
###############################
"""
dict_a = create_dict(c40)
print(dict_a)

dict_i = create_dict(c41)
print(dict_i)

dict_u = create_dict(c42)
print(dict_i)
dict_e = create_dict(c43)
print(dict_e)

dict_ru = create_dict(c44)
print(dict_ru)
"""
###############################

######################################################################################
combine_dict_alpha = [dict_ka, dict_kha, dict_ga, dict_gha, dict_ca, dict_cha, dict_ja, dict_jha, 
                      dict_ta, dict_tha, dict_da, dict_dha, dict_na, dict_taa, dict_thaa, dict_dhaa, dict_naa,
                      dict_pa, dict_pha, dict_ba, dict_bha, dict_ma, dict_ya, dict_ra, dict_la, dict_va,
                      dict_sha, dict_shaa, dict_sa, dict_ha, dict_lha, dict_a, dict_i, dict_u, dict_e,
                      dict_ru]
"""
for d in combine_dict_alpha:
    index = combine_dict_alpha.index(d)
    print(index,d)
"""
print("")