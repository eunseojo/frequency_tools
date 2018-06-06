import pickle
from collections import Counter
import matplotlib.pyplot as plt

aa = pickle.load(open("./test","rb"))
normalized_scores = []
for k,v in aa.items():
    if v[1] != 0 :
        normalized_scores.append((k, v[0]/v[1]*1.0))

a , b  = zip(*sorted(normalized_scores, key=lambda x: x[1], reverse=True))
print(a)
fig, ax = plt.subplots(1)
ax.plot(a[:40],b[:40])
ax.tick_params(axis='x', labelsize=7)
fig.autofmt_xdate()
plt.xlabel("Ref")
plt.ylabel("Rel. Freq.")
plt.title("40 Refs in Context of Development")
plt.savefig("references")
plt.show()