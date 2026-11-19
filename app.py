"""
Cloud-Ready Flask Web API
Student: Ajith Kumar R
Register Number: 192321144
Course: CSA10 Software Engineering
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status": "ONLINE",
        "service": "csa10-flask-cloud-api",
        "version": "1.0.0",
        "student": "Ajith Kumar R (192321144)",
        "cloud_environment": "GitHub Cloud Action Runner",
        "message": "Continuous Integration and Deployment Active"
    }), 200

@app.route("/health")
def health():
    return jsonify({"status": "UP", "health": 100}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
