# Text Classifier Service

TF-IDF unigram/bigram logistic-regression classifier with 20 Newsgroups training, cross-validation, joblib persistence, validated FastAPI top-three predictions, health and Prometheus metrics, container packaging and Locust load scenario.

## Run

Install requirements.txt, run `python train.py`, then `uvicorn app:app`. The training command downloads 20 Newsgroups and prints measured CV results. `pytest` trains a tiny fixture without downloading data.
