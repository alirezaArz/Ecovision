import time
from halo import Halo 
import sys
from services.APIs import gecko as gecko
from services.Scrapers import dnsd as dnsd
from services.Scrapers import nytimes as nytimes
spinner = Halo(text='', spinner={
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

