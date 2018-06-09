import pickle
import matplotlib.pyplot as plt
import numpy as np


''''
This will graph your PICKLES' relative frequencies
'''''



def graph_multiple(paths, labels, fig_name):
    fig, ax = plt.subplots()

    for path in zip(paths, labels):
        data = load_data(path[0])
        ax.plot(data[0], data[1], label=path[1])
    plt.legend()
    plt.savefig(fig_name)
    plt.show()

def load_data(path):
    data = pickle.load(open(path, "r"))
    return data


if __name__ == "__main__":

    paths = ["/Users/eunseo/Projects/rostow_network/pickles_and_images/modernize",
             "/Users/eunseo/Projects/rostow_network/pickles_and_images/technology",
             "/Users/eunseo/Projects/rostow_network/pickles_and_images/culture"]

    labels = ["modernize, modernization", "technology, technological", "culture, cultural"]
    fig_name = "combo_tech_cul.png"
    graph_multiple(paths, labels, fig_name)
