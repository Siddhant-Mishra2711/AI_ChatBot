from flask import Flask, request, jsonify
from chatbot import get_response
from stock_predictor import predict_stock

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    response = get_response(user_msg)
    if "Fetching prediction for" in response:
        ticker = response.split("for ")[1].replace("...", "")
        prediction = predict_stock(ticker)
        return jsonify({"response": f"{response} Predicted price: ${prediction}"})
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)