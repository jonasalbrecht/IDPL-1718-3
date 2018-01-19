import json
import difflib

data = json.load(open('data_arrays_classes.json'))

allQA = {}
allQ = []


q = input()

for d in data:
    allQA[d["text"]] = d["code"]
    allQ.append(d["text"])


closest = difflib.get_close_matches(q, allQ, n=1, cutoff=0.1)

answer = allQA[closest[0]]
print(answer)


