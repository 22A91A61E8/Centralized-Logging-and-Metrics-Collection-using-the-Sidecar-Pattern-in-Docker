from flask import Flask, request, jsonify

app = Flask(__name__)

# store last 10 logs in memory
logs = []

@app.route("/logs", methods=["POST"])
def receive_logs():
    data = request.json
    if not data:
        return {"error": "Invalid log"}, 400

    logs.append(data)
    if len(logs) > 10:
        logs.pop(0)

    return "", 202   # Accepted

@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs), 200

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
