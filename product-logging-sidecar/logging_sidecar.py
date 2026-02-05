import os, time, json, requests

LOG_FILE = '/var/log/app/app.log'
AGGREGATOR_URL = os.environ['LOG_AGGREGATOR_URL']
SERVICE_NAME = os.environ['SERVICE_NAME']
ENVIRONMENT = os.environ['ENVIRONMENT']

with open(LOG_FILE) as f:
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue
        try:
            log = json.loads(line)
            log['service_name'] = SERVICE_NAME
            log['environment'] = ENVIRONMENT
            requests.post(AGGREGATOR_URL, json=log)
        except:
            continue
