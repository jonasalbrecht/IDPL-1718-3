import json
import difflib
import pprint
data = json.load(open('cleanBigset.json', encoding="utf-8"))

li = []
liqa = []

class QsAC:
    def __init__(self, questions, code):
        self.questions = questions
        self.code = code

QsAClist = []

for d in data['data']:
    li.append(d["question"])
    liqa[d["question"]] = d["answercode"]
    #lo.append(d["question"])

for elem in liqa:
    print("_____________________________________________")
    print("close matches to question:")
    print("?/?/?/?/?/?/")

    QsAClist.append(QsAC(difflib.get_close_matches(elem["question"], li, n=10, cutoff=0.1), elem["code"]))


    for x in difflib.get_close_matches(elem, li, n=10, cutoff=0.1):
        print("..........")
        print(x)
        print("..........")
        li.remove(x)
        #lo.remove(x)
    print("___________________________________________")

