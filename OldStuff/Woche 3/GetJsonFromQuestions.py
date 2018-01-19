from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time
def createquestionurls(ids):
    questionurls = []
    for id in ids:
        questionurls.append("https://stackoverflow.com/questions/{0}".format(str(id)))
    return questionurls

def printkeysandvalues(page_soup):
    for c in page_soup.find('div', {'class': 'question'}).findAll('pre'):
        print(str(c))
    return

def createjson(urls):
    data =None
    try:
        data = json.load(open('data.json'))
    except:
        data = {"data": []}

    oldurls = [ q['url'] for q in data['data']]


    i = 0
    for url in urls:
        oldtime = time.time()


        i += 1
        if url in oldurls:
            print("[" + str(i) + "|" + str(len(urls)) + "]->")
            continue
        try:
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
            print("[" + str(i) + "|" + str(len(urls)) + "]")
        except:
            print("[" + str(i) + "|" + str(len(urls)) + "]x")
            print(url)
            continue

        page_soup = soup(page_html, "html.parser")
        question = page_soup.find('div', {'class': 'question'})
        qtopic = page_soup.find('a', {'class': 'question-hyperlink'}).text
        #printkeysandvalues(page_soup)
        question = question.find('td', {'class': 'postcell'})
        questionstrings = question.findAll('p')
        questioncode = question.findAll('pre')
        answers = page_soup.findAll('div', {'id': lambda value: value and value.startswith("answer-")})

        jsonpost = {'url': url,
                    'topic': qtopic,
                    'question': {
                        'string': [(q.getText()) for q in questionstrings],
                        'code': [(c.getText()) for c in questioncode]
                    },
                    'answers': [{'answerstring': [(s.getText()) for s in a.findAll('p')],
                                   'answercode': [(c.getText()) for c in a.findAll('pre')],
                                   'votes': (int(a.find('span', {'class': 'vote-count-post '}).text) if a.find('span', {'class': 'vote-count-post '}) is not None else 0),
                                   'isrightanswer': (a.find('span', {'class': 'vote-accepted-on load-accepted-answer-date'}) != None)
                                   } for a in answers]
                    }
        print(jsonpost)
        data['data'].append(jsonpost)

        with open('data.json', 'w+') as json_file:
            jsoned_data = json.dumps(data, indent=True)
            json_file.write(jsoned_data)

        if (i % 250 == 0):
            with open('data{0}.json'.format(i), 'w+') as json_file:
                jsoned_data = json.dumps(data, indent=True)
                json_file.write(jsoned_data)

        if time.time() - oldtime < 0.7:
            time.sleep(0.7 - (time.time()-oldtime ))




idtxt = open('qids.txt', 'r')
lines = idtxt.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

urls = createquestionurls(lines)

createjson(urls)



# questiontext = question.findAll('p')
# questiontext = [q.getText() for q in questiontext]

# questioncode = question.findAll('code')
# questioncode = [c.getText() for c in questioncode]

# jsonresult = {'qID': 0,
#                 'question':{
#                     'qtext': questiontext,
#                     'qcode': questioncode
#                 }
#               }
# jstring = json.dumps(jsonresult,sort_keys=True, indent=4, separators=(',', ': '))
# print(str(jstring))

# answers = page_soup.findAll('div', {'class': 'answer'})
# print(answers)

# print("len answers:" + str(len(answers)))
# with open('data.json', 'w') as f:
#     json.dump(jstring, f)