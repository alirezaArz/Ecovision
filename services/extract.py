import json
import os
import random
import sys
import time
from datetime import datetime
from datetime import datetime
import re
from services import systems as system
from services import navigation as navigation
from services.Scrapers import nytimes as nytimes
from services.Scrapers import dnsd as dnsd
from services.Scrapers import bonbast as bonbast
from services.APIs import gecko as gecko
from services.AI import gemeni as gemeni

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
Navpath = os.path.join(project_root, 'services', 'Data')

class Extract():
    def __init__(self):
        pass



    def geminiMx1(self, data):
        print("saving")
        try:
            text_content = data.candidates[0].content.parts[0].text
            
            if text_content.startswith("```json"):
                text_content = text_content[len("```json"):].strip()
            if text_content.endswith("```"):
                text_content = text_content[:-len("```")].strip()
                
            LastAnalyze = json.loads(text_content)

            output = []
            current_date = datetime.now().isoformat()

            for item_key_str, original_item_data in LastAnalyze.items():
                transformed_item = {}

                try:
                    transformed_item["id"] = int(item_key_str) + 1
                except ValueError:
                    transformed_item["id"] = item_key_str

                transformed_item["title"] = original_item_data.get("title", "")
                transformed_item["summary"] = original_item_data.get("summary", "")
                transformed_item["category"] = original_item_data.get("category", "news")
                
                if transformed_item["category"] == "Economy":
                    transformed_item["image"] = (f'images/economy/im{random.randint(1, 30)}.jpg')
                elif transformed_item["category"] == "Finance":
                    transformed_item["image"] = (f'images/finance/im{random.randint(1, 15)}.jpg')
                elif transformed_item["category"] == "Investing":
                    transformed_item["image"] = (f'images/investing/im{random.randint(1, 10)}.jpg')
                elif transformed_item["category"] == "Markets":
                    transformed_item["image"] = (f'images/markets/im{random.randint(1, 10)}.jpg')
                elif transformed_item["category"] == "Science":
                    transformed_item["image"] = (f'images/science/im{random.randint(1, 10)}.jpg')
                elif transformed_item["category"] == "Technology":
                    transformed_item["image"] = (f'images/technology/im{random.randint(1, 10)}.jpg')
                
                transformed_item["importance"] = original_item_data.get("importance", "medium")
                transformed_item["date"] = current_date
                output.append(transformed_item)

            lastResult = system.vgsy.Navread("LastAnalyze")
            lastResult["newsData"][:] = output

            with open(os.path.join(Navpath, "LastAnalyze.json"), 'w', encoding='utf-8') as file:
                json.dump(lastResult, file, indent=4, ensure_ascii=False)
            
            navigation.nav.separate()
            print("LastAnalyze saved successfully")

        except Exception as e:
            print(f"Unable to extract the AI's response with method Mx1: {e}, directing to Mx2...")
            self.geminiMx2(str(data))

    def geminiMx2(self, data):
        try:
            result = []
            memoId = []
            pattern = r'"\d+":\s*\{.*?\}'
            matches = re.findall(pattern, data, re.DOTALL)
            if matches:
                print('pattern matched')
                print(f"{len(matches)} result(s) found!")
                for item in matches:
                    id = r"\d+"
                    itemId = re.search(id, item)
                    title = r'"title": "(.*?)"'
                    itemTitle = re.search(title, item)
                    summary = r'"summary": "(.*?)"'
                    itemSummary = re.search(summary, item)
                    category = r'"category": "(.*?)"'
                    itemCategory = re.search(category, item)
                    importance = r'"importance": "(.*?)"'
                    itemImportance = re.search(importance, item)
                    if itemId and itemCategory and itemImportance and itemSummary and itemTitle:
                        itemTitle = itemTitle.group(1).group(1).replace('\u200c', '')
                        itemSummary = itemSummary.group(1).group(1).replace('\u200c', '')
                        itemCategory = itemCategory.group(1).group(1).replace('\u200c', '')
                        itemImportance = itemImportance.group(1).group(1).replace('\u200c', '')
                        itemId = itemId.group(0).group(1).replace('\u200c', '')
                        if itemId not in memoId:
                            newElement = {}

                            if itemCategory == "Economy":
                                newElement["image"] = (
                                    f'images/economy/im{random.randint(1, 30)}.jpg')
                            elif itemCategory == "Finance":
                                newElement["image"] = (
                                    f'images/finance/im{random.randint(1, 15)}.jpg')
                            elif itemCategory == "Investing":
                                newElement["image"] = (
                                    f'images/investing/im{random.randint(1, 10)}.jpg')
                            elif itemCategory == "Markets":
                                newElement["image"] = (
                                    f'images/markets/im{random.randint(1, 10)}.jpg')
                            elif itemCategory == "Science":
                                newElement["image"] = (
                                    f'images/science/im{random.randint(1, 10)}.jpg')
                            elif itemCategory == "Technology":
                                newElement["image"] = (
                                    f'images/technology/im{random.randint(1, 10)}.jpg')
                            newElement["id"] = itemId
                            newElement["title"] = itemTitle
                            newElement["summary"] = itemSummary
                            newElement["category"] = itemCategory
                            newElement["importance"] = itemImportance
                            current_iso_date = datetime.now().isoformat()
                            newElement["date"] = current_iso_date
                            memoId.append(itemId)
                            result.append(newElement)
                    lastResult = system.vgsy.Navread("LastAnalyze")
                    lastResult["newsData"][:] = result

                    with open(os.path.join(Navpath, f"LastAnalyze.json"), 'w', encoding='utf-8') as file:
                        json.dump(lastResult, file, indent=4, ensure_ascii=False)
                print("AI's response extracted successfully")
                navigation.nav.separate()
            else:
                print("failed to extract the AI's response!")
        except Exception as e:
            print(f"We had An error while extracting the AI's response: {e}")

# output_dict

ex = Extract()