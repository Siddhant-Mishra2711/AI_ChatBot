# 🧠 Stock Price Prediction Chatbot

This is a full-stack AI chatbot that answers stock price prediction queries. It uses Python, Flask, NLTK for NLP, and a simple frontend with HTML/CSS/JS. You can extend it with real prediction models like LSTM or use mock logic for demo purposes.

---

## 🚀 Features

- Intent classification using Naive Bayes and NLTK
- Entity extraction (stock tickers like AAPL, TSLA)
- Flask backend API
- Clean frontend chat interface
- Dockerized for easy deployment

---

## 📁 Project Structure

AI Chatbot/
├── backend/
│ ├── app.py # Flask app
│ ├── chatbot.py # Intent + response logic
│ ├── stock_predictor.py # Predicts (mocked) stock prices
│ ├── train_model.py # Model trainer
│ ├── intents.json # Training data
│ └── Dockerfile
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── style.css
├── requirements.txt
└── README.md

---

## 🛠️ Installation

### 🔧 Local Setup

1. **Install dependencies**

```bash
pip install -r requirements.txt

2. **Install dependencies**

pip install -r requirements.txt

3. **Train the model**

python backend/train_model.py

4.**Start the backend server**

python backend/app.py

5.**Open the chatbot frontend**

Simply open frontend/index.html in your browser.


```🐳 Docker Deployment
Build and run the app using Docker:

docker build -t stock-chatbot .
docker run -p 5000:5000 stock-chatbot
