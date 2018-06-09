import nltk
from nltk.collocations import *
from nltk import FreqDist
from nltk import ngrams
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords


stop = set(stopwords.words('english'))

text_file1 = "./years/1950"  #rostovian language
text_file2 = "./years/1951"

def print_bigrams(given_word, text_path):

    text = ""
    with open(text_path, "r") as f:
        text = f.read()
    tokens = nltk.word_tokenize(text)
    fdist=FreqDist(tokens)
    print (fdist.most_common(1000))
    tokens = nltk.wordpunct_tokenize(text)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokens)
    scored = finder.score_ngrams(bigram_measures.raw_freq)

    #s = sorted(finder.above_score(bigram_measures.raw_freq,40.0 / len(tuple(nltk.trigrams(tokens)))))
    s = sorted(bigram for bigram, score in scored)
    results = []
    for i in s:
        if i[0] == given_word: #or i[1] == given_word:
            if len(results) < 100:
                results.append(i)
            else:
                break
    #print results


def give_pos_tag(text_path):
    text = ""
    with open(text_path, "r") as f:
        text = f.read()

    tagged = nltk.pos_tag(nltk.word_tokenize(text))
    print (tagged)

def print_ngrams(text_path):
    print (text_path)
    text = ""
    with open(text_path, "r") as f:
        text = f.read()
    token = nltk.word_tokenize(text)
    bigrams = ngrams(token,2)
    trigrams = ngrams(token,3)
    fourgrams = ngrams(token,4)
    fivegrams = ngrams(token,5)

    onegram_cter = Counter(token).most_common()
    cter = Counter(bigrams).most_common()

    for count,value in enumerate(cter):

        if value[0][0] == "increase":
            if value[1] > 10:
                print (value)
        if value[0][1] == "increase":
            if value[1] > 10:
                print (value)

    for count,value in enumerate(onegram_cter):

        if value[0] == "increase":
            print (value)

give_word = "modern"
#print_bigrams(give_word, text_file1)
#print_bigrams(give_word, text_file2)


print_ngrams(text_file1)
print_ngrams(text_file2)
#give_pos_tag(text_file2)