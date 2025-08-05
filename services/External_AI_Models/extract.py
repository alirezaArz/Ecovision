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
from services.External_AI_Models import gemini as gemini

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
Navpath = os.path.join(project_root, 'Data', 'Navigations')

class Extract():
    def __init__(self):
        pass

    def geminiMx1(self, data):
        try:
  
            text_content = data.candidates[0].content.parts[0].text
    
            json_pattern = re.compile(r"```json\s*(.*?)\s*```", re.DOTALL)
            match = json_pattern.search(text_content)
            
            json_string = ""
            if match:
                json_string = match.group(1)
            else:
                json_string = text_content.strip()

            LastAnalyze = json.loads(json_string)

            output = []
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for item_key_str, original_item_data in LastAnalyze.items():
                transformed_item = {}

                try:
                    transformed_item["id"] = int(item_key_str)
                except ValueError:
                    transformed_item["id"] = item_key_str

                transformed_item["title"] = original_item_data.get("title", "").replace('\u200c', '')
                transformed_item["summary"] = original_item_data.get("summary", "").replace('\u200c', '')
                transformed_item["category"] = original_item_data.get("category", "news").replace('\u200c', '')
                
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
                else:
                    transformed_item["image"] = (f'images/default/im{random.randint(1, 5)}.jpg')
                
                transformed_item["importance"] = original_item_data.get("importance", "medium").replace('\u200c', '')
                transformed_item["date"] = current_date
                output.append(transformed_item)
                
            lastResult = system.vgsy.Navread("LastAnalyze")
            lastResult["newsData"][:] = output
            with open(os.path.join(Navpath, "LastAnalyze.json"), 'w', encoding='utf-8') as file:
                 json.dump(lastResult, file, indent=4, ensure_ascii=False)
            
            navigation.nav.separate()
            print("LastAnalyze saved successfully by Mx1")

        except Exception as e:
            print(f"Unable to extract the AI's response with method Mx1: {e}, directing to Mx2...")
            self.geminiMx2(data)


    def geminiMx2(self, data):
        try:
            text_content = data.candidates[0].content.parts[0].text
            
            result = []
            memoId = []
            pattern = r'"\d+":\s*\{[^}]*?\s*"title":\s*"(.*?)"\s*,"summary":\s*"(.*?)"\s*,"category":\s*"(.*?)"\s*,"importance":\s*"(.*?)"\s*\}'
            matches = re.findall(pattern, text_content, re.DOTALL) # جستجو در text_content

            if matches:
                print('pattern matched in Mx2')
                print(f"{len(matches)} result(s) found!")
                for i, item_match_groups in enumerate(matches):
                    itemTitle_str = item_match_groups[0].replace('\u200c', '')
                    itemSummary_str = item_match_groups[1].replace('\u200c', '')
                    itemCategory_str = item_match_groups[2].replace('\u200c', '')
                    itemImportance_str = item_match_groups[3].replace('\u200c', '')
                    itemId_str = str(i)

                    if itemId_str not in memoId:
                        newElement = {}

                        if itemCategory_str == "Economy":
                            newElement["image"] = (
                                f'images/economy/im{random.randint(1, 30)}.jpg')
                        elif itemCategory_str == "Finance":
                            newElement["image"] = (
                                f'images/finance/im{random.randint(1, 15)}.jpg')
                        elif itemCategory_str == "Investing":
                            newElement["image"] = (
                                f'images/investing/im{random.randint(1, 10)}.jpg')
                        elif itemCategory_str == "Markets":
                            newElement["image"] = (
                                f'images/markets/im{random.randint(1, 10)}.jpg')
                        elif itemCategory_str == "Science":
                            newElement["image"] = (
                                f'images/science/im{random.randint(1, 10)}.jpg')
                        elif itemCategory_str == "Technology":
                            newElement["image"] = (
                                f'images/technology/im{random.randint(1, 10)}.jpg')
                        else:
                            newElement["image"] = (f'images/default/im{random.randint(1, 5)}.jpg') 
                            
                        newElement["id"] = itemId_str
                        newElement["title"] = itemTitle_str
                        newElement["summary"] = itemSummary_str
                        newElement["category"] = itemCategory_str
                        newElement["importance"] = itemImportance_str
                        current_iso_date = datetime.now().isoformat()
                        newElement["date"] = current_iso_date
                        memoId.append(itemId_str)
                        result.append(newElement)
                
                lastResult = system.vgsy.Navread("LastAnalyze")
                lastResult["newsData"][:] = result

                with open(os.path.join(Navpath, f"LastAnalyze.json"), 'w', encoding='utf-8') as file:
                    json.dump(lastResult, file, indent=4, ensure_ascii=False)
                print("AI's response extracted successfully by Mx2")
                navigation.nav.separate()
            else:
                print("failed to extract the AI's response with Mx2! No matches found.")
        except Exception as e:
            print(f"We had An error while extracting the AI's response with Mx2: {e}")

# output_dict

ex = Extract()