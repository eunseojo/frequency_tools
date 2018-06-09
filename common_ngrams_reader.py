import nltk
from collections import Counter
import pickle
import os

### print all the collocations produced saved in pickle format by year (from common_ngrams.py)
# EXAMPLE::::
###('1977', [((u'communist', u'states', u'.'), 7), ((u'of', u'the', u'communist'), 7),
# ((u'non', u'communist', u'countries'), 7), ((u'the', u'communist', u'powers'), 6),
# ((u'the', u'communist', u'countries'), 6), ((u'and', u'non', u'communist'), 4),
# ((u'communist', u'nations', u'.'), 4), ((u'the', u'communist', u'world'), 4),
# ((u'to', u'the', u'communist'), 4), ((u'communist', u'countries', u'.'), 4),
# ((u'communist', u'and', u'non'), 4), ((u'.', u'the', u'communist'), 3),
# ((u'communist', u'countries', u'and'), 3), ((u'in', u'communist', u'countries'), 3),
# ((u'the', u'communist', u'nations'), 3), ((u'with', u'any', u'communist'), 3),
# ((u'non', u'communist', u'states'), 3), ((u'any', u'communist', u'regime'), 3),
# ((u'with', u'the', u'communist'), 3), ((u'the', u'communist', u'states'), 3),
# ((u'to', u'communist', u'countries'), 3), ((u'between', u'communist', u'and'), 3),
# ((u'from', u'the', u'communist'), 3), ((u'and', u'communist', u'states'), 3),
# ((u'the', u'then', u'communist'), 2), ((u'the', u'communist', u'party'), 2),
# ((u'the', u'communist', u'regime'), 2), ((u'communist', u'states', u'and'), 2),
# ((u'communist', u'regime', u'.'), 2), ((u'communist', u'influence', u'in'), 2)], 1431722)

'''
This file reads in the common ngrams with given word saved in pickle through common_ngrams.py
'''




file_path = "/Users/eunseo/Desktop/frequency_tools/his_bigrams"
years = pickle.load(open(file_path, "rb"))
for y in years: ##y[1]: list of tuple of tuples
    for tup in y[1]:
        if tup[0][0] == 'his':
            print (y[0], tup)
