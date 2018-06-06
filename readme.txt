Files in here make frequency tools for the FRUS, using the tokenized text. Edited: June 1, 2018.

N-grams
To make ngrams, build the freq files in the following order: 
1) make_yearly_files.py : This file concats all tokenized text of given year; this gets saved in the 'years' directory. 
2) make_ngrams.py : This file creates ngram files in the form of pickles for [1,2,3,4]-grams in the 'pickles' directory. Uses the nltk.ngrams function.
** To make lemmatized ngrams, run:
1) make_yearly_files.py
2) make_pickles_lemmat.py

To call ngrams and and graph freq:
1) find_ngrams.py : This file searches freq of given phrase (up to 4 tokens) and charts relative freq. over the years


Regress Ngram Data
For simple regression of trend of freq. run:
1) regression_plots.py : plots seaborn linear regression to figure_*.png and outputs basic stats to stats_* 

