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
    try:
        client = genai.Client(api_key=key['key'])
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents = f'''این اطلاعات رو تحلیل کن. موارد زیر رو در نظر بگیر:

1.  **حذف موارد بی‌ارزش:** اخباری که ارزش تحلیلی ندارند (مانند تبلیغات، اخبار تکراری، یا مطالب غیرمرتبط) رو کنار بگذار.
2.  **تمرکز بر کیفیت:** برای من کیفیت تحلیل مهم‌تر از کمیت خروجی است.
3.  **یکپارچه‌سازی:** اگر اخبار مرتبط و مشابهی وجود دارند، آن‌ها را به صورت یکپارچه و خلاصه‌شده ارائه بده.
4.  **کامل بودن موارد:** اگر بخشی از یک خبر یا مورد، نصفه یا ناقص بود، آن را نادیده بگیر.
5.  **خروجی JSON:** خروجی باید دقیقاً مانند فرمت JSON زیر باشد. هیچ پیام، کامنت یا توضیحات اضافی‌ای در خروجی قرار نده. تمام مقادیر (title, summary, category, importance) باید به صورت رشته (string) باشند و دقیقاً به همان شکلی که در کلیدشان ذکر شده، جایگزین شوند.

**دسته‌بندی‌های مجاز برای "category" فقط یکی از موارد زیر است:**
"Economy", "Finance", "Markets", "Investing", "Personal Finance", "Business", "Technology", "Science", "Health", "World".
اگر خبری به هیچ یک از این دسته‌بندی‌ها مرتبط نبود، آن را نادیده بگیر.

**مقیاس اهمیت برای "importance" فقط یکی از مقادیر زیر است:**
"Low", "Medium", "High", "Critical".

**فرمت خروجی مورد انتظار:**
{
    "0": {
        "title": "TITLE_HERE",
        "summary": "SUMMARY_HERE",
        "category": "CATEGORY_HERE",
        "importance": "IMPORTANCE_HERE"
    },
    "1": {
        "title": "TITLE_HERE",
        "summary": "SUMMARY_HERE",
        "category": "CATEGORY_HERE",
        "importance": "IMPORTANCE_HERE"
    }
}

**اطلاعات ورودی:**
{data}''')
        print("gemeni analyzed successfully")
        return response
        
    except:
        print(response)
        print("couldn't get accessed to the gemini, check your network and try again")
        return None
        
    
