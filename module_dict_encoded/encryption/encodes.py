import combinations
#########################################################################
#0 to 9
DIGITS = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
ISO_DIGITS = [ '0', '1', '2', '3','4','5','6','7','8','9']


#########################################################################
#VOWELS
#13 vowels in Marathi,

STD_VOWELS = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ',     'ऋ',  'ॠ',  'ऌ' , 'ॡ', 'अं',  'अः', 'अँ',  'ऽ'   ]
ISO_STD_VOWELS = [ 'a', 'ā', 'i', 'ī', 'u', 'ū', 'ē', 'ai', 'ō', 'au', 'r̥','r̥̄' , 'l̥', 'l̥̄', 'ṁ	', 'ḥ', 'm̐' , '’' ]


DEV_VOWELS = ['ा', 'ॅ', 'ॉ', 'ि', 'ी', 'ु', 'ू', 'ॆ', 'े', 'ै', 'ॊ', 'ो', 'ौ', 'ृ', 'ॄ', 'ॢ', 'ॣ', 'ं', 'ः']
ISO_DEV_VOWELS = [ 'ā', 'æ', 'ɒ', 'i', 'ī', 'u', 'ū', 'e','ē', 'ai','o', 'ō', 'au', 'r̥','r̥̄' , 'l̥', 'l̥̄', 'ṁ', 'ḥ']

len(DEV_VOWELS)
len(ISO_DEV_VOWELS)

"""
print(STD_VOWELS)

for i in STD_VOWELS:
    for j in i:
        print(j)

print(DEV_VOWELS)
print(ISO_DEV_VOWELS)

"""
#########################################################################
#Using (IAST) these vowels can be represented as:
IAST_REPRESENTATION_VOWELS = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'e', 'ai', 'o', 'au', 'ae', 'ao']



#########################################################################
#CONSONENTS
# corresponding consonant

VELAR_CONSONANTS = ['क', 'ख', 'ग', 'घ', 'ङ']
PALATAL_CONSONANTS = ['च', 'छ', 'ज', 'झ', 'ञ']
RETROFLEX_CONSONANTS = ['ट','ठ', 'ड', 'ढ', 'ण']
DENTAL_CONSONANTS = ['त', 'थ', 'द', 'ध', 'न']
LABIAL_CONSONANTS = ['प', 'फ', 'ब', 'भ', 'म']

IAST_VELAR_CONSONANTS = ['k', 'kh', 'g', 'gh', 'ṅ']
IAST_PALATAL_CONSONANTS = ['c', 'ch', 'j', 'jh', 'ñ']
IAST_RETROFLEX_CONSONANTS = ['ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ']
IAST_DENTAL_CONSONANTS = ['t', 'th', 'd', 'dh', 'n']
IAST_LABIAL_CONSONANTS = ['p', 'ph', 'b', 'bh', 'm']


ISO_velar_C = [ 'ka', 'kha', 'ga', 'gha', 'ṅa' ]
ISO_palatal_C = [ 'ca', 'cha', 'ja', 'jha','ña'   ]
ISO_retroflex_C = [ 'ṭa', 'ṭha', 'ḍa', 'ḍha', 'ṇa'  ]
ISO_dental_C = [ 'ta', 'tha', 'da' , 'dha', 'na']
ISO_labial_C = [ 'pa', 'pha', 'ba', 'bha', 'ma' ]




#########################################################################
#semi vowels in marathi
SEMI_VOWELS = ['य', 'र', 'ल', 'व']
IAST_SEMI_VOWELS = ['y', 'r', 'l', 'w']

ISO_semi_V = [ 'ya', 'ra', 'la', 'va' ]


#sibilants in marathi
SIBILANTS = ['श', 'ष', 'स']
IAST_SIBILANTS = ['ś', 'ṣ', 's']
ISO_semi_sibilants = [ 'śa', 'ṣa', 'sa']


#fricative consonant in marathi
FRIACTIVE_CONSONANTS = ['ह']
IAST_FRIACTIVE_CONSONANTS = ['h']
ISO_friactive_C = [ 'ha' ]



#additional consonants:
ADDITIONAL_CONSONANTS = ['ळ', 'क्ष', 'ज्ञ']
IAST_ADDITIONAL_CONSONANTS = ['La', 'kSha', 'dnya']

ISO_additional_C = [ 'kṣa', 'tra', 'jña', 'śra' ]



######################################################################################
######################################################################################

List_of_DEV_C = [ VELAR_CONSONANTS, PALATAL_CONSONANTS , RETROFLEX_CONSONANTS, DENTAL_CONSONANTS,
                 LABIAL_CONSONANTS,SEMI_VOWELS, SIBILANTS, FRIACTIVE_CONSONANTS, ADDITIONAL_CONSONANTS ]


List_of_ISO_C= [ ISO_velar_C, ISO_palatal_C, ISO_retroflex_C, ISO_dental_C, ISO_labial_C,
                ISO_semi_V, ISO_semi_sibilants, ISO_friactive_C, ISO_additional_C ]


print()
"""
for i,j in zip( List_of_DEV_C, List_of_ISO_C):
    for l,m in zip( i,j ):
        print(l +  "     "+ m)
    print()


""" 
print()
