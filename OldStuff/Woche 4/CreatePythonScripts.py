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

k = 0
for d in data['data']:
    print(d['url'] + " ###############################################################################################################")

    k += 1
    if k % 1000 == 0:
        print(k)
    #final_directory = os.path.join(current_directory, r'pythoncodes\{0}'.format(d['url'].replace('https://stackoverflow.com/questions/', "")))
    #if not os.path.exists(final_directory):
    #    os.makedirs(final_directory)
    for j in range(len(d['answers'])):

        print("Answer " + str(j) + "  ###############################################################################################################")

        a = d['answers'][j]
        ac = ""
        for i in range(len(a['answercode'])):
            ac += a['answercode'][i] + '\n'

        ac = re.sub(r'Out\s*\[\d*\]:\s', "", ac)
        ac = re.sub(r'In\s*\[\d*\]:\s', "", ac)
        ac = re.sub(r'\s*\.\.\.:\s', "", ac)
        ac = re.sub(r'\s*\.\.\.', "", ac)

        ac = re.sub(r'>>>*\s', "", ac)

        if len(ac) > 0:
            try:
                with open('{0}\\{2}-{1}.py'.format(final_directory, j, d['url'].replace('https://stackoverflow.com/questions/', "")), 'w+', encoding='utf8') as pythonfile:
                    pythonfile.write(ac)
                    pythonfile.close()
            except Exception as e:
                logging.error(traceback.format_exc())

            try:
                tree = parser.suite(open('pythoncodes\\{1}-{0}.py'.format(j, d['url'].replace('https://stackoverflow.com/questions/', ""))).read())
                print("Parsing is good")
            except Exception as e:
                logging.error(traceback.format_exc())
