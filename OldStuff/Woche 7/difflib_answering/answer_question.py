import json
import difflib

# load dataset
data = json.load(open('bigset.json', encoding="utf-8"))

# make QA-dictionary and questionlist
allQA ={}
allQ = []

for d in data['data']:
    allQA[d["question"]] = d["answercode"]
    allQ.append(d["question"])

#print(allQ[2])

i = input()

closest = difflib.get_close_matches(i, allQ, n=1, cutoff=0.01)

answer = allQA[closest[0]]
questionfromanswer = closest[0]

print("*************QUESTION:")
print(questionfromanswer)
print("*************ANSWER:")
print(answer)
