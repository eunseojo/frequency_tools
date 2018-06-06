import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
from scipy import stats
import pandas
import pickle
from numpy.polynomial import polynomial as P

pickle_dir = "./he"
data = pickle.load(open(pickle_dir, "rb")) #tuple of (x,y)
df = pandas.DataFrame({"years": data[0], "freq": data[1]})

tips = sns.load_dataset("tips")

slope, intercept, r_value, p_value, std_err = stats.linregress(data[0], data[1]) #simple linear regression



with open("stats_"+pickle_dir.split("./")[-1], "w") as writefile:
    writefile.write("slope: " + str(slope) + "\n" +
                    "intercept: "+ str(intercept) + "\n" +
                    "r_value: " + str(r_value) + "\n" +
                    "p_value: " + str(p_value) + "\n" +
                    "std_error: " + str(std_err) + "\n")

ax = sns.regplot(x="years", y="freq", data=df, order=1)
plt.title(str(pickle_dir.split("./")[-1]))
plt.savefig("figure_"+pickle_dir.split("./")[-1])
plt.show()