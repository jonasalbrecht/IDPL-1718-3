import json
import parser
import os
import traceback
import logging
import re
import pprint
data = json.load(open('data.json'))

collecteddata = 0

smallset = []
for d in data['data']:
    qs = '\n'.join(d['question']['string'])
    if len(qs) <= 100: #frage kürzer als 100 chars
        if len(d['answers']) > 0: #gibt es überhaupt antworten
            highestvote = -1
            ac = ''
            for a in d['answers']:
                c = '\n'.join(a['answercode'])
                if len(c) <= 100 and a['votes'] > highestvote:
                    ac = c
                    highestvote = a['votes']
            if highestvote > -1 and ac != '':
                smallset.append({
                    'question': qs,
                    'answercode': ac,
                })
                collecteddata += 1
    if collecteddata > 999:
        break

for d in smallset:
    print(d)

with open('smallset.json', 'w+') as json_file:
    dataj = { 'data': smallset}
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)