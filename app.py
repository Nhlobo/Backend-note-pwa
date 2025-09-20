from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# PostgreSQL connection
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://username:password@host:port/dbname")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/api/data", methods=["GET"])
def get_notes():
    notes = Note.query.all()
    return jsonify([{"id": n.id, "text": n.text, "timestamp": n.timestamp} for n in notes])

@app.route("/api/data", methods=["POST"])
def add_note():
    data = request.json
    note = Note(text=data["text"], timestamp=data["timestamp"])
    db.session.add(note)
    db.session.commit()
    return jsonify({"status": "success", "item": {"text": note.text, "timestamp": note.timestamp}}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
