import requests
import json
from datetime import datetime
import os

def send_payload():
    url = os.getenv('WEBHOOK_URL')
    payload = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'deployment_version': os.getenv('DEPLOYMENT_VERSION'),
        'app_name': os.getenv('APP_NAME'),
        'app_name': 'today',
        'rollback_version': os.getenv('ROLLBACK_VERSION')

    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')

if __name__ == "__main__":
    send_payload()