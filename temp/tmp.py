import json

json_string = "{   \"0\": {     \"title\": \"Trump Spars With Powell Over Fed’s Costly Renovations in Rare Visit\",     \"summary\": \"The administration has repeatedly criticized Jerome H. Powell, the chair of the central bank, for his handling of the economy and the cost of work on the institution’s headquarters.\",     \"category\": \"Markets\",     \"importance\": \"HIGH\"   },   \"1\": {     \"title\": \"How Trump’s Attacks on the Fed Chair Have Intensified\",     \"summary\": \"President Trump has targeted Jerome H. Powell on more than 70 separate occasions, more than half of them since April. His statements fall into four broad categories.\",     \"category\": \"Economy\",     \"importance\": \"HIGH\"   },   \"2\": {     \"title\": \"‘Unprecedented’ Investment Fund Seals Deal for Japan and Expands Trump’s Influence\",     \"summary\": \"President Trump will get to decide where to invest Japanese money and the United States will keep 90 percent of the profits, the White House said.\",     \"category\": \"Markets\",     \"importance\": \"MEDIUM\"   },   \"id\": 6830 }"

python_dict = json.loads(json_string)

print(python_dict)
print(python_dict["0"]["title"])
print(python_dict["id"])