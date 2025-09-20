from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow GitHub Pages frontend to connect

# Temporary in-memory storage (later you can switch to DB)
data_store = []

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(data_store)

@app.route("/api/data", methods=["POST"])
def add_data():
    new_item = request.json
    data_store.append(new_item)
    return jsonify({"status": "success", "item": new_item}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
