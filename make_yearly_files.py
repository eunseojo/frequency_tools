import os
import re
import nltk
from nltk import *
from collections import Counter
import pickle
import matplotlib.pyplot as plt



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



if __name__ == "__main__":
    #build:
    root_path = "/Users/eunseo/Desktop/tokenized_text"
    year_dir = "/Users/eunseo/Desktop/frequency_tools/years"
    dates = make_list_dates(root_path)
    make_textfiles(year_dir, dates)