import json
import string

data = json.load(open('data.json'))

i = 0
a = 0
b = 0
for d in data['data']:
    oi = i
    oa = a
    if d['topic'].find('numpy') > -1 or d['topic'].find('Numpy') > -1:
        i += 1
    for s in d['question']['string']:
        if s.find('numpy') > -1 or s.find('Numpy') > -1:
            a += 1
            break
    if i > oi or a >oa:
        b += 1

print("Number of releant topics= " + str(i))
print("Number of relevant questions= " + str(a))
print("Total Number: " + str(b))

percentages = {}

translator = str.maketrans('', '', string.punctuation)

dd=[{'url': d['url'],
      'topicwords': [ s for s in d['topic'].lower().translate(translator).split(' ')]
      }for d in data['data']]

i = 0
for d1 in dd:
    i += 1
    if i % 1000 == 0:
        print(i)

    percentages[d1['url']] = {}
    for d2 in dd:
        if d2['url'] not in percentages:
            percentages[d2['url']] = {}

        percentage1 = 0
        percentage2 = 0
        if d1 == d2 or d2['url'] in percentages[d1['url']]:
            continue
        for w in d1['topicwords']:
            if w in d2['topicwords']:
                percentage1 += 1

        percentage1 /= len(d1['topicwords']) +len(d2['topicwords'])
        percentage2 /= len(d2['topicwords']) + len(d2['topicwords'])

        if percentage1 > 0.85:
            percentages[d1['url']][d2['url']] = percentage1 *100
        if percentage2 > 0.85:
            percentages[d2['url']][d1['url']] = percentage2 *100


with open('topicpercentage.json', 'w+') as json_file:
    jsoned_data = json.dumps(percentages, indent=True)
    json_file.write(jsoned_data)
