import json
import string
import os
import traceback
import logging

data = json.load(open('data.json'))

current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'pythoncodes')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

k = 0
for d in data['data']:
    k += 1
    if k % 1000 == 0:
        print(k)
    #final_directory = os.path.join(current_directory, r'pythoncodes\{0}'.format(d['url'].replace('https://stackoverflow.com/questions/', "")))
    #if not os.path.exists(final_directory):
    #    os.makedirs(final_directory)
    for j in range(len(d['answers'])):
        a = d['answers'][j]
        for i in range(len(a['answercode'])):
            try:
                with open('{0}\\{3}_{1}_{2}.py'.format(final_directory, j, i, d['url'].replace('https://stackoverflow.com/questions/', "")), 'w+', encoding='utf8') as pythonfile:
                    pythonfile.write(a['answercode'][i])
            except Exception as e:
                logging.error(traceback.format_exc())