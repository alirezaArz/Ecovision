import time
from halo import Halo 
import os
import sys
import json
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
		
		self.durationsBackup = {
			'gecko' : 3600,
			'bonbast': 3600,
			'dnsd': 3600,
			'nytimes':3600,
			'yahoo' : 3600,
			"bloomberg": 3600,
			"esdn": 3600
		}
		self.durations = self.durationsBackup.copy()

	def instantrun(self, names = []):
		if names == []:
			bonbast.main()
			dnsd.main()
			nytimes.main()
			yahoo.main()
			gecko.price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'Polygon'}, {'usd'})
			esdn.main()
			bloomberg.main()
		else:
			if 'bonbast' in names:
				bonbast.main()
			if 'dnsd' in names:
				dnsd.main()
			if 'nytimes' in names:
				nytimes.main()
			if 'yahoo' in names:
				yahoo.main()
			if 'gecko' in names:
				gecko.price({'bitcoin', 'ethereum', 'Cardano', 'tether', 'Solana', 'Polygon'}, {'usd'})
			if 'esdn' in names:
				esdn.main()
			if "bloomberg" in names:
				bloomberg.main()



	def runserver(self):
		self.instantrun()
		try:
			while True:
	
				self.next_process_name = min(self.durations, key=lambda k: self.durations[k])
				self.CurrentWaitTime = self.durations[self.next_process_name]
				print(f"\n next process in {int(min(self.durations.values()) / 60)} minutres! for {self.next_process_name}")
				self.spinner.start()

#---------------------------------------------------------- code space
#code that runs here, runs every time a timer hits 0
#------------------------------------------------------------


				time.sleep(self.CurrentWaitTime)

				print('\nbbbooommm')

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
							gecko.price({'bitcoin', 'ethereum', 'tether'}, {'usd'})
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
			print('server is shuted down')

	def lead(self):
		with open(os.path.join(snailpath, f"Snaildata.json"), 'r', encoding='utf-8') as file:
			self.data = json.load(file)
			return(self.data)

	def snailsave(self, sfile):
		text_content = sfile.candidates[0].content.parts[0].text
		if text_content.startswith("```json"):
			text_content = text_content[len("```json"):].strip()
		if text_content.endswith("```"):
			text_content = text_content[:-len("```")].strip()

		parsed_json = json.loads(text_content)

		with open(os.path.join(snailpath, f"Snaildata.json"), 'w', encoding='utf-8') as file:
			json.dump(parsed_json, file, indent=4, ensure_ascii=False)

	def get_news_data(self):
		with open(os.path.join(DATA_PATH, f"nyt.json"), 'r', encoding='utf-8') as file:
			data = json.load(file)
			return(data)

	def analyze(self):
		self.entry = self.get_news_data()
		self.result = gemeni.analyze(self.entry)
		print(self.result)
		self.snailsave(self.result)
		
snail = Snail()		


snail.analyze()