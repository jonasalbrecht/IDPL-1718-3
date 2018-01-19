import json
import string
dataset = json.load(open('bigset.json'))

datalist = dataset['data']
#datalist = datalist[: 1000]
ldataset = len(datalist)

i = 0
Train = []
Test = []

validchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ 1234567890'

onlylowchar_list = []
for d in datalist:
    s = ''
    for c in d['question']:
        if c in validchars:
            s += c
        else:
            s += ' '
    onlylowchar_list.append(s.lower())
    d['question'] = s.lower()
    d['realquestion'] = s.lower()


worddict = {}
for question in onlylowchar_list:
    for word in question.split():
        if word not in worddict:
            worddict[word] = len(worddict)+1

i = 1
for d in datalist:
    ints = []
    for word in d['question'].split():
        ints.append(worddict[word])
    d['question'] = ints
    d['realanswercode'] = d['answercode']
    d['answercode'] = i
    i += 1

with open('EncodedSetSmall.json', 'w+') as json_file:
    dataj = {'data': [(d['question'], d['answercode']) for d in datalist]}
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)

with open('EncodedSetSmallWithReal.json', 'w+') as json_file:
    dataj = {'data': [d for d in datalist]}
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)

