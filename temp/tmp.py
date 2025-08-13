import json
from datetime import datetime
import re

data =['''   ```json
{
  "0": {
    "title": "Small Businesses Brace for the Punishing Side Effects of Trump’s Tariffs",
    "summary": "Large firms with big bank balances, workers already in jobs and households near the top of the income ladder will have an easier time navigating the economic waves.",
    "category": "Economy",
    "importance": "High"
  },
  "1": {
    "title": "Car Companies Are Paying Tariffs So You Don’t Have To",
    "summary": "But automakers can’t absorb the cost forever and will soon begin to raise new car prices, analysts say.",
    "category": "Economy",
    "importance": "Medium"
  },
  "4": {
    "title": "New Tariff on ‘Transshipped’ Goods Mystifies Importers",
    "summary": "The Trump administration levied a hefty tariff on goods that are moved through other countries, but it has not yet fully explained its plans.",
    "category": "Economy",
    "importance": "Medium"
  },
  "7": {
    "title": "Swiss Businesses Fear Being ‘Annihilated’ by One of the World’s Highest Tariffs",
    "summary": "Goods shipped from the country face a 39 percent tariff in the U.S., which companies warn will have dire consequences if President Trump cannot be quickly dissuaded.",
    "category": "Economy",
    "importance": "High"
  },
  "8": {
    "title": "Here’s What Could Get More Expensive Under Trump’s Tariffs",
    "summary": "The tariffs are driving up prices on everyday goods as businesses warn they can no longer absorb costs, leaving consumers to foot the bill.",
    "category": "Economy",
    "importance": "High"
  },
  "9": {
    "title": "Effect of U.S. Tariffs on British Companies Is ‘Milder Than Feared,’ Central Bank Says",
    "summary": "Britain’s economy is driven by domestic factors more than global ones right now, the governor of the Bank of England said on Thursday, when the central bank cut interest rates.",
    "category": "Economy",
    "importance": "Medium"
  },
  "10": {
    "title": "Stocks End Mixed, as Investors Take Steeper Tariffs in Stride",
    "summary": "The S&P 500 ended the day 0.1 percent lower, a muted move compared to the upheaval when tariffs were first announced in early April.",
    "category": "Markets",
    "importance": "Medium"
  },
  "11": {
    "title": "Southeast Asia Looks for Clarity From U.S. on ‘Rules of Origin’",
    "summary": "Thailand, Vietnam and other countries in the region face much higher tariffs on exports with Chinese-made components. But questions remain on how the U.S. defines a locally made product.",
    "category": "Economy",
    "importance": "Medium"
  },
  "14": {
    "title": "China’s Exports Surged Again in July, but Not to America",
    "summary": "China is shipping more goods to Southeast Asia and other regions that often re-export them to the United States. China still sells three times as much to the United States as it buys.",
    "category": "Economy",
    "importance": "Medium"
  },
  "15": {
    "title": "Staggering U.S. Tariffs Begin as Trump Widens Trade War",
    "summary": "The duties, which the president announced last week, took effect for about 90 countries just after midnight.",
    "category": "Economy",
    "importance": "High"
  },
  "17": {
    "title": "Trump to Double India’s Tariff as Punishment for Buying Russian Oil",
    "summary": "Tariffs on Indian exports to the United States will surge to 50 percent by late August, as part of an effort by President Trump to pressure Russia into resolving its war in Ukraine.",
    "category": "Economy",
    "importance": "Medium"
  },
  "19": {
    "title": "U.S. Imports Slid in June on Higher Tariffs",
    "summary": "Imports from other countries fell around 4 percent from the previous month as President Trump’s steep tariffs discouraged businesses from ordering goods.",
    "category": "Economy",
    "importance": "Medium"
  }
}
```''', None]

match = re.search(r'(\{.*\})', data[0], flags=re.DOTALL)
json_str = match.group(1)
jsdata = json.loads(json_str)
    
cnt = 0
result = []
for item in jsdata.values():
  current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  outpt = {
    "id": cnt,
    "title": item["title"],
    "summary": item["summary"],
    "category": item["category"],
    "importance":  item["importance"],
    "date": current_date
  }
  result.append(outpt)
  cnt += 1
  
print(result)
  
  