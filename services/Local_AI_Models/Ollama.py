import ollama
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "model.json")

with open(mode="r", file=DATA_PATH) as file:
    odel = json.load(file)["model"]


def answer(data):

    try:
        response = ollama.chat(model=odel, messages=[
            {
                'role': 'system',
                'content': (
                    "You are a financial analysis expert. When given data, you will analyze it and respond in the following format:\n"
                    '{ "0": { "title": "TITLE_HERE", "summary": "SUMMARY_HERE", '
                    '"category": "CATEGORY_HERE", "importance": "IMPORTANCE_HERE" } }\n'
                    "Allowed categories: [Economy, Finance, Markets, Investing, Technology, Science]\n"
                    "Allowed importance levels: [low, medium, high]*importance should be lowercased*"
                )
            },
            {
                'role': 'user',
                'content': f"This is the data that you are given: {data}"
            }
        ])
        response = response.message.content
        response = response.replace("\n", " ")
        response = response.replace('\"', '"')
    except Exception as e:
        print(
            f"couldn't get accessed to the local-ai, check ollama and try again: {e}")

    return (response)


def priceDetermine(data: list):

    try:
        response = ollama.chat(model=odel, messages=[
            {
                'role': 'user',
                'content': (
                    f"""
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
۴. ** خروجی خودت رو به صورت کد Markdown بهم بده
یافته‌های خود را به صورت یک گزارش مختصر و حرفه‌ای ارائه کن.
"""
                )
            }
        ])
        print("gemini response: ", response)
        return response

    except:
        print("couldn't get accessed to the gemini, check your network and try again")
        return None
