import os
import re
#from rostow_text_for_tagging import clean_up_text
import nltk
from nltk import *
from collections import Counter
import pickle
import matplotlib.pyplot as plt
import numpy as np


def grab_all_cognates(words, counter):
    print(words)
    return counter[words]

def ngrams_by_year_helper(word):
    return tuple(word.split(" "))

##return the counts of one-grams by year
def ngrams_by_year(word, gram, lemat_bool):
    if lemat_bool:
        root = "/Users/eunseo/Desktop/frequency_tools/lemmat_pickles"
    else:
        root = "/Users/eunseo/Desktop/frequency_tools/pickles"
    files = os.listdir(root)
    selected_paths = [os.path.join(root, f) for f in files if f[0] == str(gram)]
    selected_paths.sort(key=lambda path: int(path[-4:]))
    #print selected_paths
    all_counts = []
    if gram > 1:
        word = ngrams_by_year_helper(word)
    for path in selected_paths:
        tup = pickle.load(open(path, "rb"))
        counter = tup[0]
        wc = tup[1]
        total_words = grab_all_cognates(word, counter)
        tup_to_append = (float(total_words/wc), path[-5:])
        all_counts.append(tup_to_append)
    return all_counts[80:]

def graph_ngrams(word, rel_freq):
    x = []
    y = []

    for freq in rel_freq:
        x.append(int(freq[1][1:]))
        y.append(freq[0])
    pickle.dump((x,y), open(word,"wb"))
    xlabels = [year for year in x if year%5==0]
    plt.plot(x,y)
    plt.xticks(xlabels, xlabels, rotation='vertical')
    plt.title(word)
    plt.savefig(word)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.savefig(word)


def ngrams_multiple_words(list_words, filename):   #only works for single words
    frequencies = []
    years = []
    for w in list_words:
        freq = ngrams_by_year(w, 1, lemat_bool=False)
        f, y = zip(*freq)
        years = y
        frequencies.append(f)
    freq = np.array(frequencies)
    print(freq.shape)
    freq = np.sum(freq, axis=0)
    print(freq.shape)
    zipped = zip(freq, years)
    graph_ngrams(filename, zipped)


if __name__ == "__main__":
    # word = ["self determination"]
    # n = len(word[0].split())
    # rel_freq = ngrams_by_year(word, n, lemat_bool=False) ###lemat bool determines - it is looking at the lemmatized files
    # file_name = "_".join(word)
    # print (rel_freq)
    # graph_ngrams(file_name, rel_freq)


    list_of_words = ["adolescent", "mature", "infantile", "child", "childlike", "childlike", "boy", "boyish", "childish", "adult",
                     "infant", "girlish", "girl", "pubescent", "embryonic", "fledgling", "developing", "develop", "growing",
                     "burgeoning", "nascent", "young", "budding", "juvenile", "baby", "babyish"]

    female_pronouns = ["she", "her", "hers", "herself"]
    male_pronouns = ["he", "his", "himself"]


    ngrams_multiple_words(female_pronouns, "f_pronouns")
    ngrams_multiple_words(male_pronouns, "m_pronouns")