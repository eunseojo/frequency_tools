#make textfiles for every year - build
#get n-grams for every year
import os
import re
#from rostow_text_for_tagging import clean_up_text
import nltk
from nltk import *
from collections import Counter
import pickle
import matplotlib.pyplot as plt


''''
make n-gram pickles and charts n-gram charts
'''''

def get_year(string):
    try:
        year = re.match("(\d\d\d\d).*", string).group(1)

    except:
        year = "0000"
    return year

def make_list_dates(root_path):
    files = os.listdir(root_path)
    paths = [(get_year(f),os.path.join(root_path, f)) for f in files]
    sorted_list = sorted(paths, key=lambda tup: tup[0])
    current = ""
    final_list = []
    current_list = []
    for path in sorted_list:
        if path[0] == "0000":
            continue
        else:
            if current == "":
                current = path[0]
                current_list.append(path)
            else:
                if current == path[0]:
                    current_list.append(path)
                elif current != path[0]:
                    final_list.append(current_list)
                    current_list = []
                    current_list.append(path)
                current = path[0]
    return final_list

#take in sorted and grouped list and make textfiles
def make_textfiles(year_dir, sorted_paths):
    if not os.path.isdir(year_dir):
        os.makedirs(year_dir)
    for group in sorted_paths:
        with open(os.path.join(year_dir, group[0][0]), "w") as fw:
            for file in group:
                with open(file[1], "r") as fr:
                    #cleaned = clean_up_text(fr.read())
                    fw.write(fr.read())
                    fw.write(" ")

def return_ngrams(text_path, given_word):
    text = ""
    with open(text_path, "r") as f:
        text = f.read().decode("utf8")
    token = nltk.word_tokenize(text)
    word_count = len(token)
    #bigrams = nltk.ngrams(token,2)
    #trigrams = nltk.ngrams(token,3)
    #fourgrams = nltk.ngrams(token,4)
    #fivegrams = nltk.ngrams(token,5)

    onegram_cter = Counter(token).most_common()
    #cter = Counter(bigrams).most_common()

    # for count,value in enumerate(cter):
    #
    #     if value[0][0] == "increase":
    #         if value[1] > 10:
    #             print value
    #     if value[0][1] == "increase":
    #         if value[1] > 10:
    #             print value

    for count, value in enumerate(onegram_cter):

        if value[0] == given_word:
            return value, word_count
    return None, None

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
    #print all_counts
    return all_counts

def grab_all_cognates(words, counter):
    total = float(0)
    for w in words:
        print (w)
        total += counter[w]
    return total

def ngrams_by_year_helper(word):
    words = [tuple(w.split(" ")) for w in word]
    return words

def pickle_helper(text_path, gram):
    text = ""
    with open(text_path, "r") as f:
        text = f.read().decode("utf8")
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

def pickle_ngrams():
    root = "/Users/eunseo/rostow_network/years"
    ngram_types = [1,2,3,4]
    filepaths = [os.path.join(root, f) for f in os.listdir(root)]

    for i in ngram_types:
        for path in zip(filepaths, os.listdir(root)):
            tup = (pickle_helper(path[0], i))
            pickle.dump(tup, open(os.path.join("/Users/eunseo/rostow_network/pickles_for_ngrams", str(i) + path[1]),"w"))

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

#def moving_average(x):




if __name__ == "__main__":
    #build:
    root_path = "/Users/eunseo/Desktop/tokenized_text"
    year_dir = "/Users/eunseo/Desktop/frequency_tools/years"
    dates = make_list_dates(root_path)
    make_textfiles(year_dir, dates)

    #pickle_ngrams()

    # word = ["mass consumption"]
    # rel_freq = ngrams_by_year(word,2, lemat_bool=False)
    # file_name = "mass_consumption_lemma"
    # print rel_freq
    # graph_ngrams(file_name, rel_freq)

