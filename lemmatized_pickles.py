import nltk
from nltk.stem import WordNetLemmatizer
import os
from collections import Counter
import pickle

'''
makes lemmatized n-gram pickles

'''

def iterate_years(paths, dir):
    paths = sorted(paths)
    lemat = WordNetLemmatizer()
    print(len(paths))
    for p in paths:
        f = open(p, "r")
        str = f.read()
        lemat_list = lemmatize_doc(str, lemat) #list of lemmatized words
        pickle_ngrams(lemat_list, p[-4:], dir)

def convert_label(pre_convert):
    if pre_convert[0] == "J":
        return "a"
    elif pre_convert[0] == "N":
        return "n"
    elif pre_convert[0] == "R":
        return "r"
    elif pre_convert[0] == "V":
        return "v"
    else:
        return "X"


def lemmatize_doc(total_str, lemat):
    tokened = nltk.word_tokenize(total_str)
    pos_tagged = nltk.pos_tag(tokened)
    lemmatized = []
    for tagged in pos_tagged:
        #print tagged
        if convert_label(tagged[1]) != "X":
            #print lemat.lemmatize(tagged[0],convert_label(tagged[1]))
            lemmatized.append(lemat.lemmatize(tagged[0],convert_label(tagged[1])))
        else:
            lemmatized.append(lemat.lemmatize(tagged[0]))
    return lemmatized

def pickle_ngrams(lemat_list, year, dir):
    ngram_types = [1,2,3,4]
    for i in ngram_types:
        tup = (pickle_helper(lemat_list, i))
        pickle.dump(tup, open(os.path.join(dir, str(i) + year),"wb"))

def pickle_helper(tokens, gram):
    word_count = len(tokens)
    #print tokens
    if gram == 1:
        #print Counter(tokens)
        return Counter(tokens), word_count
    elif gram == 2:
        return Counter(nltk.ngrams(tokens,2)), word_count
    elif gram == 3:
        return Counter(nltk.ngrams(tokens,3)), word_count
    elif gram == 4:
        return Counter(nltk.ngrams(tokens,4)), word_count

def pickle_with_lemmas(paths, dir):
    iterate_years(paths, dir)

if __name__ == "__main__":
    root = "/Users/eunseo/Desktop/frequency_tools/years"
    dir = "/Users/eunseo/Desktop/frequency_tools/lemmat_pickles"
    if not os.path.isdir(dir):
        os.makedirs(dir)
    paths = [os.path.join(root, file) for file in os.listdir(root)]
    pickle_with_lemmas(paths, dir)