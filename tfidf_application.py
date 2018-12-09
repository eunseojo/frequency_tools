import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import numpy as np


directory_path = "/Users/eunseo/Desktop/tokenized_text"
all_docs = sorted([os.path.join(directory_path, f) for f in os.listdir(directory_path)])
all_docs = all_docs[:200] #test with first 200
#print(all_docs)
corpus = []
for doc in all_docs:
    with open(doc, "r") as f:
        corpus.append(f.read())

new_regex = r"(?u)\b\w+\b"
tfidf = TfidfVectorizer(token_pattern=new_regex, use_idf=False)


transformed_vect = tfidf.fit(corpus)
#print(tfidf.transform(corpus))
X = tfidf.transform(corpus).toarray()
print(X)
sum_across_vocab = np.sum(X, axis=0, keepdims=True)
var_across_vocab = np.var(X, axis=0, keepdims=True)
print(sum_across_vocab.shape)
sorted_indices = np.fliplr(np.argsort(sum_across_vocab))

print(sorted_indices)

for i in sorted_indices[0][-50:]:
    print(tfidf.get_feature_names()[i])