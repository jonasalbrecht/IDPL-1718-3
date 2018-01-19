import json
import string

data = json.load(open('bigset.json'))

i = 0
maxquelength = -1
for d in data['data']:
    i += 1
    if maxquelength < len(d['question']):
        maxquelength = len(d['question'])

print(maxquelength)
print(i)