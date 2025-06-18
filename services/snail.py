import time
from halo import Halo 
import os
import sys
import json
from datetime import datetime
import random
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
snailpath = os.path.join(project_root,'services', 'SnailData')
DATA_PATH= os.path.join(project_root , "scraped")


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from services.APIs import gecko as gecko
from services.Scrapers import bonbast as bonbast
from services.Scrapers import dnsd as dnsd
from services.Scrapers import nytimes as nytimes
from services.Scrapers import yahoo
from services.Scrapers import esdn
from services.Scrapers import bloomberg
from services.AI import gemeni as gemeni



class Snail():
	def __init__(self):

		self.spinner = Halo(text='', spinner={
		"interval": 80,
		"frames": [
			"[    ]",
			"[   =]",
			"[  ==]",
			"[ ===]",
			"[====]",
			"[=== ]",
			"[==  ]",
			"[=   ]"
		]
	})
		self.active = True
		self.durationsBackup = {
		}

	def activate(self, name):
		if name == 'bonbast' and name not in self.durationsBackup:
			self.durationsBackup['bonbast'] = 30	
		elif name == 'dnsd' and name not in self.durationsBackup:
			self.durationsBackup['dnsd'] = 3600
		elif name == 'nytimes' and name not in self.durationsBackup:
			self.durationsBackup['nytimes'] = 3600
		elif name == 'yahoo' and name not in self.durationsBackup:
			self.durationsBackup['yahoo'] = 3600
		elif name == 'gecko' and name not in self.durationsBackup:
			self.durationsBackup['gecko'] = 10
		elif name == 'esdn' and name not in self.durationsBackup:
			self.durationsBackup['esdn'] = 3600
		elif name == 'bloomberg' and name not in self.durationsBackup:
			self.durationsBackup['bloomberg'] = 3600
		self.durations = self.durationsBackup.copy()
		print(f"activated {name} service")
		print(f"current durations: {self.durations}")
		print(f"current backup durations: {self.durationsBackup}")
	
	def deactivate(self, name):
		if name == 'bonbast' and name in self.durationsBackup:
			del self.durationsBackup['bonbast']
		elif name == 'dnsd' and name in self.durationsBackup:
			del self.durationsBackup['dnsd']
		elif name == 'nytimes' and name in self.durationsBackup:
			del self.durationsBackup['nytimes']
		elif name == 'yahoo' and name in self.durationsBackup:
			del self.durationsBackup['yahoo']
		elif name == 'gecko' and name in self.durationsBackup:
			del self.durationsBackup['gecko']
		elif name == 'esdn' and name in self.durationsBackup:
			del self.durationsBackup['esdn']
		elif name == 'bloomberg' and name in self.durationsBackup:
			del self.durationsBackup['bloomberg']
		self.durations = self.durationsBackup.copy()
		print(f"deactivated {name} service")
		print(f"current durations: {self.durations}")
		print(f"current backup durations: {self.durationsBackup}")
		
		

	def instantrun(self, name = ''):
			if name == 'bonbast':
				try:
					print("starting bonbast")
					bonbast.main()
					print("bonbast done successfully")
				except:
					print("bonbast failed")

			if name == 'dnsd':
				try:
					print("starting dnsd")
					dnsd.main()
					print("dnsd done successfully")
				except:
					print("dnsd failed")

			if name == 'nytimes':
				try:
					print("starting nytimes")
					nytimes.main()
					print("nytimes done successfully")
				except:
					print("nytimes failed")

			if name == 'yahoo':
				try:
					print("starting yahoo")
					yahoo.main()
					print("yahoo done successfully")
				except:
					print("yahoo failed")

			if name == 'gecko':
				try:
					print("starting gecko")
					gecko.price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
					gecko.percentage()
					print("gecko done successfully")
				except:
					print("gecko failed")

			if name == 'esdn':
				try:
					print("starting esdn")
					esdn.main()
					print("esdn done successfully")
				except:
					print("esdn failed")

			if name == "bloomberg":
				try:
					print("starting bloomberg")
					bloomberg.main()
					print("bloomberg done successfully")
				except:
					print("bloomberg failed")

			if name == 'analyze':
				try:
					print("starting snail")
					self.analyze()
					print("analyze done successfully")
				except:
					print("analyze failed")


	def runserver(self):
		try:
			while self.active and self.durations:
	
				self.next_process_name = min(self.durations, key=lambda k: self.durations[k])
				self.CurrentWaitTime = self.durations[self.next_process_name]
				print(f"\n next process in {int(min(self.durations.values()) / 60)} minutres! for {self.next_process_name}")
				self.spinner.start()

