import json
import parser
import os
import traceback
import logging
import re
import pprint
data = json.load(open('data.json'))

bigset = []
for d in data['data']:
    qs = d['topic'] + ':\n'
    qs += '\n'.join(d['question']['string'])

    if len(d['answers']) > 0: #gibt es überhaupt antworten
        highestvote = -1
        ac = ''
        for a in d['answers']:
            c = '\n'.join(a['answercode'])
            if a['votes'] > highestvote:
                ac = c
                highestvote = a['votes']
        if highestvote > -1 and ac != '':
            bigset.append({
                'question': qs,
                'answercode': ac,
            })


for d in bigset:
    print(d)

with open('bigset.json', 'w+') as json_file:
    dataj = {'data': bigset}
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)