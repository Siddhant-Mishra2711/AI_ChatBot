import json
import random
import pickle
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')

with open("backend/intents.json") as file:
    data = json.load(file)

X, y = [], []
for intent in data['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
X_vec = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

with open("backend/model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)