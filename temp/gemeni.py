from google import genai
import json
import os
#  run this command     pip install -q -U google-genai     then...
# create a file with the name of  (gmkey.json) in the same folder with this file and inside that  type this    {    'key': ''your gemeni API key"    }  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')

with open(DATA_PATH, 'r', encoding='utf-8') as file:
    key = json.load(file)

client = genai.Client(api_key=key['key'])
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="hi how are you"
)
print(response.text)

