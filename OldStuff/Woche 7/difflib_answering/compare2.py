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
qList = []

for d in data['data']:
    qList.append(d["question"])
    dict[d["question"]] = d["answercode"]

i=0

QsACList = []
for q in qList:
    matches = difflib.get_close_matches(q, qList, n=10, cutoff=0.1)
    codeAnswers = []
    for m in matches:
        qList.remove(m)
        codeAnswers.append(dict[m])

    QsACList.append(QsAC(matches, codeAnswers))
    ts = time.time()
    print(len(qList))
    print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    print(i)
    i+=1
    if i == 100:
        break



with open('QAPairs.json', 'w+') as json_file:
    dataj = {'QsACList': [ { 'questions': qa.questions , 'code': qa.code }  for qa in QsACList] }
    jsoned_data = json.dumps(dataj, indent=True)
    json_file.write(jsoned_data)