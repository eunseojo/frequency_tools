import nltk
from collections import Counter
import pickle
import os

'''
saves in a pickle common n-grams with given token with corresponding frequency
eg. ((u'independent', u'communist'), 2), ((u'increased', u'communist'), 2), ((u'communist', u'threat'), 2), ((u'go', u'communist'), 2), ((u'all', u'communist'), 2),


'''


def single_year_top_ngrams(co, phrase):
    all_words = Counter()
    for k,v in co.items():
        if contains_word(phrase[0], k):
            all_words[k] = v
    return all_words.most_common()[:50]

def contains_word(word, k):
    for i in k:
        if word == i:
            return True
    return False

def iterate_years(phrase, paths, pickle_path):
    to_pickle = []
    for p in paths:
        f = open(p, "rb")
        co, wc = pickle.load(f)
        to_pickle.append((p[-4:], single_year_top_ngrams(co, phrase),wc, co[tuple(phrase)]))
    pickle.dump(to_pickle, open(pickle_path, "wb"))

if __name__ == "__main__":
    root = "/Users/eunseo/Desktop/frequency_tools/pickles"
    ngram = 2 # start with just two-grams
    paths = [os.path.join(root, file) for file in os.listdir(root) if file[0] == str(ngram)]
    paths.sort()
    #paths = ["/Users/eunseo/rostow_network/years/1952", "/Users/eunseo/rostow_network/years/1962"]
    phrase = ["penetration"]  #start w just single words
    pickle_path = "penetration_ngrams"
    iterate_years(phrase, paths, pickle_path)