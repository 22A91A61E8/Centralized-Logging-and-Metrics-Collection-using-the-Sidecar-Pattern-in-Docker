from flask import Flask, jsonify
import logging
import os
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

os.makedirs("/var/log/app", exist_ok=True)

logging.basicConfig(
    filename='/var/log/app/app.log',
    level=logging.INFO,
    format='{"level":"%(levelname)s","message":"%(message)s","timestamp":"%(asctime)s"}'
)

REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP requests', ['method', 'path'])

@app.route('/health')
def health():
    REQUEST_COUNTER.labels(method='GET', path='/health').inc()
    return "OK", 200

@app.route('/metrics')
def metrics():
    return generate_latest(REQUEST_COUNTER), 200, {'Content-Type': 'text/plain'}

@app.route('/test')
def test_log():
    logging.info('Test log from order-service')
    REQUEST_COUNTER.labels(method='GET', path='/test').inc()
    return jsonify({"status":"logged"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003)
