import ollama
def answer(data):

    response = ollama.chat(model='gemma3:1b', messages=[{

        'role': 'user', 
        
        'content': f'''این اطلاعات رو تحلیل کن اون هایی که ارزش تحلیل ندارن رو کنار بزار و باقی مونده ها رو درنظر بگیر و تحلیل کن  میتونی اونهایی که به هم مرتبط هستن رو بکی کنی (برای من مهم کیفیته نه کمیت ) تمام این مقدار ها باید برابر همون جیزی باشن که در کلیدشون ذکر شده و هیج گونه پیام یا کامنتی نزار اگه یه موردی نصفه نیمه بود اون رو هم حساب نکن . درنهایت مانند جیسونی که فرستادم خروجی بده: {{ "0": {{ "title": "TITLE_HERE", "summary": "SUMMARY_HERE", "category": "CATEGORY_HERE", "importance": "IMPORTANCE_HERE" }} }} اطلاعات ورودی: {data}'''
        
        }])


    response = response.message.content
    print(25)
    return(response)