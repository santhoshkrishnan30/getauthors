from flask import Flask, jsonify
import os
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*', allow_headers=['Content-Type', 'Authorization'])
app.config['SECRET_KEY'] = os.urandom(24)
port = int(os.environ.get('PORT', 5002))

# File path for the authors JSON file
AUTHORS_FILE = os.path.join(os.path.dirname(__file__), 'authors.json')

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice for Authors"

@app.route('/authors', methods=['GET'])
def get_authors():
    try:
        with open(AUTHORS_FILE, 'r') as f:
            authors_data = json.load(f)
        return jsonify(authors_data), 200
    except FileNotFoundError:
        return jsonify({'error': 'Authors file not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Error decoding JSON file'}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
