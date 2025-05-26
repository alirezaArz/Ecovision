from google import genai
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    key = json.load(file)

client = genai.Client(api_key=key['key'])
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="hi how are you"
)
print(response.text)

