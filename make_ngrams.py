import os
import re
#from rostow_text_for_tagging import clean_up_text
import nltk
from nltk import *
from collections import Counter
import pickle



def pickle_helper(text_path, gram):
    text = ""
    with open(text_path, "r") as f:
        text = f.read()
    token = nltk.word_tokenize(text)
    word_count = len(token)
    if gram == 1:
        return Counter(token), word_count
    elif gram == 2:
        return Counter(nltk.ngrams(token,2)), word_count
    elif gram == 3:
        return Counter(nltk.ngrams(token,3)), word_count
    elif gram == 4:
        return Counter(nltk.ngrams(token,4)), word_count

def pickle_ngrams(root, pickles):
    if not os.path.isdir(pickles):
        os.makedirs(pickles)
    ngram_types = [1,2,3,4]
    filepaths = [os.path.join(root, f) for f in os.listdir(root)]

    for i in ngram_types:
        for path in zip(filepaths, os.listdir(root)):
            tup = (pickle_helper(path[0], i))
            pickle.dump(tup, open(os.path.join(pickles, str(i) + path[1]),"wb"))


if __name__ == "__main__":
    root_dir = "/Users/eunseo/Desktop/frequency_tools/years"
    pickles_dir = "/Users/eunseo/Desktop/frequency_tools/pickles"
    pickle_ngrams(root_dir, pickles_dir)

