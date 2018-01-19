import json
import parser
import os
import traceback
import logging
import re
import pprint
data = json.load(open('data.json'))

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'pythoncodes')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

print(repr('\n\t\n'))

k = 0
validparses = 0
invalidparses = 0
dict_nos = {}
dict_ws = {}
i = 0
for d in data['data']:
    i += 1
    if i % 1000 == 0:
        print(i)
    for j in range(len(d['answers'])):
        # print("###############################################################################################################")

        with open('pythoncodes\\{1}-{0}.py'.format(j, d['url'].replace('https://stackoverflow.com/questions/', "")),'r+', encoding='utf8') as pfile:
            code = pfile.read()

            codelist = code.split('\n')
            for s in codelist:
                match = re.match('\S*', s)
                if match is None:
                    continue
                ms = str(match.group())
                if ms in dict_nos:
                    dict_nos[ms] += 1
                else:
                    dict_nos[ms] = 0
                match = re.match('\S*\s*\S*', s)
                if match is None:
                    continue
                ms = str(match.group())
                if ms in dict_ws:
                    dict_ws[ms] += 1
                else:
                    dict_ws[ms] = 0

            pfile.write(code)
            pfile.close()

sortlist_nos =[]
for ms in dict_nos:
    sortlist_nos.append((dict_nos[ms], ms))

sortlist_nos.sort(key=lambda x: x[0], reverse=True)
i = 0
print("no s ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for item in sortlist_nos:
    i += 1
    if i == 100:
        break
    print( str(item[0]) + " = " + repr(item[1]))

sortlist_ws = []
for ms in dict_ws:
    sortlist_ws.append((dict_ws[ms], ms))

sortlist_ws.sort(key=lambda x: x[0], reverse=True)
i = 0
print("s ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for item in sortlist_ws:
    i += 1
    if i == 100:
        break
    print( str(item[0]) + " = " + repr(item[1]))