#---------------------------------------------------------- code space
#code that runs here, runs every time a timer hits 0
#------------------------------------------------------------

				time.sleep(self.CurrentWaitTime)

				for item in self.durations:
					val = self.durations[item]

					self.durations[item] -= self.CurrentWaitTime
					if self.durations[item] == 0:
						if item == "bonbast":
							bonbast.main()
						elif item == "dnsd":
							dnsd.main()
						elif item == "nytimes":
							nytimes.main()
						elif item == "yahoo":
							yahoo.main()
						elif item == "gecko":
							gecko.price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'dogecoin'}, {'usd'})
						elif item == "esdn":
							esdn.main()
						elif item == "bloomberg":
							bloomberg.main()
						self.durations[item] = self.durationsBackup[item]

				print(f" remaining times: {self.durations}")
				self.spinner.stop()
		except:
			self.spinner.stop()
			print('cut in process')
		finally:
			self.spinner.stop()
			print('snail has been deactivated')

	def snailread(self):
		with open(os.path.join(snailpath, f"Snaildata.json"), 'r', encoding='utf-8') as file:
			self.data = json.load(file)
			return(self.data)

	def snailsave(self, sfile):
		text_content = sfile.candidates[0].content.parts[0].text
		if text_content.startswith("```json"):
			text_content = text_content[len("```json"):].strip()
		if text_content.endswith("```"):
			text_content = text_content[:-len("```")].strip()
		snaildata = json.loads(text_content)

		images = ["images/im1.jpg", "images/im2.jpg", "images/im3.jpg", "images/im4.jpg", "images/im5.jpg"]
		output_dict = {}
		output_dict["newsData"] = []	
		current_iso_date = datetime.now().isoformat()
		
		for item_key_str, original_item_data in snaildata.items():
			transformed_item = {}
			
			try:
				transformed_item["id"] = int(item_key_str) + 1
			except ValueError:
				transformed_item["id"] = item_key_str 
            
			transformed_item["title"] = original_item_data.get("title", "")
			transformed_item["summary"] = original_item_data.get("summary", "")
			transformed_item["image"] = random.choice(images)
			transformed_item["category"] = original_item_data.get("category", "news")
			transformed_item["importance"] = original_item_data.get("importance", "medium")
			transformed_item["date"] = current_iso_date
			output_dict["newsData"].append(transformed_item)
		with open(os.path.join(snailpath, f"Snaildata.json"), 'w', encoding='utf-8') as file:
			json.dump(output_dict, file, indent=4, ensure_ascii=False)

	def get_news_data(self):
			data = ""
			files = [ bloomberg, dnsd, esdn, nytimes, yahoo ]
			data += str(bloomberg.load())
			data += str(dnsd.load())
			data += str(esdn.load())
			data += str(nytimes.load())
			data += str(yahoo.load())
			
			print(data)
			return(data)

	def analyze(self):
		self.entry = self.get_news_data()
		self.result = gemeni.analyze(self.entry)
		print(self.result)
		self.snailsave(self.result)
		
snail = Snail()
#snail.runserver()
#snail.instantrun(['yahoo','gecko', 'esdn', 'bloomberg'])		


