
from openai import OpenAI
import os
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'gmkey.json')






def summarize_news(news_text):
    
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        key = json.load(file)
        client = OpenAI(api_key=key['gpt']) 

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes news articles concisely."},
            {"role": "user", "content": f"Please summarize the following news article:\n\n{news_text}"}
        ],
        max_tokens=150, # حداکثر طول خلاصه (می‌تونی تغییرش بدی)
        temperature=0.7 # خلاقیت مدل (0.0 کمترین، 1.0 بیشترین)
    )
    return response.choices[0].message.content

sample_news = """
شرکت فلان امروز اعلام کرد که در سه ماهه دوم سال جاری، سود خالص آن‌ها نسبت به مدت مشابه سال قبل ۲۰ درصد افزایش یافته است. این افزایش عمدتاً به دلیل رشد چشمگیر در بازارهای نوظهور و عرضه موفق محصول جدید X بوده است. مدیرعامل شرکت، آقای بهاروند، در یک کنفرانس خبری اظهار داشت که این موفقیت نشان‌دهنده استراتژی‌های صحیح شرکت و تلاش بی‌وقفه کارکنان است و انتظار دارند روند رشد در نیمه دوم سال نیز ادامه داشته باشد.
"""

summary = summarize_news(sample_news)
print("--- خلاصه‌ی خبر ---")
print(summary)