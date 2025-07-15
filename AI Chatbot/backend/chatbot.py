import json
import random
import nltk
import pickle
import re

with open("backend/intents.json") as file:
    intents = json.load(file)

with open("backend/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def extract_ticker(msg):
    match = re.search(r"\b[A-Z]{2,5}\b", msg)
    return match.group(0) if match else "AAPL"

def predict_intent(msg):
    X_test = vectorizer.transform([msg])
    tag = model.predict(X_test)[0]
    return tag

def get_response(msg):
    tag = predict_intent(msg)
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            if tag == "stock_prediction":
                ticker = extract_ticker(msg)
                return response.replace("{ticker}", ticker)
            return response
    return "I'm not sure how to help with that."