import ollama
import json
import os
def answer(data):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "model.json")

    with open(mode="r", file=DATA_PATH) as file:
        odel = json.load(file)["model"]

    try:
        response = ollama.chat(model=odel, messages=[
    {
        'role': 'system',
        'content': (
            "You are a financial analysis expert. When given data, you will analyze it and respond in the following format:\n"
            '{ "0": { "title": "TITLE_HERE", "summary": "SUMMARY_HERE", '
            '"category": "CATEGORY_HERE", "importance": "IMPORTANCE_HERE" } }\n'
            "Allowed categories: [Economy, Finance, Markets, Investing, Technology, Science]\n"
            "Allowed importance levels: [low, medium, high]"
        )
    },
    {
        'role': 'user',
        'content': f"This is the data that you are given: {data}"
    }
])
        response = response.message.content
        return(response)
    except Exception as e:
        print(f"couldn't get accessed to the local-ai, check ollama and try again: {e}")


