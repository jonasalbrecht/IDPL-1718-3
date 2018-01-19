import json
import string

data = json.load(open('data.json'))

words = {}
translator = str.maketrans('', '', string.punctuation)

i = 0
for d in data['data']:
    i += 1
    if i % 1000 == 0:
        print(i)
    wordlist = d['topic'].lower().translate(translator).split(' ')

    for sl in d['question']['string']:
        wordlist.extend(sl.lower().translate(translator).split(' '))

    for a in d['answers']:
        for sl in a['answerstring']:
            wordlist.extend(sl.lower().translate(translator).split(' '))

    for w in wordlist:
        if w not in words:
            words[w] = 1
        else:
            words[w] += 1

sortedwords = []

while len(words) > 0:
    biggestkey = None
    biggestvalue = -1

    for key in words:
        if words[key] > biggestvalue:
            biggestkey = key
            biggestvalue = words[key]

    sortedwords.append((biggestvalue,biggestkey))
    del words[biggestkey]

    if len(words) % 1000 == 0:
        print(len(words))


with open('wordcount.json', 'w+') as json_file:
    jsoned_data = json.dumps({ 'data': sortedwords}, indent=True)
    json_file.write(jsoned_data)