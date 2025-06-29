import requests
import json

response = requests.get('http://127.0.0.1:8000/api/crypto/?key=admin').json()
print(response)