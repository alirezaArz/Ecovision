from google import genai
import json
import os
#  run this command     pip install -q -U google-genai     then...
# create a file with the name of  (gmkey.json) in the same folder with this file and inside that  type this    {    'key': ''your gemeni API key"    }  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')

def analyze(data:str):
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        key = json.load(file)

    client = genai.Client(api_key=key['key'])
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents = f'''این اطلاعات رو تحلیل کن اون هایی که ارزش تحلیل ندارن رو کنار بزار و باقی مونده ها رو درنظر بگیر و تحلیل کن  میتونی اونهایی که به هم مرتبط هستن رو بکی کنی (برای من مهم کیفیته نه کمیت ) تمام این مقدار ها باید برابر همون جیزی باشن که در کلیدشون ذکر شده و هیج گونه پیام یا کامنتی نزار اگه یه موردی نصفه نیمه بود اون رو هم حساب نکن . درنهایت مانند جیسونی که فرستادم خروجی بده: {{ "0": {{ "title": "TITLE_HERE", "summary": "SUMMARY_HERE", "category": "CATEGORY_HERE", "importance": "IMPORTANCE_HERE" }} }} اطلاعات ورودی: {data}'''
    )
    return response


