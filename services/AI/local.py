import ollama
def answer():
    try:
        response = ollama.chat(model='gemma:2b', messages=[{

            'role': 'user', 
            
            'content': '''analyze this :             "title": "As a Nation’s Economy Slows, Some Say It’s No Time for a Free Lunch",
            "summary": "Indonesia’s president promised free meals for every student in the country. But unemployment is rising, and some analysts say he’s making matters worse.",
            "image": "placeholder.svg",
            "category": "news",
            "importance": "medium",
            "date": "2025-07-05T02:15:08.852514"
        }'''
            }])
        response = response.message.content
        return(response)
    except:
        print("couldn't get accessed to the local-ai, check ollama and try again")

print(answer())

