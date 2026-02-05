import time
import json
import os
import requests

LOG_FILE = "/var/log/app/app.log"

AGGREGATOR_URL = os.environ.get("LOG_AGGREGATOR_URL")
SERVICE_NAME = os.environ.get("SERVICE_NAME")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

def follow(file):
    file.seek(0, 2)  # go to end of file
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line

while not os.path.exists(LOG_FILE):
    time.sleep(1)

with open(LOG_FILE, "r") as logfile:
    for line in follow(logfile):
        try:
            log = json.loads(line.strip())
            log["service_name"] = SERVICE_NAME
            log["environment"] = ENVIRONMENT

            requests.post(AGGREGATOR_URL, json=log, timeout=2)
        except Exception as e:
            print("Error processing log:", e)
