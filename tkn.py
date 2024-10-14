import requests
from Tools.scripts.fixdiv import report

def get_token():
    rq = '''username=guest&password=1'''

    url = 'http://localhost:8000/auth/token'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=rq)
    return response.json()["access_token"]
