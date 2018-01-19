import json
from collections import Counter
import pprint
from safewordlist import safewords

# load big dataset
data = json.load(open('bigset.json'))

allQ = []

for d in data['data']:
    allQ.append(d["question"])

bigstring = ' '.join(allQ)
wordcount = Counter(bigstring.split()).most_common(200)

wordlist = []
for x in wordcount:
    wordlist.append(x[0])

for sw in safewords:
    if sw in wordlist: wordlist.remove(sw)

print(wordlist)
