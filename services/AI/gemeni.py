from google import genai
import json
import os
#  run this command     pip install -q -U google-genai     then...
# create a file with the name of  (gmkey.json) in the same folder with this file and inside that  type this    {    'key': ''your gemeni API key"    }

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')


def analyze(data: str):
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        key = json.load(file)
    try:
        client = genai.Client(api_key=key['key'])
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'''
            این اطلاعات رو تحلیل کن اون هایی که ارزش تحلیل ندارن رو کنار بزار و باقی مونده ها رو درنظر بگیر و تحلیل کن  میتونی اونهایی که به هم مرتبط هستن رو بکی کنی (برای من مهم کیفیته نه کمیت ) تمام این مقدار ها باید برابر همون جیزی باشن که در کلیدشون ذکر شده و هیج گونه پیام یا کامنتی نزار اگه یه موردی نصفه نیمه بود اون رو هم حساب نکن . درنهایت مانند جیسونی که فرستادم خروجی بده
            : {{ "0": {{ "title": "TITLE_HERE", "summary": "SUMMARY_HERE", "category": "CATEGORY_HERE", "importance": "IMPORTANCE_HERE" }} }}
              اطلاعات ورودی: {data},
            "remember, these are the only categories that you can assign, and each answer can only have one category: [Economy, Finance, Markets, Investing, Technology, Science]"
'''
        )
        print("gemini response: ", response)
        return str(response)

    except:
        print("couldn't get accessed to the gemini, check your network and try again")
        return None


def priceDetermine(data:list):
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        key = json.load(file)

    try:
        client = genai.Client(api_key=key['key'])
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f'''prompt = f"""
به عنوان یک تحلیل‌گر متخصص بازار، با توجه به تحلیل اخباری که به تازگی انجام دادی، داده‌های زیر را بررسی کن.

داده‌های هفته گذشته:
- ارزهای دیجیتال: {data[0]}
- ارزهای رایج (فیات): {data[1]}

داده‌های امروز:
- ارزهای دیجیتال: {data[2]}
- ارزهای رایج (فیات): {data[3]}

وظایف شما:
۱. **تشخیص تغییرات مهم:** مهم‌ترین جهش‌ها، سقوط‌ها یا ناهنجاری‌های قیمتی را در هر دو بازار مشخص کن.
۲. **تحلیل و ارتباط‌دهی:** دلایل احتمالی این تغییرات را با مرتبط کردن آن‌ها به موضوعات خبری اخیر (مانند تورم، تحریم‌ها، اعلانات فناوری) به طور خلاصه توضیح بده.
۳. **پیش‌بینی آینده:** یک پیش‌بینی کوتاه و آینده‌نگر در مورد احساسات حاکم بر بازار و مسیر احتمالی دارایی‌های کلیدی در ۲۴ تا ۴۸ ساعت آینده ارائه بده.

یافته‌های خود را به صورت یک گزارش مختصر و حرفه‌ای ارائه کن.
"""'''
        )
        print("gemini response: ", response)
        return str(response)

    except:
        print("couldn't get accessed to the gemini, check your network and try again")
        return None
