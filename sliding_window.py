from itertools import islice
import os
from collections import Counter
import pickle
import itertools

def window(seq, n=4):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def give_files(root):
    return [os.path.join(root, file) for file in os.listdir(root)]

def search_before_after(word, files): #given one word, return 100 char before & after in tokens
    word = word.lower()
    all_tokens = []
    for f in files:
        with open(f, "r") as reader:
            s = reader.read()
            if word in s:
                start = s.index(word)
                end = start + len(word) - 1
                if start < 100:
                    all_tokens.append(s[:start].split())
                else:
                    all_tokens.append(s[start - 100:start].split())
                if end > len(s) -1 :
                    all_tokens.append(s[end:].split())
                else:
                    all_tokens.append(s[end:end+100].split())
    return list(itertools.chain.from_iterable(all_tokens))


def count_relevant_words(tokens, relevant_words):

    total_count = 0
    c = Counter(tokens)
    for r in relevant_words:
        if r in c:
            total_count += c[r]
    print(total_count)
    return (total_count, sum(c.values()))


def iterate_all_countries(relevant_words, countries, root):
    all_scores = {}
    files = give_files(root)
    for c in read_countries(countries):
        print (c)
        tokens = search_before_after(c, files)
        all_scores[c] = count_relevant_words(tokens, relevant_words)
    return all_scores

def read_countries(countries):
    with open(countries, "r") as file:
        countries_list = file.read().split("\n")
    return countries_list

if __name__ == "__main__":
    list_of_words = ["adolescent", "infantile", "child", "childlike", "childlike", "boy", "boyish",
                     "childish",
                     "infant", "girlish", "girl", "pubescent", "embryonic", "fledgling", "developing", "develop",
                     "growing",
                     "burgeoning", "nascent", "young", "budding", "juvenile", "baby", "babyish"]

    root = "/Users/eunseo/Desktop/frequency_tools/years"
    countries = "/Users/eunseo/Desktop/gender_chapter/most_common_500"
    pickle.dump(iterate_all_countries(list_of_words, countries, root), open("./test", "wb"))


