import pickle
import matplotlib.pyplot as plt
import numpy as np
import os


''''
This will graph your PICKLES' relative frequencies
'''''


def graph_multiple(paths, labels, fig_name):
    fig, ax = plt.subplots()
    avgs = []
    read_data = {}
    for path in zip(paths, labels):
        data = load_data(path[0])
        avg = np.mean(data[1])
        avgs.append((path[1],avg))
        read_data[path[1]] = data

    sorted_avgs = sorted(avgs, key=lambda x: x[1], reverse=True)

    for _ in range(6):
        data = read_data[sorted_avgs[_][0]]
        ax.plot(data[0], data[1], label=sorted_avgs[_][0])

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(fig_name)
    plt.show()

def load_data(path):
    data = pickle.load(open(path, "rb"))
    return data


if __name__ == "__main__":
    list_of_words = ["adolescent", "mature", "infantile", "child", "childlike", "childlike", "boyish",
                     "childish",
                     "girlish", "pubescent", "embryonic", "fledgling", "developing", "develop",
                     "growing",
                     "burgeoning", "nascent", "young", "budding", "juvenile", "babyish"]
    root = "/Users/eunseo/Desktop/frequency_tools/"
    paths = [os.path.join(root, w) for w in list_of_words]

    fig_name = "developing_all.png"
    graph_multiple(paths, list_of_words, fig_name)
