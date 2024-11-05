import requests
import json
import os
from datetime import datetime

payload = {
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'deployment_version': os.environ['GITHUB_SHA'][:8],
    'app_name': os.environ['INPUT_APP_NAME'],
    'rollback_version': os.environ.get('ROLLBACK', 'default_version')
}

#endpoint = os.environ['INPUT_APP_ENDPOINT']
endpoint = 'https://europe-west1-hw-sre.cloudfunctions.net/deployments'
headers = {'Content-Type': 'application/json'}

response = requests.post(endpoint, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print("Payload sent successfully!")
else:
    print(f"Failed to send payload. Status code: {response.status_code}")
