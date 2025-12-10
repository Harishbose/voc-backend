
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Path to the JSON file created from Excel
DATA_FILE = os.path.join(os.path.dirname(__file__), "reviews.json")

@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "reviews.json not found"}), 404

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data)

@app.route("/", methods=["GET"])
def home():
    return "Backend is running! Use /api/reviews to fetch data."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
