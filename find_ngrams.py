import os
import re
#from rostow_text_for_tagging import clean_up_text
import nltk
from nltk import *
from collections import Counter
import pickle
import matplotlib.pyplot as plt


def grab_all_cognates(words, counter):
    total = float(0)
    for w in words:
        print (w)
        total += counter[w]
    return total

def ngrams_by_year_helper(word):
    words = [tuple(w.split(" ")) for w in word]
    return words

##return the counts of one-grams by year
def ngrams_by_year(word, gram, lemat_bool):
    if lemat_bool:
        root = "/Users/eunseo/Projects/rostow_network/lemat_pickles"
    else:
        root = "/Users/eunseo/Projects/rostow_network/pickles_for_ngrams"
    files = os.listdir(root)
    selected_paths = [os.path.join(root, f) for f in files if f[0] == str(gram)]
    selected_paths.sort(key=lambda path: int(path[-4:]))
    #print selected_paths
    all_counts = []
    if gram > 1:
        word = ngrams_by_year_helper(word)
    for path in selected_paths:
        tup = pickle.load(open(path, "r"))
        counter = tup[0]
        wc = tup[1]
        total_words = grab_all_cognates(word, counter)
        tup_to_append = (float(total_words/wc), path[-5:])
        all_counts.append(tup_to_append)
    return all_counts

def graph_ngrams(word, rel_freq):
    x = []
    y = []

    for freq in rel_freq:
        x.append(int(freq[1][1:]))
        y.append(freq[0])
    pickle.dump((x,y), open(word,"w"))
    xlabels = [year for year in x if year%5==0]
    plt.plot(x,y)
    plt.xticks(xlabels, xlabels, rotation='vertical')
    plt.title(word)
    plt.savefig(word)

    # fig, ax = plt.subplots()
    # ax.plot(x, y)
    # plt.savefig(word)


if __name__ == "__main__":
    word = ["mass consumption"]
    rel_freq = ngrams_by_year(word,2, lemat_bool=False)
    file_name = "mass_consumption_lemma"
    print rel_freq
    graph_ngrams(file_name, rel_freq)