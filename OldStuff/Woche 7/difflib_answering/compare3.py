import json
import difflib
import datetime
import time
data = json.load(open('cleanBigset.json', encoding="utf-8"))

class QsAC:
    def __init__(self, questions, code):
        self.questions = questions
        self.code = code

dict = {}

for d in data['data']:
    dict[d["question"]] = d["answercode"]

i=0
x = []

QsACList = []
for q in dict:
    print(q)
    print(list(dict.keys()))
    matches = difflib.get_close_matches(q, list(dict.keys()), n=10, cutoff=0.1)
    codeAnswers = []
    for m in matches:
        dict.pop(m, None)
        codeAnswers.append(dict[m])

    QsACList.append(QsAC(matches, codeAnswers))
    ts = time.time()
    print(len(dict))
    print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



with open('QAPairs.json', 'w+') as json_file:
    dataj = {'QsACList': [ { 'questions': qa.questions , 'code': qa.code }  for qa in QsACList] }
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)