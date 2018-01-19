import json

data = json.load(open('QAPairs.json', encoding="utf-8"))

for d in data["QsACList"]:
    print(d["questions"][1])
    print(d["code"][1])
    break