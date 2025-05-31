import time
from halo import Halo 
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'SnailData')

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from services.APIs import gecko as gecko
from services.Scrapers import bonbast as bonbast
from services.Scrapers import dnsd as dnsd
from services.Scrapers import nytimes as nytimes
from services.Scrapers import yahoo



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
			'gecko' : 60,
			'bonbast': 35,
			'dnsd': 50,
			'nytimes':70,
			'yahoo' : 60
		}
		self.durations = self.durationsBackup.copy()
		print(self.durations)

	def runserver(self):
		try:
			while True:
	
				self.next_process_name = min(self.durations, key=lambda k: self.durations[k])
				self.CurrentWaitTime = self.durations[self.next_process_name]
				print(f"\n next procces in {min(self.durations.values())} minutres! for {self.next_process_name}")
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
							bonbast.getcurrency()
						elif item == "dnsd":
							dnsd.main()
						elif item == "nytimes":
							nytimes.main()
						elif item == "yahoo":
							yahoo.main()
						elif item == "gecko":
							#---------------------------alireza add this one, i don't know how gecko works. too many functions
							pass
						self.durations[item] = self.durationsBackup[item]

				print(f" remaining times: {self.durations}")
				self.spinner.stop()
		except:
			self.spinner.stop()
			print('cut in process')
		finally:
			self.spinner.stop()
			print('server is shuted down')


	def save(self):
		with open(os.path.join(DATA_PATH, f"Snaildata.json"), 'w', encoding='utf-8') as file:
			json.dump('', file, indent=4, ensure_ascii=False)

	def read(self):
		with open(os.path.join(DATA_PATH, f"Snaildata.json"), 'r', encoding='utf-8') as file:
			self.data = json.load(file)
			return(self.data)
		
snail = Snail()		
if __name__ == '__main__':
	snail.runserver()