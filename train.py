import argparse,joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
def pipeline():return make_pipeline(TfidfVectorizer(ngram_range=(1,2),max_features=50000),LogisticRegression(max_iter=1000))
def train():
 d=fetch_20newsgroups(subset="train",remove=("headers","footers","quotes"))
 model=pipeline();scores=cross_val_score(model,d.data,d.target,cv=5)
 print({"accuracy_mean":scores.mean(),"accuracy_std":scores.std()})
 model.fit(d.data,d.target);joblib.dump({"model":model,"labels":d.target_names},"model.joblib")
if __name__=="__main__":train()
