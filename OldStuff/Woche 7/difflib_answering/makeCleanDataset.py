import json
import difflib
import re
from replacewordlist import commonwords

# load bigset
data = json.load(open('bigset.json'))

# clean dataset from unnecessary words
for d in data['data']:
    for w in commonwords:
        d["question"] = re.sub(r"\b" + w + r"\b", " ", d["question"])
    d["question"] = " ".join(d["question"].split())

with open('cleanBigset.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
