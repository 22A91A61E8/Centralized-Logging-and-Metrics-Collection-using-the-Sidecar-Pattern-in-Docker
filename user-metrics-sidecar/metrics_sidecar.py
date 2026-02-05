import os, time, requests
from flask import Flask, Response
import threading

APP_METRICS_URL = os.environ['APP_METRICS_URL']
SERVICE_NAME = os.environ['SERVICE_NAME']
ENVIRONMENT = os.environ['ENVIRONMENT']

metrics_data = ""
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return Response(metrics_data, mimetype='text/plain')

def scrape_metrics():
    global metrics_data
    while True:
        try:
            r = requests.get(APP_METRICS_URL)
            lines = r.text.splitlines()
            enriched = []
            for line in lines:
                if line.startswith("#"):
                    enriched.append(line)
                else:
                    parts = line.split(" ")
                    metric, value = parts[0], parts[1]
                    enriched.append(f'{metric},service_name="{SERVICE_NAME}",environment="{ENVIRONMENT}" {value}')
            metrics_data = "\n".join(enriched)
        except:
            metrics_data = ""
        time.sleep(15)

if __name__ == '__main__':
    t = threading.Thread(target=scrape_metrics)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=9100)

