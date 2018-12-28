
## AIM :
Operations on Devnagari Language like Tokeniser, Grammer Check, Next word Predictor, Ngram, Stemmer

## Introduction
It is very easy to process a text in English an languate similar to english language, for a Indic languages like Sanskrit, Hinde and Devnagari we have to write a program manually for each operation such as Tokeniser, Stemmer, Grammer Checker and next word Predictor.


### Keywords 
Keywords : Re, Pandas, CSV, Machine Learning

## Tools
PreRequirements :

		 LIBRARIES	: Pandas,Sklearn, Keras,csv.
		 IDE		: spyder

###
		


# procedure to traverse
Procedure : 

	1). Exctraction :
		Dataset is exctrated from iitb website. as well as Devnagari language sites
	2). Preporcessing
		This language datasets is availabe in text files, and Tabular word files and Dictionaries.
		We have to prepare the dictionary  with word counts, stem, and Ngram_words
	3). exicution :
		For each Operation here are Saperate modules which can be imported and run the respective files from respective modules to test work on input text.

# Evaluation Plan

	Tokeniser is an easy task to tokenise the input text paragraph with proper eliminaton Tabs and Newline charector.
	Grammer checking can be done using Ngram, Noisy Channel and some other algorithms
	Next word prediction can be done using Ngram.
	To predict next Charector in word trigrams will give a better results
	To predict next Word in sentese Bigram is good for small sentense but for larger sentense trigrams will work better.
	Stemming is difficult task as there are hundreads of stems availble in Marathi Language.
	Rule base stemmer works well but is available for very few words, and rules can be scripted for valid no of words, once reules are scripted it will works for that set of words.

### key Metrics :

