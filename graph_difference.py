import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas
import numpy as np
import pickle

pickle_dir1 = "./m_pronouns"
pickle_dir2 = "./f_pronouns"
data1 = pickle.load(open(pickle_dir1, "rb")) #tuple of (x,y)
data2 = pickle.load(open(pickle_dir2, "rb"))

years = data1[0]
freq = np.array(data1[1]) - np.array(data2[1])

df = pandas.DataFrame({"years": years, "freq": freq})

tips = sns.load_dataset("tips")

slope, intercept, r_value, p_value, std_err = stats.linregress(years, freq) #simple linear regression
with open("stats_diff_f_m_pronouns", "w") as writefile:
    writefile.write("slope: " + str(slope) + "\n" +
                    "intercept: "+ str(intercept) + "\n" +
                    "r_value: " + str(r_value) + "\n" +
                    "p_value: " + str(p_value) + "\n" +
                    "std_error: " + str(std_err) + "\n")

ax = sns.regplot(x="years", y="freq", data=df)
plt.title("diff")
plt.savefig("figure_diff_f_m_pronouns")
plt.show()


#graph diff in two sets of data over years
