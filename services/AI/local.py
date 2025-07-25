import ollama
def answer():
    data = "Stocks wobble with Trump-Xi call, Musk feud in focus",

    try:
        response = ollama.chat(model='gemma:2b', messages=[{

            'role': 'user', 
            
            'content': f"analyze this{data}",
            "category": "news",
            "importance": "medium",
            "date": "2025-07-05T02:15:08.852514"
        }
            ])
        response = response.message.content
        return(response)
    except Exception as e:
        print(f"couldn't get accessed to the local-ai, check ollama and try again: {e}")

print(answer())

